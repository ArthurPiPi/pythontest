#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: nothing -*-

a = 'qghx{jo7h1oh0v54vh9jqc0c473v7hhvc8881}'
aa = ''
for i in a:
    for j in range(0,26):
    	if i>='a' and i<='z':
	        c = (7*j+7)%26  #仿射加密公式，自行更改
	        # print c
	        if(c==ord(i)-97):
	            aa+=chr(j+97)
	            break
    	else:
	        aa+=i
	        break
print(aa)