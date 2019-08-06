#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:48:47 2019

@author: damienrigden

Examples of strings encrypted using polymorph.
Feel free to make more requests
"""

encrypt = polymorph("Hello world!")
print(encrypt)
[[{'%'}, ['VY]V\\\\VWVV]YVWYVU]VXWV]\\V^UV]YV\\[Y[', 101, 114, 112, 115, 111, 104, 123, 108, 119, 124, 35, 100]]]

encrypt2 = polymorph("world! Hello")
print(encrypt2)
[(['V[XVZZ[ZZ^ZVRV[RV\\WXVYZZ^VZW[W', 101, 114, 111, 115, 110, 104, 123, 107, 118, 123, 35, 100], {'%'})]

encrypt3 = polymorph("🐐")
print(encrypt3)
(({'%', '#'}, ['TWZ^U]', 118]),)

encrypt4 = polymorph("a")
print(encrypt4)
[[{'#'}, ['TZV', 102]]]

encrypt5 = polymorph("aa")
print(encrypt5)
[({'&', '%', '$', '#'}, ['\\WVYS', 114, 117])]

encrypt6 = polymorph('aaaaaaaa')
print(encrypt6)
[[['VWT[SVYUT[SVYUT[SXUVYU', 114, 114, 111, 124, 112, 114, 116, 115], {'%', '#'}]]

encrypt7 = polymorph("🂡")
print(encrypt7)
(({'&', '%', '$'}, ['UW]VV\\', 117]),)

encrypt8 = polymorph("⟰")
print(encrypt8)
[[['TUX[\\', 116], {'&', '%', '#'}]]

encrypt9 = polymorph("")
print(encrypt9)
([['[a^', 102], {'*'}],)

encrypt10 = polymorph("\x00")
print(encrypt10)
([['U\\', 114], {'%', '$'}],)

encrypt11 = polymorph("\x01")
print(encrypt11)
([{'%'}, ['VZV', 102]],)

encrypt12 = polymorph("\x00\x00")
print(encrypt12)
[[['ZWZW', 101, 113], {'$'}]]

encrypt13 = polymorph("\x00\x01")
print(encrypt13)
([['UTYU\\', 101, 114], {'$'}],)

encrypt14 = polymorph("\x01\x01")
print(encrypt14)
([['T^T^', 114, 113], {'&', '#'}],)

encrypt15 = polymorph("A")
print(encrypt15)
[[{'&'}, ['WZW', 102]]]

encrypt16 = polymorph("AB")
print(encrypt16)
[({'$', '#'}, ['YU\\]', 114, 113])]

encrypt17 = polymorph("BA")
print(encrypt17)
[[{'&', '%', '$', '#'}, ['Z]VZT', 114, 117]]]

encrypt18 = polymorph("B")
print(encrypt18)
[({'%'}, ['^^', 101])]

encrypt19 = polymorph("1")
print(encrypt19)
([['YZ', 114], {'&', '%', '$', '#'}],)

encrypt20 = polymorph("\n")
print(encrypt20)
[({'$'}, ['XW', 101])]

encrypt21 = polymorph("\n\n")
print(encrypt21)
[[{'&', '%'}, ['WY]\\', 114, 113]]]

encrypt22 = polymorph("\r")
print(encrypt22)
([['TU^', 114], {'&', '$', '#'}],)

encrypt23 = polymorph("\r\n")
print(encrypt23)
([['TV^U\\', 113, 102], {'&', '%', '#'}],)

encrypt24 = polymorph("\r\r")
print(encrypt24)
([['TT[VS', 101, 114], {'#'}],)

encrypt25 = polymorph("AA")
print(encrypt25)
[[{'&', '%'}, ['\\^VZV', 114, 114]]]