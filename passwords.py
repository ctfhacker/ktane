from collections import Counter, defaultdict

words = ['about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house', 'large', 'learn', 'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound', 'spell', 'still', 'study', 'their', 'there', 'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'world', 'would', 'write']

counts = defaultdict(Counter)

for word in words:
    for index, letter in enumerate(word):
        counts[index][letter] += 1


for index,val in counts.iteritems():
    for letter, num in val.iteritems():
        if num == 1:
            for word in words:
                if word[index] == letter:
                    print (index, letter), word




