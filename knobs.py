#!/usr/bin/env python
leds = raw_input("""
Bottom left 3, then top right 3 as 0's and 1's.
i.e
  x xx
xxxx x
=
111011
> """)

if leds == '111011' or leds == '011010':
    print 'Up'
if leds == '111001' or leds == '010010':
    print 'Down'
if leds == '100010' or leds == '000010':
    print 'Left'
if leds == '111111' or leds == '111100':
    print 'Right'
