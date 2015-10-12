#!/usr/bin/env python
import string

set(['d', 'g', 'k', 'j', 'n', 'q', 'p', 'u', 'w', 'y', 'z'])
morse = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..', 
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'r': '.-.',
    's': '...',
    't': '-',
    'v': '...-',
    'x': '-..-',
}

codes = {}
for key, val in morse.iteritems():
    codes[val] = key

words = {
'shell': 505,
'halls': 515,
'slick': 522,
'trick': 532,
'boxes': 535,
'leaks': 542,
'strobe': 545,
'bistro': 552,
'flick': 555,
'bombs': 565,
'break': 572,
'brick': 575,
'steak': 582,
'sting': 592,
'vector': 595,
'beats': 600,
}

combos = {}
for word in words:
    curr_combo = []
    for num in xrange(len(word)):
        curr_word = ''.join((word+word)[num:num+3])
        combos[curr_word] = word

code = raw_input("""
Disfuser: Please give three letters from morse.

Feed the string of morse code: 
> """)

possibles = []
for key, val in combos.iteritems():
    curr_word = ''.join([morse[letter] for letter in key])
    if code.startswith(curr_word):
        # print val, key, code, words[val]
        print words[val]
