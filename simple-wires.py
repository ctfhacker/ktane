#!/usr/bin/env python

wire = raw_input("""
Enter wire (blUe, blacK, White, Yellow, Red)

""").lower()

print wire

if len(wire) == 3:
    if 'r' not in wire:
        print '2nd  wire'
    elif wire[-1] == 'w':
        print 'last wire'
    elif wire.count('u') > 1:
        print 'cut last blue wire'
    else:
        print 'cut last wire'

elif len(wire) == 4:
    if wire.count('r') > 1:
        print 'if odd, cut last red wire'
    if wire[-1] == 'y' and wire.count('r') == 0:
        print 'cut first wire'
    if wire.count('u') == 1:
        print 'cut first wire'
    if wire.count('y') > 1:
        print 'cut last wire'
    else:
        print 'cut second wire'

elif len(wire) == 5:
    if wire[-1] == 'k':
        print 'if odd, cut fourth wire'
    if wire.count('r') and wire.count('y') > 1:
        print 'cut first wire'
    if wire.count('k') == 0:
        print 'cut second wire'
    else:
        print 'cut first wire'

elif len(wire) == 6:
    if wire.count('y') == 0:
        print 'if odd, cut third wire'
    if wire.count('y') == 1 and wire.count('w') > 1:
        print 'cut fourth wire'
    if wire.count('r') == 0:
        print 'cut last wire'
    else:
        print 'cut fourth wire'


