"""
A dodgy ripoff of rsync for my music files.

To copy the contents of 'Zechs Marquise/Getting Paid/' and 'Grails/' from your
music library to your mounted phone:

    $ $NAME --source $HOME/Music \\
            --destination /mnt/phone/Music \\
           'Zechs Marquise/Getting Paid/' \\
           'Grails/'

The source defaults to `pwd`. This script works best when you are in the
source directory, as you can leave off the source and tab-complete files to
copy:

    $ cd $HOME/Music
    $ $NAME --destination /mnt/phone/Music \\
           'Zechs Marquise/Getting Paid/' \\
           'Grails/'

This never deletes files, and should not be used for transferring back to
your music library. It is designed specifically for transferring to
intermittent FAT devices. File names are munged on the destination to fit FAT
naming restrictions, as well as other conversions that might happen.
"""
from __future__ import annotations

import argparse
import contextlib
import dataclasses
import enum
import os
import pathlib
import sys
import typing as t

from tqdm import tqdm

from . import adapters, sync
from .utils.console import Fore, Style, c


def main() -> None:
    """
    The console entry point. Parses command line arguments and calls run().
    """
    parser = get_parser()
    arguments = parser.parse_args()

    verbosity = Verbosity(min(arguments.verbosity, 3))
    out = Printer(verbosity=verbosity)
    run(
        arguments.source,
        arguments.destination,
        arguments.files,
        out=out,
        dry_run=arguments.dry_run,
    )


def run(
    source: pathlib.Path,
    destination: pathlib.Path,
    to_copy: t.List[pathlib.Path],
    *,
    out: Printer,
    dry_run: bool = False,
) -> None:
    """
    The program entry point. Copies all `to_copy` files from `source` to
    `destination`, where `destination` is some form of FAT filesystem.
    """
    for f in to_copy:
        if f.is_absolute() and not f.is_relative_to(source):
            raise CommandError(f"{str(f)!r} is not relative to source directory {str(source)!r}")

    out(Verbosity.all, "Searching for files to transfer...")
    all_files = sorted(sync.collect_files(source, to_copy))
    out(Verbosity.most, ngettext(
        "Found {count} file in source",
        "Found {count} files in source",
        len(all_files),
    ).format(
        count=c(Style.bright & Fore.green, str(len(all_files)))
    ))

    all_transfers = list(sync.collect_transfers(
        source, destination,
        tqdm(all_files, unit='file', leave=False),
        adapter=adapters.ExFATAdapter(),
    ))

    needs_transfer = [t for t in all_transfers if t.needs_copy]
    needs_transfer_bytes = sum(t.size for t in needs_transfer)
    out(Verbosity.minimal, ngettext(
        "Found {count} file to transfer to destination",
        "Found {count} files to transfer to destination",
        len(needs_transfer),
    ).format(
        count=c(Style.bright & Fore.green, str(len(needs_transfer))),
    ))

    progress: tqdm[sync.Transfer] = tqdm(
        total=needs_transfer_bytes, unit='B', unit_scale=True, unit_divisor=1024,
        disable=out.verbosity is Verbosity.silent,
    )

    with out.redirect(tqdm.write):
        for transfer in all_transfers:
            if transfer.needs_copy:
                symbol = (
                    c(Fore.cyan & Style.bright, "U")
                    if transfer.exists
                    else c(Fore.green & Style.bright, "A")
                )
                out(Verbosity.most, f"{symbol} {str(transfer.source_file)!r}")
                if not dry_run:
                    try:
                        sync.transfer(source, destination, transfer)
                    except IOError as exc:
                        sys.stderr.write(str(exc) + "\n")

                progress.update(transfer.size)
            else:
                out(Verbosity.all, c(Fore.grey_19, f"  {str(transfer.source_file)!r}"))


def get_parser() -> argparse.ArgumentParser:
    """Construct a `syncfat` ArgumentParser."""
    parser = argparse.ArgumentParser(
        prog="syncfat",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        '-f', '--source', type=pathlib.Path, default=os.getcwd(),
        help=(
            "The path to your Music library on your computer. "
            "Defaults to the current directory."
        ))
    parser.add_argument(
        '-t', '--destination', type=pathlib.Path, required=True,
        help="The path to your Music library on your mounted phone.")

    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument(
        '-v', '--verbose',
        action='count', dest='verbosity',
        help=(
            "Print more information when transferring. "
            "Add twice for even more output."
        ))
    verbosity.add_argument(
        '-q', '--quiet',
        action='store_const', dest='verbosity', const=0,
        help="Don't print anything except errors.")
    parser.set_defaults(verbosity=1)

    parser.add_argument(
        '--dry-run', action='store_true', default=False,
        help="Don't actually transfer any files, only print what would happen.")

    parser.add_argument(
        'files', nargs='*', type=pathlib.Path, default=[pathlib.Path('.')],
        help=(
            "The files or directories that should be transferred. "
            "Defaults to transferring the entire `source` directory."
        ))

    return parser


class Verbosity(enum.IntEnum):
    """
    How much noise to make in the console. Select using --quiet or --verbose.
    """
    silent = 0
    minimal = 1
    most = 2
    all = 3


class Writable(t.Protocol):
    def __call__(self, message: str, end: str = ...) -> t.Any: ...


@dataclasses.dataclass
class Printer:
    verbosity: Verbosity
    out: Writable = t.cast(Writable, print)

    def __call__(self, verbosity: Verbosity, message: str, end: str = '\n') -> None:
        if self.verbosity >= verbosity:
            self.out(message, end=end)

    @contextlib.contextmanager
    def redirect(self, out: Writable) -> t.Iterator[None]:
        old_out = self.out
        try:
            self.out = out
            yield
        finally:
            self.out = old_out


def ngettext(
    singular: str,
    plural: str,
    count: int,
) -> str:
    if count == 1:
        return singular
    else:
        return plural


class CommandError(Exception):
    code: int

    def __init__(self, message: str, code: int = 1):
        super().__init__(message)
        self.code = code

    def exit(self) -> t.NoReturn:
        print(str(self), file=sys.stderr, flush=True)
        sys.exit(self.code)


@contextlib.contextmanager
def handle_errors() -> t.Iterator[None]:
    try:
        yield
    except CommandError as exc:
        exc.exit()
    except KeyboardInterrupt:
        sys.exit(1)
