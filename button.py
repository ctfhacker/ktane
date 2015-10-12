#!/usr/bin/env python
from colors import color as colorify

problem = raw_input("""
Enter color (rywb) then the word

r abort
y detonate
> """)
color, word = problem.split()
word = word.lower()

def print_hold_colors():
    print colorify('Blue - 4', 'blue')
    print('White - 1')
    print colorify('Yellow - 5', 'yellow')
    print 'ANY OTHER - 1'

if color == 'b' and word == 'abort':
    print 'Press and Hold'
    print_hold_colors()
    sys.exit(1)

if word.startswith('det'):
    print 'if >1 battery, press and release'

if color == 'w':
    print 'if "CAR", press and hold'
    print_hold_colors()

print 'if >2 batteries and "FRK", press and release'

if color == 'y':
    print 'press and hold'
    print_hold_colors()

if color == 'r' and word.startswith('hol'):
    print 'press and release'

print 'press and hold'
print_hold_colors()







