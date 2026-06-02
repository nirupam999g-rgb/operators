Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#bitwise
a=3
b=4
a&b
0
a=2
b=4
a&b
0
a=5
>>> b=7
>>> a&b
5
>>> bin(3)
'0b11'
>>> a=6
>>> b=8

>>> a&b
0
>>> bin(6)
'0b110'
>>> bin(8)
'0b1000'
>>> #or
>>> a=7
>>> b=9
>>> bin(7)
'0b111'
>>> bin(9)
'0b1001'
>>> a or b
7
>>> a|b
15
>>> a=3
>>> b=5
>>> a^b
6
>>> a=3
>>> b=9
>>> a^b
10
>>> #nor
>>> a>>3
0
>>> a=8
>>> a>>3
1
>>> a<<2
32
