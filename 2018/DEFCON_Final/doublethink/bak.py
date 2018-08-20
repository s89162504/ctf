#!/usr/bin/env python3
#from pwn import *
import re

p = 1 << 6

bcd = {
    ' ' : 0x00,     '¢' : 0x10,         '-' : 0x20,     '&' : 0x30,
    '1' : 0x01,         '/' : 0x11 | p,     'J' : 0x21 | p, 'A' : 0x31,
    '2' : 0x02,         'S' : 0x12 | p,     'K' : 0x22 | p, 'B' : 0x32,
    '3' : 0x03,     'T' : 0x13,         'L' : 0x23,     'C' : 0x33 | p,
    '4' : 0x04,         'U' : 0x14 | p,     'M' : 0x24 | p, 'D' : 0x34,
    '5' : 0x05,     'V' : 0x15,         'N' : 0x25,     'E' : 0x35 | p,
    '6' : 0x06 | p,     'W' : 0x16,         'O' : 0x26,     'F' : 0x36 | p,
    '7' : 0x07,         'X' : 0x17 | p,     'P' : 0x27 | p, 'G' : 0x37,
    '8' : 0x08,         'Y' : 0x18 | p,     'Q' : 0x28 | p, 'H' : 0x38,
    '9' : 0x09 | p,     'Z' : 0x19,         'R' : 0x29,     'I' : 0x39 | p,
    '0' : 0x0a ,        '‡' : 0x1a,         '!' : 0x2a,     '?' : 0x3a | p,
    '#' : 0x0b,         ',' : 0x1b | p,     '$' : 0x2b | p, '.' : 0x3b,
    '@' : 0x0c | p,     '%' : 0x1c,         '*' : 0x2c,     '⌑' : 0x3c,
    ':' : 0x0d,         '=' : 0x1d,         ')' : 0x2d,     '(' : 0x3d,
    '>' : 0x0e,         '\'' : 0x1e,        ';' : 0x2e,     '<' : 0x3e,
    '√' : 0x0f,         '"' : 0x1f,         'Δ' : 0x2f,     '⯒' : 0x3f,

}

op = ',008015,022029,036043,050054,055062,063065,069080/333/M0792502F1.065HELLO WORLD'
#op = '/333/M0792502F1.065HELLO WORLD'

'''
p = 0
for i , c in enumerate( re.findall( '.' , op ) , start = 1 ):
    print( 'd %d %s' % ( i , oct( bcd[c] )[2:].rjust( 3 , '0' ) ) )


'''
p = 0
for i , c in enumerate( re.findall( '.' , op ) , start = 1 ):
    if c == ',':
        print( 'd %d %s' % ( i , oct( bcd[c] | (1 << 6) )[2:].rjust( 3 , '0' ) ) )
    else:
        print( 'd %d %s' % ( i , oct( bcd[c] )[2:].rjust( 3 , '0' ) ) )
    i += 1
