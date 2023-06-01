from random import choice, randint
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


def get_random_passwd(size:int=15, min_num:int=1, min_punc:int=1,
                      avoid_ambiguous_characters:int=True) -> str:
    if avoid_ambiguous_characters:
        character = Unambiguous
    else:
        character = Ambiguous
    
    num_of_num = randint(min_num, size - min_punc - 2)
    num_of_punc = randint(min_punc, size - num_of_num - 2)
    return
