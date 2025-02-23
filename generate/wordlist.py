# EFF's Long Wordlist from https://www.eff.org/dice
import os


_dir = os.path.realpath(os.path.join(__file__, '..'))


def load_wordlist(file_name: str) -> tuple[str]:
    with open(os.path.join(_dir, file_name)) as f:
        lines = f.read().splitlines()

    wordlist = []
    for line in lines:
        word = line.split('\t')[-1]
        wordlist.append(word)
    return tuple(wordlist)


five_dice = load_wordlist('eff_large_wordlist.txt')
four_dice_1 = load_wordlist('eff_short_wordlist_1.txt')
four_dice_2 = load_wordlist('eff_short_wordlist_2_0.txt')

if __name__ == '__main__':
    from secrets import choice

    print(choice(five_dice))
    print(choice(four_dice_1))
    print(choice(four_dice_2))
