from dataclasses import dataclass
from string import (ascii_lowercase as lowercase_,
                    ascii_uppercase as uppercase_,
                    ascii_letters as letters_,
                    digits as digits_,
                    hexdigits as hexdigits_,
                    punctuation as punctuation_,
                    printable as printable_)

@dataclass
class Character: ...

class Ambiguous(Character):
    lower:str = lowercase_
    upper:str = uppercase_
    number:str = digits_
    punctuation:str = punctuation_

@dataclass
class Unambiguous(Character):
    lower:str = lowercase_.replace('l', '')                  # "l"  ell
    upper:str = uppercase_.replace('I', '').replace('O', '') # "IO" capital i, capital o
    number:str = digits_[2:]                                 # "01" zero and one
    punctuation:str = punctuation_.replace('|', '')          # "|"  vertical bar

@dataclass
class Unicode(Character):
    code_points:frozenset[int] = frozenset(range(0x110000))
    printable_unicode_chars:frozenset[str] = frozenset(
        chr(code_point) for code_point in code_points if chr(code_point).isprintable()
    )
    unprintable_unicode_chars:frozenset[str] = frozenset(
        chr(code_point) for code_point in code_points if not chr(code_point).isprintable()
    )
