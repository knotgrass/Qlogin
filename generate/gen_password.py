from secrets import choice as choice_ # https://docs.python.org/3/library/secrets.html
from random  import (randint as randint_,
                     shuffle as shuffle_,
                     seed    as seed_ )

from .character import Ambiguous, Unambiguous, MesloNerdFont

_NERD_ICON_SETS = (
    'pomicons', 'powerline', 'powerline_extra', 'iec_power',
    'fa_extension', 'weather', 'seti_ui', 'devicons', 'codicons',
    'font_awesome', 'progress', 'font_logos', 'octicons',
    'material_design', 'heavy_angle_brackets',
)


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
    num_of_num = randint_(min_num, size - min_punc - min_num_of_letters)
    num_of_punc = randint_(min_punc, size - num_of_num - min_num_of_letters)
    num_of_lower = size - num_of_num - num_of_punc - 1
    num_of_upper = size - num_of_num - num_of_punc - num_of_lower

    passwd = [choice_(character.lower) for _ in range(num_of_lower)]    \
           + [choice_(character.upper) for _ in range(num_of_upper)]     \
           + [choice_(character.punctuation) for _ in range(num_of_punc)] \
           + [choice_(character.number) for _ in range(num_of_num)]

    shuffle_(passwd)
    str_passwd = ''.join(passwd)
    # print(str_passwd)
    # print(f'num_of_num = {num_of_num}\nnum_of_punc = {num_of_punc} \nnum_of_lower = {num_of_lower} \nnum_of_upper = {num_of_upper}')
    # print()
    return str_passwd, (num_of_num, num_of_punc, num_of_lower, num_of_upper)


def get_nerdfont_passwd(size:int=20, min_num:int=1, min_punc:int=1,
                        min_icons:int=3,
                        glyph_sets:list[str]|None=None,
                        seed:int|None=None
                        ) -> tuple[str, tuple[int, int, int, int, int]]:
    """Generate a password mixing ASCII characters with Nerd Font glyphs.

    Parameters
    ----------
    size         : total password length
    min_num      : minimum digit characters
    min_punc     : minimum punctuation characters
    min_icons    : minimum Nerd Font icon characters
    glyph_sets   : which icon sets to draw from (None = all 15 sets)
    seed         : reproducible PRNG seed (None = non-deterministic)

    Returns
    -------
    (password_string, (num_lower, num_upper, num_num, num_punc, num_icons))
    """
    seed_(seed)
    nf = MesloNerdFont

    sets = glyph_sets or _NERD_ICON_SETS
    icon_pool = ''.join(getattr(nf, s) for s in sets if hasattr(nf, s))
    if not icon_pool:
        raise ValueError(f"No valid glyph sets found in: {sets}")

    min_letters = 2  # at least 1 lower + 1 upper
    total_min = min_letters + min_num + min_punc + min_icons
    if size < total_min:
        raise ValueError(
            f"size={size} is too small for the required minimums (need >= {total_min})"
        )

    slack = size - total_min

    num_of_icons = min_icons + randint_(0, max(0, slack // 3))
    remaining    = size - num_of_icons
    num_of_num   = randint_(min_num,  max(min_num,  remaining // 4))
    remaining   -= num_of_num
    num_of_punc  = randint_(min_punc, max(min_punc, remaining // 3))
    remaining   -= num_of_punc
    num_of_upper = max(1, remaining // 3)
    num_of_lower = remaining - num_of_upper

    passwd = [choice_(nf.lower)      for _ in range(num_of_lower)]  \
           + [choice_(nf.upper)      for _ in range(num_of_upper)]  \
           + [choice_(nf.punctuation)for _ in range(num_of_punc)]   \
           + [choice_(nf.number)     for _ in range(num_of_num)]    \
           + [choice_(icon_pool)     for _ in range(num_of_icons)]

    shuffle_(passwd)
    str_passwd = ''.join(passwd)
    return str_passwd, (num_of_lower, num_of_upper, num_of_num, num_of_punc, num_of_icons)


if __name__ == '__main__':
    for _ in range(1000):
        str_passwd, nums = get_random_passwd(size=15)

    print("--- Nerd Font password samples ---")
    for _ in range(5):
        pw, counts = get_nerdfont_passwd(size=20)
        print(f"{pw}  lower={counts[0]} upper={counts[1]} "
              f"num={counts[2]} punc={counts[3]} icons={counts[4]}")
