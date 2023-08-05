from __future__ import annotations

import argparse
import logging
import os
import shutil
import time
import zipfile
from pathlib import Path
from typing import Set, TypedDict

# import rarfile
import py7zr

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class Args(TypedDict):
    source: Path
    recursive: bool


def get_from_args() -> Args:
    ret: Args = {"source": Path("."), "recursive": False}
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

    ret["source"] = src
    ret["recursive"] = args.recursive

    return ret


def is_rar_or_zip(file: Path) -> bool:
    suffix = file.suffix.lower()
    # return (suffix == ".rar") or (suffix == ".zip")
    return suffix == ".zip"


def not_in_ignore(file: Path, ignore: Set[Path]) -> bool:
    root_dir = str(file.parent.resolve())
    # print(f"{root_dir=}")
    for i in ignore:
        i_str = str(i.resolve())
        # print(f"{i_str=}")
        if i_str in root_dir:
            # print(f"Ignored! {root_dir}")
            return False
    return True


def get_rar_and_zips(
    source: Path, ignore: Set[Path] = set(), recursive: bool = False
) -> Set[Path]:
    rar_and_zips: Set[Path] = set()

    for root, dirs, files in os.walk(source, topdown=True):
        for file in files:
            full_file = Path(root) / file
            if is_rar_or_zip(full_file) and not_in_ignore(full_file, ignore):
                logger.debug(f"Found file {full_file}")
                rar_and_zips.add(full_file)
        if not recursive:
            break

    return rar_and_zips


def change_zip_to_7z(file: Path, dest: Path) -> None:
    logger.debug(f"Extracting zip {file} to {dest}")
    with zipfile.ZipFile(file, "r") as zip_ref:
        zip_ref.extractall(dest)


def change_rar_to_7z(file: Path, dest: Path) -> None:
    logger.debug(f"Extracting rar {file} to {dest}")
    logger.debug(f"RAR: not implemented!")
    # with zipfile.ZipFile(file, "r") as zip_ref:
    #     zip_ref.extractall(dest)


def create_7z_from_dir(src: Path, file_7z: Path) -> None:
    cur_dir = Path.cwd()
    with py7zr.SevenZipFile(file_7z, "w") as archive:
        logger.debug(f"Changing dir to {src}")
        os.chdir(src)
        archive.writeall(".")
        os.chdir(cur_dir)
    logger.debug(f"Created {file_7z}")


def change_to_7z(file: Path) -> None:
    temp_folder = Path(str(file) + "_temp_dir")
    logger.debug(f"Creating temp dir {temp_folder}")
    temp_folder.mkdir(exist_ok=True)

    suffix = file.suffix.lower()
    if suffix == ".zip":
        change_zip_to_7z(file, temp_folder)
    elif suffix == ".rar":
        change_rar_to_7z(file, temp_folder)

    basename_file_7z = file.name.replace(file.suffix, ".7z")
    file_7z = file.with_name(basename_file_7z)

    logger.debug(f"Creating 7z from {temp_folder} to {file_7z}")
    create_7z_from_dir(temp_folder, file_7z)

    logger.debug(f"Removing temp dir {temp_folder}")
    shutil.rmtree(temp_folder, ignore_errors=True)


def change_to_7z_iterate(files: Set[Path]) -> None:
    for file in files:
        change_to_7z(file)


def delete_rar_and_zip(file: Path, check_if_7z_exists: bool = True) -> None:
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
    for file in files:
        delete_rar_and_zip(file, check_if_7z_exists=check_if_7z_exists)


def get_total_size(files: Set[Path]) -> int:
    total_size: int = 0
    for file in files:
        total_size += file.stat().st_size
    return total_size


def main() -> None:
    logger.info("Starting program")
    start_time = time.time()

    args = get_from_args()
    source = args["source"]
    recursive = args["recursive"]

    rar_and_zips = get_rar_and_zips(source, recursive=recursive)
    change_to_7z_iterate(rar_and_zips)
    delete_rar_and_zips_iterate(rar_and_zips)

    elapsed_time = time.time() - start_time
    logger.info(f"Finished in {elapsed_time:.2f} seconds")
