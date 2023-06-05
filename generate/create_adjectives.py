from nltk.corpus import wordnet
from string import digits


def check_contain_digit(word:str) -> bool:
    for char in word:
        if char in digits:
            return False
    return True

adjectives = []

for synset in wordnet.all_synsets(pos=wordnet.ADJ):
    for lemma in synset.lemmas():
        adj = lemma.name()
        if check_contain_digit(adj):
            if '-' in adj:
                adjectives.extend(adj.split('-'))
            elif '_' in adj:
                adjectives.extend(adj.split('_'))
            else:
                adjectives.append(adj)

adjectives = set(adjectives)
with open('generate/eng_adj.txt', 'w') as f:
    f.write('\n'.join(adjectives))

print(len(adjectives))
