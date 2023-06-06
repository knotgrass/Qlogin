from nltk import download
from nltk.corpus import wordnet
download('wordnet')

# https://chat.openai.com/share/79c4993d-8060-4a74-acd1-acb81ce27c14
def get_english_word(pos):
    words = []
    for synset in wordnet.all_synsets(pos=pos):
        for lemma in synset.lemmas():
            noun:str = lemma.name()
            if noun.isalpha():
                words.append(noun)
            elif '-' in noun:
                words.extend(noun.split('-'))
            elif '_' in noun:
                words.extend(noun.split('_'))
    return set(words)

words = []
for pos in (wordnet.ADJ, wordnet.ADJ_SAT, wordnet.ADV, wordnet.NOUN, wordnet.VERB):
    words.extend(get_english_word(pos))

words = set(words)
with open('generate/eng.txt', 'w', encoding="ascii") as f:
    f.write('\n'.join(words))

print(len(words))
