#!/usr/bin/env python
from colors import color

meaning = {
int('0000', 2): 'cut',
int('0001', 2): 'dont cut',
int('0010', 2): 'cut',
int('0011', 2): '>1 battery',
int('0100', 2): 'even digit',
int('0101', 2): 'parallel port',
int('0110', 2): 'dont cut',
int('0111', 2): 'parallel port',
int('1000', 2): 'even digit',
int('1001', 2): '>1 battery',
int('1010', 2): 'cut',
int('1011', 2): '>1 battery',
int('1100', 2): 'even digit',
int('1101', 2): 'even digit',
int('1110', 2): 'parallel port',
int('1111', 2): 'dont cut'
}

wires = []

for _ in xrange(6):
    wire = raw_input("Enter wire {} (rbsl): ".format(_)).lower()[:4]

    total = 0
    for letter, value in [('r', 8), ('b', 4), ('s', 2), ('l', 1)]:
        if letter in wire:
            total += value

    wires.append(meaning[total])

for wire in wires:
    for name, c in [('cut', 'green'), 
                    ('dont cut', 'red'),
                    ('>1 battery', 'purple'),
                    ('even digit', 'cyan'),
                    ('parallel port', 'blue'),
                    ]:
        if wire == name:
            print color(wire, c)
