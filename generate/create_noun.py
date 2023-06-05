from nltk.corpus import wordnet
from string import digits


def check_contain_digit(word:str) -> bool:
    for char in word:
        if char in digits:
            return False
    return True

def split_word(word:str):
    if '_' in word:
        return word.split('_')
    elif '-' in word:
        return word.split('-')
    return word


nouns = []
for synset in wordnet.all_synsets(pos=wordnet.NOUN):
    for lemma in synset.lemmas():
        noun = lemma.name()
        if check_contain_digit(noun):
            noun = split_word(noun)
            if isinstance(noun, list):
                nouns.extend(noun)
            else:
                nouns.append(noun)

nouns = set(nouns)
with open('generate/eng_noun.txt', 'w') as f:
    f.write('\n'.join(nouns))
print(len(nouns))
