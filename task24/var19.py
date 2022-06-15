s = open('24-s1.txt').read()
lines = s.split()
max_line_q = ''
mx = 0
for line in lines:
    if line.count('Q') >= mx:
        mx = line.count('Q')
        max_line_q = line
min_letter = ''
mn = 2**64
for letter in sorted(set(max_line_q)):
    if max_line_q.count(letter) < mn:
        mn = max_line_q.count(letter)
        min_letter = letter
print(min_letter, s.count(min_letter))

