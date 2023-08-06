from __future__ import annotations

import dataclasses
import enum
import os
import pathlib
import shutil
import typing as t

from . import adapters

Kind = enum.Enum("Kind", ["file", "directory"])


@dataclasses.dataclass
class Transfer:
    source_file: pathlib.Path
    destination_file: pathlib.Path
    kind: Kind
    size: int
    exists: bool
    needs_copy: bool


def collect_files(
    source: pathlib.Path,
    to_copy: t.List[pathlib.Path],
) -> t.Iterable[pathlib.Path]:
    to_copy_absolute = [source / f for f in to_copy]
    yield from (
        f.relative_to(source)
        for d in to_copy_absolute
        for f in _list_files(d)
    )


def _list_files(root: pathlib.Path) -> t.Iterable[pathlib.Path]:
    yield root
    if root.is_file():
        return

    for _parent, dirs, files in os.walk(root):
        parent = pathlib.Path(_parent)
        yield from (parent / f for f in dirs)
        yield from (parent / f for f in files)


def collect_transfers(
    source: pathlib.Path,
    destination: pathlib.Path,
    all_files: t.Iterable[pathlib.Path],
    adapter: adapters.Adapter,
) -> t.Iterable[Transfer]:
    missing_directories: t.MutableSet[pathlib.Path] = set()

    for source_file in all_files:
        destination_file = adapter.munge_path(source_file)

        source_path = source / source_file
        destination_path = destination / destination_file

        # Checking for non-existent files is actually quite time consuming.
        # If a parent directory does not exist, then the child will not either.
        # When we find a missing directory, make a note of it, then check that
        # first as a shortcut.
        if source_file.parent in missing_directories:
            exists = False
        else:
            exists = destination_path.exists()

        if source_path.is_dir():
            if not exists:
                missing_directories.add(source_file)

            yield Transfer(
                source_file=source_file,
                destination_file=destination_file,
                kind=Kind.directory,
                exists=exists,
                size=0,
                needs_copy=not exists,
            )

        elif source_path.is_file():
            source_size = source_path.stat().st_size

            if not exists:
                needs_copy = True
            else:
                destination_size = destination_path.stat().st_size
                needs_copy = (source_size != destination_size)

            yield Transfer(
                source_file=source_file,
                destination_file=destination_file,
                kind=Kind.file,
                exists=exists,
                size=source_size,
                needs_copy=needs_copy,
            )

        else:
            pass


def transfer(
    source: pathlib.Path,
    destination: pathlib.Path,
    transfer: Transfer,
) -> None:
    source_path = source / transfer.source_file
    destination_path = destination / transfer.destination_file

    if transfer.kind is Kind.directory:
        destination_path.mkdir(parents=True, exist_ok=True)
    else:
        shutil.copyfile(source_path, destination_path)
