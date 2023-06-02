from random import choice, randint, shuffle, seed as seed_
from .character import Ambiguous, Unambiguous


def get_random_passwd(size:int=15, min_num:int=1, min_punc:int=1,
                      avoid_ambiguous_characters:int=True,
                      seed:int|None=None ) -> str:
    seed_(seed)
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
    # print(str_passwd)
    # print(f'num_of_num = {num_of_num}\nnum_of_punc = {num_of_punc} \nnum_of_lower = {num_of_lower} \nnum_of_upper = {num_of_upper}')
    # print()
    return str_passwd, (num_of_num, num_of_punc, num_of_lower, num_of_upper)

if __name__ == '__main__':
    for _ in range(1000):
        str_passwd, nums = get_random_passwd(size=15)
