from random import choice
from dataclasses import dataclass
from string import (ascii_lowercase as lowercase_,
                    ascii_uppercase as uppercase_,
                    ascii_letters as letters_,
                    digits as digits_,
                    hexdigits as hexdigits_,
                    punctuation as punctuation_,
                    printable as printable_)


@dataclass
class Ambiguous:
    lower:str = lowercase_[11]                 # "l"  ell
    upper:str = uppercase_[8] + uppercase_[14] # "IO" capital i, capital o
    number:str = digits_[:2]                   # "01" zero and one
    punctuation:str = punctuation_[-3]         # "|"  vertical bar

@dataclass
class Unambiguous:
    lower:str = lowercase_.replace('l', '')                  # "l"  ell
    upper:str = uppercase_.replace('I', '').replace('O', '') # "IO" capital i, capital o
    number:str = digits_[2:]                                 # "01" zero and one
    punctuation:str = punctuation_.replace('|', '')          # "|"  vertical bar


def get_random_passwd(size:int=15, min_num:int=1, min_punc:int=1,
                      avoid_ambiguous_characters:int=True) -> str:
    if avoid_ambiguous_characters:
        all_char = ...
    else:
        all_char = ...

    return

