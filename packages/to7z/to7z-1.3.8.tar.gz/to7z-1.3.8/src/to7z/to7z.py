from __future__ import annotations

import argparse
import logging
import os
import shutil
import zipfile
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Set

import py7zr
from rich.logging import RichHandler

from .rich_console import console

logger = logging.getLogger(__name__)
FORMAT = "%(message)s"
logging.basicConfig(
    level=logging.DEBUG,
    format=FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler(console=console)],
)


@dataclass
class Args:
    source: Path
    recursive: bool


def get_from_args() -> Args:
    """Get command ling arguments from sys args

    Raises:
        RuntimeError: If args.source is not informed

    Returns:
        Args: dict
            Args["source"]: Path
            Args["recursive"]: bool
    """
    ret = Args(Path("."), False)
    parser = argparse.ArgumentParser("to7z")
    parser.add_argument("source", type=Path)
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("-r", "--recursive", action="store_true")
    args = parser.parse_args()
    if args.source is None:
        raise RuntimeError("Expected source arg")

    logger.setLevel(logging.INFO)
    if args.debug:
        logger.setLevel(logging.DEBUG)

    logger.debug(f"Arguments: {args}")

    src = Path(args.source).resolve()

    ret.source = src
    ret.recursive = args.recursive

    return ret


def is_rar_or_zip(file: Path) -> bool:
    """Return True if file is a .zip

    Args:
        file (Path): File to check

    Returns:
        bool: True if file is .zip
    """
    return file.suffix.lower() == ".zip"


def not_in_ignore(file: Path, ignore: Set[Path]) -> bool:
    """Check if file is not in a ignored directory

    Args:
        file (Path): File to check
        ignore (Set[Path]): Set containing ignored directories

    Returns:
        bool: True if file is not contained int ignore directories
    """
    root_dir = str(file.parent.resolve())
    for i in ignore:
        if str(i.resolve()) in root_dir:
            return False
    return True


def get_rar_and_zips(
    source: Path,
    ignore: Set[Path] = set(),
    recursive: bool = False,
    callback: Callable[[Path, int], None] = None,
) -> Set[Path]:
    """Get all .rar and .zips files from a given path

    Args:
        source (Path): Working path
        ignore (Set[Path], optional): Directories to be ignored. Defaults to set().
        recursive (bool, optional): If True, performs a recursive search. Defaults to False.
        callback (Callable[[Path, int], None], optional): [description]. When a .zip is found, call this function passing the filename (fullpath) and total number of files found. Defaults to None.

    Returns:
        Set[Path]: Set containg all .zip and .rar found
    """
    rar_and_zips: Set[Path] = set()
    total_found = 0

    for root, dirs, files in os.walk(source, topdown=True):
        for file in files:
            full_file = Path(root) / file
            if is_rar_or_zip(full_file) and not_in_ignore(full_file, ignore):
                logger.debug(f"Found file {full_file}")
                rar_and_zips.add(full_file)
                total_found += 1
                if callback is not None:
                    callback(full_file, total_found)

        if not recursive:
            break

    return rar_and_zips


def extract_zip(file: Path, dest: Path, callback: Callable[[int], None] = None) -> None:
    """Extract file .zip contents to dest folder

    Args:
        file (Path): .zip file to be extracted
        dest (Path): Destination of extracted content
    """
    logger.debug(f"Extracting zip {file} to {dest}")

    with zipfile.ZipFile(file, "r") as zf:
        for f in zf.infolist():
            zf.extract(f, dest)
            if callback is not None:
                callback(f.file_size)


def extract_rar(file: Path, dest: Path) -> None:
    """Extract file .rar contents to dest folder

    Args:
        file (Path): .rar file to be extracted
        dest (Path): Destination of extracted content
    """
    logger.debug(f"Extracting rar {file} to {dest}")
    logger.debug(f"RAR: not implemented!")


def create_7z_from_dir(
    src: Path, file_7z: Path, callback: Callable[[int], None] = None
) -> None:
    """Create a .7z from a directory

    Args:
        src (Path): Directory to be compacted. All contents will be compacted.
        file_7z (Path): .7z file (with extension). Ex.: "output.7z"
    """
    cur_dir = Path.cwd()
    logger.debug(f"Changing dir to {src}")
    os.chdir(src)
    with py7zr.SevenZipFile(file_7z, "w") as archive:
        archive.writeall(".")
        # f: Path
        # for f in Path(".").iterdir():
        #     archive.write(f)
        #     if callback is not None:
        #         callback(f.stat().st_size)
    os.chdir(cur_dir)
    logger.debug(f"Created {file_7z}")


def change_to_7z(
    file: Path,
    callback_size: Callable[[int], None] = None,
    callback_action: Callable[[str], None] = None,
) -> None:
    """Convert .rar or .zip file to .7z

    Args:
        file (Path): .zip or .7z file
    """
    temp_folder = Path(str(file) + "_temp_dir")
    logger.debug(f"Creating temp dir {temp_folder}")
    temp_folder.mkdir(exist_ok=True)

    suffix = file.suffix.lower()
    if suffix == ".zip":
        if callback_action is not None:
            callback_action("zip")
        extract_zip(file, temp_folder, callback=callback_size)
    elif suffix == ".rar":
        extract_rar(file, temp_folder)

    basename_file_7z = file.name.replace(file.suffix, ".7z")
    file_7z = file.with_name(basename_file_7z)

    if callback_action is not None:
        callback_action("7z")
    logger.debug(f"Creating 7z from {temp_folder} to {file_7z}")
    create_7z_from_dir(temp_folder, file_7z, callback=callback_size)

    logger.debug(f"Removing temp dir {temp_folder}")
    shutil.rmtree(temp_folder, ignore_errors=True)


def change_to_7z_iterate(files: Set[Path]) -> None:
    """Converts list of .rar and .zip files to .7z files

    Args:
        files (Set[Path]): Set containing all .rar and .zip files to be converted
    """
    for file in files:
        change_to_7z(file)


def delete_rar_and_zip(file: Path, check_if_7z_exists: bool = True) -> None:
    """Delete file. Optionally, checks if there's a .7z with the same name.

    Args:
        file (Path): .rar or .zip file to be deleted
        check_if_7z_exists (bool, optional): Checks if there's a correspondent .7z file before delting the .zip. Defaults to True.
    """
    if check_if_7z_exists:
        file7z = file.with_name(file.name.replace(file.suffix, ".7z"))
        if file7z.is_file():
            logger.debug(f"Safely removing file {file}")
            os.remove(file)
    else:
        logger.debug(f"Removing file {file}")
        os.remove(file)


def delete_rar_and_zips_iterate(
    files: Set[Path], check_if_7z_exists: bool = True
) -> None:
    """Calls delete_rar_and_zip in all files

    Args:
        files (Set[Path]): Files to be deleted
        check_if_7z_exists (bool, optional): Defaults to True.
    """
    for file in files:
        delete_rar_and_zip(file, check_if_7z_exists=check_if_7z_exists)


def get_total_size(files: Set[Path]) -> int:
    """Returns the total size (in bytes) of files.

    Args:
        files (Set[Path]): Files to be analyzed

    Returns:
        int: Size (in bytes) of all files
    """
    total_size: int = 0
    for file in files:
        total_size += file.stat().st_size
    return total_size
