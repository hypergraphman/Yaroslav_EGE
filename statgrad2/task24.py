with open('24.txt') as f:
    s = f.read().strip()

print(max([len(word) for word in s.split('A') if word.count('E') >= 3]))