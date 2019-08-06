#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:19:39 2019

@author: damienrigden
"""

s = 'Ad hoc polymorphism refers to polymorphic functions that can be applied to \
arguments of different types, but that behave differently depending on the type \
of the argument to which they are applied.'

encrypt = polymorph(s)

print(encrypt)

[[['UV\\UZW]YUZ[U[XUZVQWWU[YU[XXWYZXXXZX]X[UZ[XTU[\\U[V]YX]UZXUZYWZU[[YTQWWYUXZ]YU[YU[XU[UU\\XU[VXZU[[U[YW]XTWXQWWW[YVU[WWXU[]UZ\\U[XXYU[\\]YYUUZ[WVYUQWWWXUZTU[W]YUZUUZX]YWVU[YU[YXWXTWZWYQWWYUU[XQWWUZTU[[UZZYVU[VUZXXYU[]YTQWWXZW[]YUZWUZ\\UZYUZYUZXX]UZXU[WYUQWWYUYZX[WZU[\\QVU]YUZUU\\TYU]YU[]W]UZTYUQWWWWWZUZ[UZTU\\UUZX]YUZWXTUZYUZYWZX]WZXYYUXWU\\XQWWUZWUZXU[YWZU[WUZWXTU[WW\\QWWXZXY]YU[]UZ[UZX]YU[]YZU[YUZXQWWXZW[QWWYUW]UZXQWWUZTU[[UZZYVU[VUZXXYU[]QWWYUXZQWWU\\VUZ[UZ\\UZVUZ[]YYUUZ[UZXYZQWWWVX]WZQWWUZTX[U[YU[UUZ\\WZUZWUT]', 102, 114, 111, 115, 111, 104, 122, 108, 119, 123, 34, 99, 113, 102, 35, 115, 113, 110, 124, 112, 114, 117, 115, 107, 107, 117, 112, 35, 113, 105, 35, 106, 120, 112, 100, 113, 35, 101, 113, 106, 112, 107, 119, 108, 114, 112, 102, 113, 112, 115, 111, 103, 122, 107, 119, 123, 35, 99, 113, 103, 34, 115, 114, 111, 124, 112, 113, 116, 114, 106, 107, 117, 112, 35, 113, 105, 34, 107, 120, 112, 100, 112, 34, 102, 113, 106, 112, 108, 118, 107, 114, 113, 101, 114, 112, 114, 110, 103, 122, 108, 118, 124, 35, 99, 113, 103, 35, 115, 114, 110, 123, 111, 114, 116, 115, 106, 108, 118, 111, 35, 114, 105, 35, 107, 119, 112, 99, 112, 34, 101, 114, 106, 112, 107, 119, 108, 113, 113, 102, 113, 112, 114, 110, 104, 122, 107, 119, 123, 35, 100, 113, 102, 35, 114, 113, 111, 123, 111, 113, 117, 115, 106, 108, 118, 112, 35, 114, 104, 34, 106, 120, 111, 100, 112, 35, 102, 113, 105, 113, 108, 118, 108, 113, 112, 101, 113, 111, 114, 111, 104, 123, 108, 119, 124, 34, 100, 113], {'$'}]]

decrypt = depoly(encrypt)

print(decrypt)

'Ad hoc polymorphism refers to polymorphic functions that can be applied to \
arguments of different types, but that behave differently depending on the type \
of the argument to which they are applied.'