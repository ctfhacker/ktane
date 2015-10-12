#!/usr/bin/env python
from collections import Counter, defaultdict
import sys

try:
    columns = int(sys.argv[1])
except IndexError:
    columns = 3

words = ['about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house', 'large', 'learn', 'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound', 'spell', 'still', 'study', 'their', 'there', 'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'world', 'would', 'write']

indexes = {0: 'First', 1: 'Second', 2: 'Third'}

possibles = []


for index in range(columns):
    curr_words = words[:]
    column = raw_input("{} column of letter: ".format(indexes[index]))
    for word in words:
        if word[index] not in column:
            curr_words.remove(word)

    words = curr_words

print words
