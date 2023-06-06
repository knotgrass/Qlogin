from nltk.corpus import wordnet

nouns = []
for synset in wordnet.all_synsets(pos=wordnet.NOUN):
    for lemma in synset.lemmas():
        noun:str = lemma.name()
        if noun.isalpha():
            nouns.append(noun)
        elif '-' in noun:
            nouns.extend(noun.split('-'))
        elif '_' in noun:
            nouns.extend(noun.split('_'))

nouns = set(nouns)
with open('generate/eng_noun.txt', 'w', encoding="ascii") as f:
    f.write('\n'.join(nouns))
print(len(nouns))
