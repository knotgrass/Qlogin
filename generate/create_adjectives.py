from nltk.corpus import wordnet

adjectives = []

for synset in wordnet.all_synsets(pos=wordnet.ADJ):
    for lemma in synset.lemmas():
        adj = lemma.name()
        if adj.isalpha():
            adjectives.append(adj)
        elif '-' in adj:
            adjectives.extend(adj.split('-'))
        elif '_' in adj:
            adjectives.extend(adj.split('_'))

adjectives = set(adjectives)
with open('generate/eng_adj.txt', 'w', encoding="ascii") as f:
    f.write('\n'.join(adjectives))

print(len(adjectives))
