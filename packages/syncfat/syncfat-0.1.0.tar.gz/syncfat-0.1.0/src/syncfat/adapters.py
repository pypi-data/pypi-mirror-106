import abc
import dataclasses
import pathlib
import re

_CONTROL_CHARS = map(chr, [*range(0x00, 0x20), *range(0x7f, 0xa0)])
RE_CONTROL_CHARS = re.compile('[%s]' % re.escape(''.join(_CONTROL_CHARS)))


class Adapter(abc.ABC):
    def munge_path(self, path: pathlib.Path) -> pathlib.Path: ...


@dataclasses.dataclass
class ExFATAdapter(Adapter):
    """
    ExFAT is picky about its filenames. It does not tolerate control
    characters, or the characters in NOT_ALLOWED. It does not toleraste leading
    or trailing spaces or dots in filename components.

    This will munge a filename into something compatible with ExFAT. This does
    not look to see if the destination name it munges to is unique, so this
    might cause collisions for sufficiently bad choices of names.
    """

    NOT_ALLOWED = '"*:<>?|\\'

    RE_NOT_ALLOWED = re.compile('[%s]' % re.escape(NOT_ALLOWED))
    RE_CONSECUTIVE_STAR = re.compile('[*]+')

    def munge_path(self, path: pathlib.Path) -> pathlib.Path:
        return pathlib.Path(*(self._munge_part(p) for p in path.parts))

    def _munge_part(self, name: str) -> str:
        """Munge a single path component"""
        # Replace control characters and disallowed ASCII characters with '*'
        name = RE_CONTROL_CHARS.sub('*', name)
        name = self.RE_NOT_ALLOWED.sub('*', name)
        # Remove all leading '*' or '.' characters
        name = name.strip('.*')
        # Replace all '*' with '-'
        name = self.RE_CONSECUTIVE_STAR.sub('-', name)
        # Done!
        return name
