from __future__ import annotations

import logging
import time
from pathlib import Path
from typing import List, Optional, Set, Tuple

import typer
from rich.logging import RichHandler
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)
from rich.prompt import Prompt
from rich.table import Table
from rich.traceback import install

from to7z import __version__, to7z

from .rich_console import console

install()

logger = logging.getLogger("to7z")
logging.basicConfig(level=logging.DEBUG)
FORMAT = "%(message)s"
logging.basicConfig(
    level=logging.DEBUG,
    format=FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler(console=console)],
)


PROG_NAME = "to7z"
DELETE_DELAY = 0.2
PROCESSING_DELAY = 0.2

app = typer.Typer()


def to_human_size(byts: int) -> str:
    rep: str = "bytes"
    num: float = byts

    if num > 1024:
        num /= 1024.0
        rep = "KB"

    if num > 1024:
        num /= 1024.0
        rep = "MB"

    if num > 1024:
        num /= 1024.0
        rep = "GB"

    return f"{num:.2f} {rep}"


def do_sort(files: Set[Path]) -> Tuple[List[str], List[str]]:

    fls: List[str] = []
    size: List[int] = []
    for file in files:
        fls.append(str(file))
        size.append(file.stat().st_size)

    fls = [x for _, x in sorted(zip(size, fls), reverse=True)]
    size_fmt: List[str] = [to_human_size(s) for s in sorted(size, reverse=True)]

    return fls, size_fmt


def version_callback(value: bool) -> None:
    if value:
        typer.echo(f"to7z version: {__version__}")
        raise typer.Exit()


@app.command()
def cli(
    path: Path = typer.Argument(
        Path(".").resolve(),
        show_default=False,
        help="Path to working directory. Default to current dir",
    ),
    ignore: List[Path] = typer.Option(
        [], "-i", "--ignore", help="Directories to ignore"
    ),
    recursive: bool = typer.Option(False, "-r", "--recursive"),
    no_fetch: bool = typer.Option(
        False,
        "-n",
        "--no-fetch",
        help="Proceed without prompting",
        is_flag=True,
    ),
    keep_original_files: bool = typer.Option(
        False,
        "-k",
        "--keep-original",
        is_flag=True,
        help="Keep original ZIP files. Default is to delete them",
    ),
    debug: bool = typer.Option(False, "--debug", "-d", is_flag=True),
    version: Optional[bool] = typer.Option(
        None, "--version", "-v", callback=version_callback, is_eager=True
    ),
) -> None:

    logger.setLevel(logging.INFO)
    if debug:
        logger.setLevel(logging.DEBUG)

    if not path.is_dir():
        logger.error("Path not found!")
        return

    ig: Path
    for ig in ignore:
        if not ig.is_dir():
            logger.error(f"Dir {ig} in IGNORE not found")
            return

    rar_and_zips = set()

    fetching_message = "Fetching files..."
    with console.status(
        fetching_message,
    ) as status:
        rar_and_zips = to7z.get_rar_and_zips(
            path.resolve(),
            ignore=set(ig.resolve() for ig in ignore),
            recursive=recursive,
        )

    console.print(f"[bold green]OK![/] {fetching_message}")

    total_files = len(rar_and_zips)

    if total_files == 0:
        console.print("None found!")
        return
    elif total_files == 1:
        console.print(f"Found 1 file")
    else:
        console.print(f"Found {total_files} files")

    start_time = time.time()
    zips_total_size = to7z.get_total_size(rar_and_zips)

    if no_fetch:
        console.print(f"Total size: [bold red]{to_human_size(zips_total_size)}")
    else:
        table = Table(
            show_header=True,
            header_style="bold red",
            show_footer=True,
            footer_style="bold red",
        )
        table.add_column("#", style="dim", max_width=5, justify="right", footer="Total")
        table.add_column(
            "Size", justify="right", max_width=12, footer=to_human_size(zips_total_size)
        )
        table.add_column("File", justify="left")

        file_str: str
        size_str: str
        sep = r"\\"
        i = 1
        files_str, sizes_str = do_sort(rar_and_zips)
        for file_str, size_str in zip(files_str, sizes_str):
            f = Path(file_str)
            f_str = f"[dim]{str(f.parent)}[/]{ sep }[bold]{str(f.name)}[/]"
            table.add_row(f"{i:03d}", size_str, f_str)
            i += 1

        console.print(table)

        resp = Prompt.ask(
            "Proceed? [y/N]", console=console, default="n", choices=["y", "n"]
        ).lower()

        if not (resp in ("y", "s", "yes", "sim")):
            return

    progress_bar = lambda: Progress(
        SpinnerColumn(),
        "[progress.description]{task.description}",
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TimeRemainingColumn(),
        "[",
        TimeElapsedColumn(),
        "]",
        "[dim]{task.fields[file]}[/]",
        console=console,
    )
    with progress_bar() as progress:
        task = progress.add_task("[bold]Processing...", total=total_files, file="")
        for file in rar_and_zips:
            progress.update(task, file=str(file.name))
            to7z.change_to_7z(file)
            time.sleep(PROCESSING_DELAY)
            progress.advance(task, 1)
        progress.update(task, file="")

    time.sleep(0.1)
    files_7z: Set[Path] = set(
        [f.with_name(f.name.replace(f.suffix, ".7z")) for f in rar_and_zips]
    )
    total_size_7z = to7z.get_total_size(files_7z)

    console.print(f"Total size after: {to_human_size(total_size_7z)}")

    if total_size_7z < zips_total_size:
        reduced_size = 100.0 * (zips_total_size - total_size_7z) / zips_total_size
        console.print(f"Reduced [green]{reduced_size:.2f}%[/] of size!")

    if keep_original_files:
        console.print("Keeping original files")
    else:
        console.print("Deleting original files")
        with progress_bar() as progress:
            task = progress.add_task(
                "[bold red]Deleting...", total=total_files, file=""
            )
            for file in rar_and_zips:
                progress.update(task, file=str(file.name))
                to7z.delete_rar_and_zip(file)
                time.sleep(DELETE_DELAY)
                progress.advance(task, 1)
            progress.update(task, file="")

    elapsed_time = time.time() - start_time
    time_repr = f"{elapsed_time:.2f} seconds"
    if elapsed_time > 60:
        time_repr = (
            f"{elapsed_time//60.0:.0f} minute(s) {elapsed_time % 60.0:.0f} seconds"
        )
        elapsed_time /= 60.0

    console.print(f"Finished in {time_repr}")


def main() -> None:
    app(prog_name=PROG_NAME)


if __name__ == "__main__":
    main()
