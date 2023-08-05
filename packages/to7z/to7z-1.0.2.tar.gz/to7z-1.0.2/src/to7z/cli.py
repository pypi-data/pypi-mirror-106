from __future__ import annotations

import logging
import time
from pathlib import Path
from typing import List, Optional

import typer

from to7z import __version__, to7z

logger = logging.getLogger("to7z")
logging.basicConfig(level=logging.DEBUG)


def human_size(byts: int) -> str:
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


def version_callback(value: bool) -> None:
    if value:
        typer.echo(f"to7z version: {__version__}")
        raise typer.Exit()


def cli(
    path: Path = typer.Argument(Path(".").resolve()),
    ignore: List[Path] = typer.Option([], "-i", "--ignore"),
    recursive: bool = typer.Option(False, "-r", "--recursive"),
    fetch: bool = typer.Option(
        False,
        "-f",
        "--fetch",
        help="Return list of zips and rar found in path",
        is_flag=True,
    ),
    keep_original_files: bool = typer.Option(
        False,
        "-k",
        "--keep-original",
        # prompt=True,
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

    logger.info("Starting program")

    logger.info("Fetching files...")
    rar_and_zips = to7z.get_rar_and_zips(
        path.resolve(), ignore=set(ig.resolve() for ig in ignore), recursive=recursive
    )
    if len(rar_and_zips) == 0:
        logger.info("None found!")
        return
    elif len(rar_and_zips) == 1:
        logger.info(f"Found 1 file")
    else:
        logger.info(f"Found {len(rar_and_zips)} files")

    start_time = time.time()
    zips_total_size = to7z.get_total_size(rar_and_zips)

    logger.info(f"Total size: {human_size(zips_total_size)}")

    if fetch:
        file: Path
        for i, file in enumerate(rar_and_zips):
            typer.echo(f"{i+1:02d} - {human_size(file.stat().st_size)} - {file}")
        resp = input("Proceed? [y/N] ").lower()
        if not (resp in ("y", "s", "yes", "sim")):
            return

    if not debug:
        with typer.progressbar(rar_and_zips, label="Processing") as files_progress:
            for file in files_progress:
                to7z.change_to_7z(file)
    else:
        to7z.change_to_7z_iterate(rar_and_zips)

    f: Path
    total_size_7z = to7z.get_total_size(
        set([f.with_name(f.name.replace(f.suffix, ".7z")) for f in rar_and_zips])
    )

    logger.info(f"Total size after: {human_size(total_size_7z)}")

    if total_size_7z < zips_total_size:
        logger.info(
            f"Reduced {100.*(zips_total_size- total_size_7z)/zips_total_size:.2f}% of size"
        )

    if keep_original_files:
        logger.info("Keeping original files")
    else:
        logger.info("Deleting original files")
        if not debug:
            with typer.progressbar(rar_and_zips, label="Deleting") as files_progress:
                for file in files_progress:
                    to7z.delete_rar_and_zip(file)
        else:
            to7z.delete_rar_and_zips_iterate(rar_and_zips)

    elapsed_time = time.time() - start_time
    time_repr = f"{elapsed_time:.2f} seconds"
    if elapsed_time > 60:
        time_repr = (
            f"{elapsed_time//60.0:.0f} minute(s) {elapsed_time % 60.0:.0f} seconds"
        )
        elapsed_time /= 60.0
    logger.info(f"Finished in {time_repr}")


def main() -> None:
    typer.run(cli)


if __name__ == "__main__":
    main()
