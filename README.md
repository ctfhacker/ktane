# Keep Talking and Nobody Explodes (KTANE) toolkit

## Button

Give the first letter of the button and word. The given options are listed in order of possibility.

```
$ ./button.py

Enter color (rywb) then the word

r abort
y detonate
> r abort
------------------------------------------------------------
if >2 batteries and "FRK", press and release
------------------------------------------------------------
press and hold
Blue - 4
White - 1
Yellow - 5
ANY OTHER - 1
```

## Complicated Wires

Give the attributes of each wire from left to right ([r]ed, [b]lue, [l]ed, [s]tar). The characteristics of bomb are given. 

```
$ ./complicated-wires.py
Enter wire 0 (rbsl): r
Enter wire 1 (rbsl):
Enter wire 2 (rbsl): rbls
Enter wire 3 (rbsl): sb
Enter wire 4 (rbsl): lr
Enter wire 5 (rbsl): rbs

even digit # Cut if even digit
cut
dont cut
dont cut
>1 battery # Cut if >1 battery
parallel port # Cut if parallel port
```

## Knobs

Give the LEDs of the lower left three then upper right three.

```
$ ./knobs.py

Bottom left 3, then top right 3 as 0's and 1's.
i.e
x xx
xxxx x
=
111011
> 111011
Up
```

## Maze

Give coordinates of ONE indicator, the start, then the finish in "across, then down" fashion.

Example:
```
x x x
x x ?
x x x
x x x

Coords of ?: (3, 2)
```

```
$ ./maze.py
Indicator: 12
Start: 11
Finish: 66
Path:  R2 D1 L1 D1 R1 D1 R1 U1 R2 D3
```

## Morse

Give THREE letters worth of morse code. Does not have to begin with the word, only three complete letters.

```
$ python morse.py

Disfuser: Please give three letters from morse.

Feed the string of morse code:
> -.......
545
```

## Passwords

Give the first three columns worth of letters. If want fewer columns, give the number also on the command line.

The options of words are listed

```
$ ./passwords.py
First column of letter: tsqedc
Second column of letter: heiazq
Third column of letter: eipoul
['their', 'there', 'these', 'thing', 'think']
```

```
$ ./passwords.py 2
First column of letter: iqetas
Second column of letter: hacqey
['their', 'there', 'these', 'thing', 'think', 'three']
```

## Wire Sequence

Give the color and letter of the current wire and `Cut` and `Don't Cut` is then shown. Note: the colors are below:

```
[r]ed
bl[u]e
blac[k]
```

```
$ ./sequence.py

Enter color and letter of next wire:
Colors: Red, blUe, blacK
Letters: a, b, c
> ra
Don't Cut
> ra
Don't Cut
> ra
Cut
```

## Simple Wires

Give all the wires from top to bottom. Due to blue and black having the same first 2 letters, we are using a slightly different letter for those two.

```
Colors:
[r]ed
[y]ellow
[w]hite
bl[u]e
blac[k]
```

```
$ ./simple-wires.py

Enter wire (blUe, blacK, White, Yellow, Red)

uky
uky
2nd wire
```
