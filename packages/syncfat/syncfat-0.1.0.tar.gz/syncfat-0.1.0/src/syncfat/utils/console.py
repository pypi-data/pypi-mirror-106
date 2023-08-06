from __future__ import annotations

import enum
import typing as t


def c(colour: t.Union[str, t.Iterable[str]], message: str) -> str:
    """
    Wrap a string in some ANSI escape codes to set colours and styles.
    Works well with `Style`, `Fore`, and `Back` enums.

        print(c(Style.bright & Fore.cyan, "Reticulating splines..."))
    """
    if isinstance(colour, str):
        colour = [colour]
    escape = '\033[' + ';'.join(colour) + 'm'
    reset = '\033[0m'
    return escape + message + reset


class Joinable(str):
    """
    Join two Joinables together with `j1 & j2`, get `[j1, j2]`. Append more
    Joinables on the end with `j1 & j2 & j3 == [j1, j2] & j3 == [j1, j2, j3]`.
    If you're joining a whole bunch together, probably best to use plain list
    operations, as this will get needlessly slow.
    """
    def __and__(self: Joinable, other: Joinable) -> t.List[Joinable]:
        return [self, other]

    def __rand__(self: Joinable, other: t.List[Joinable]) -> t.List[Joinable]:
        return other + [self]


class Style(Joinable, enum.Enum):
    reset = "0"
    bright = "1"


class Fore(Joinable, enum.Enum):
    black = "30"
    red = "31"
    green = "32"
    yellow = "33"
    blue = "34"
    magenta = "35"
    cyan = "36"
    white = "37"
    reset = "39"

    grey_0 = '38:5:232'
    grey_1 = '38:5:233'
    grey_2 = '38:5:234'
    grey_3 = '38:5:235'
    grey_4 = '38:5:236'
    grey_5 = '38:5:237'
    grey_6 = '38:5:238'
    grey_7 = '38:5:239'
    grey_8 = '38:5:240'
    grey_9 = '38:5:241'
    grey_10 = '38:5:242'
    grey_11 = '38:5:243'
    grey_12 = '38:5:244'
    grey_13 = '38:5:245'
    grey_14 = '38:5:246'
    grey_15 = '38:5:247'
    grey_16 = '38:5:248'
    grey_17 = '38:5:249'
    grey_18 = '38:5:250'
    grey_19 = '38:5:251'
    grey_20 = '38:5:252'
    grey_21 = '38:5:253'
    grey_22 = '38:5:254'
    grey_23 = '38:5:255'


class Back(Joinable, enum.Enum):
    black = "40"
    red = "41"
    green = "42"
    yellow = "43"
    blue = "44"
    magenta = "45"
    cyan = "46"
    white = "47"
    reset = "49"
