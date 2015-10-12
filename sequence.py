#!/usr/bin/env python
from collections import defaultdict

counts = defaultdict(int)

sequences = {}
sequences['r'] = [
    ('c'),
    ('b'),
    ('a'),
    ('a', 'c'),
    ('b'),
    ('a', 'c'),
    ('a', 'b', 'c'),
    ('a', 'b'),
    ('b')
    ]
sequences['u'] = [
    ('b'),
    ('a', 'c'),
    ('b'),
    ('a'),
    ('b'),
    ('b','c'),
    ('c'),
    ('a', 'c'),
    ('a')
    ]
sequences['k'] = [
    ('a', 'b', 'c'),
    ('a', 'c'),
    ('b'),
    ('a', 'c'),
    ('b'),
    ('b', 'c'),
    ('a', 'b'),
    ('c'),
    ('c')
    ]

wire = raw_input("""
Enter color and letter of next wire:
Colors: Red, blUe, blacK
Letters: a, b, c
> """)
while True:
    wire = list(wire[:2])
    color = wire[0]
    if wire[1] in sequences[color][counts[color]]:
        print 'Cut'
    else:
        print "Don't Cut"
    counts[color] += 1
    wire = raw_input("> ")


