Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators
#arthematic
a=2
b=4
print(a+b)
6
print(a-b)
-2
ptint(a**b)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ptint(a**b)
NameError: name 'ptint' is not defined. Did you mean: 'print'?
print(a**b)
16
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
#assignment
a=3
b=5
print(a+=b)
SyntaxError: invalid syntax
a+=b
print(a,b)
8 5
a=3
b=5
a+=b
a
8
a-=1
a
7
a*=3
a
21
a//=3
a
7
a/=2
a
3.5
a**=b
print(a)
525.21875
a*=b
a
2626.09375
#comparision
a=4
b=8
a<b
True
b>a
True
b>=a
True
a<=b
True
a>=b
False
a>b
False
b<=a
False
a!=b
True
a==b
False
a=b=9
a==b
True
#logical
a=6
b=9
a<b and b>a
True
a<=b and b>=a
True
a!=b or a==b
True
a>b or b>a
True
>>> not True
False
>>> not False
True
>>> #Membership
>>> #identify operators
>>> a=6
>>> if type(a) is int:
...     print("it is int")
... 
...     
it is int
>>> if type(a) is int:
...     print()
... 
...     

>>> 
>>> if type(a) is not int:
...     print("True")
... 
...     
>>> 
>>> #membership
...     
>>> a=2,3,4,5,6,7,8,9,10
>>> if 10 in a:
...     print(10)
... 
...     
10
>>> if 20 in a:
...     print(20)
... 
...     
>>> 
>>> if 20 not in a:
...     print(20)
... 
...     
20
