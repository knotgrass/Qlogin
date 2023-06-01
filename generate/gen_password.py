from random import choice, randint, shuffle
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

    # 8 = num_of_letters include both lower & upper
    min_num_of_letters = size // 2 + 1
    num_of_num = randint(min_num, size - min_punc - min_num_of_letters)
    num_of_punc = randint(min_punc, size - num_of_num - min_num_of_letters)
    num_of_lower = size - num_of_num - num_of_punc - 1
    num_of_upper = size - num_of_num - num_of_punc - num_of_lower

    passwd = [choice(character.lower) for _ in range(num_of_lower)]    \
           + [choice(character.upper) for _ in range(num_of_upper)]     \
           + [choice(character.punctuation) for _ in range(num_of_punc)] \
           + [choice(character.number) for _ in range(num_of_num)]

    shuffle(passwd)
    str_passwd = ''.join(passwd)
    print(str_passwd)
    print(f'num_of_num = {num_of_num}\nnum_of_punc = {num_of_punc} \nnum_of_lower = {num_of_lower} \nnum_of_upper = {num_of_upper}')
    print()
    return str_passwd, (num_of_num, num_of_punc, num_of_lower, num_of_upper)

for _ in range(1000):
    str_passwd, nums = get_random_passwd(size=15)
