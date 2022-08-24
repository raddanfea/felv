text = """Imagine a vast sheet of paper on which straight Lines, Triangles, Squares, Pentagons, Hexagons, and other figures, instead of remaining fixed in their places, move freely about, on or in the surface, but without the power of rising above or sinking below it, very much like shadows - only hard and with luminous edges - and you will then have a pretty correct notion of my country and countrymen. Alas, a few years ago, I should have said "my universe": but now my mind has been opened to higher views of things."""

text = text.lower()
words = text.split()


import string
w_punc = list(string.punctuation)

# remove first and last characters if they are punctuation marks
for i, word in enumerate(words):
    if word[-1] in w_punc:
        words[i] = word[:-1]
    if word[0:1] in w_punc:
        words[i] = word[1:]

# remove empty strings
for each in range(words.count("")):
    words.remove('')

# counting into a dict
counts = {}
for each in words:
    if each not in counts.keys():
        counts[each] = 1
    else:
        counts[each] += 1

print(counts)
print('DISTINCT WORDS: ', len(words))