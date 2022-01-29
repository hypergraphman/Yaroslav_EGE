from itertools import permutations

alf = 'svetlana'
words = set()
for word in permutations(alf):
    word = ''.join(word)
    if 'aa' not in word:
        words.add(word)
print(len(words))