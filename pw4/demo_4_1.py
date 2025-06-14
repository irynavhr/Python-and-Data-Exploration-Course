Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = "zemene"
y = "dzervenes"
x[4]
'n'
y[3]
'r'
x[len(x)-3]
'e'
len(y)
9
x[1:4]
'eme'
x[3:99]
'ene'
x[876:7777]
''
x[7]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x[7]
IndexError: string index out of range
x[:]
'zemene'
x[-1]
'e'
x[-8]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x[-8]
IndexError: string index out of range
x[-3]
'e'
x[-4:]
'mene'

x[-44:]
'zemene'
x[-44:4]
'zeme'
x[44:-44]
''
y
'dzervenes'
"zer" in y
True
"a" in y
False
"dz" in x
False
"dz" not in x
True
x+y
'zemenedzervenes'
"zemene"==x
True
"Zemene"==x
False
"Zemene">x
False
"Zemene"<x
True
"abc"> "cda"
False
"z"
'z'
int('z')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int('z')
ValueError: invalid literal for int() with base 10: 'z'
x.upper()
'ZEMENE'
x
'zemene'
dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
x2 ="  bhb  nj  "
x2.strip()
'bhb  nj'
x2.strip(" ")
'bhb  nj'
x2.strip("  ")
'bhb  nj'
x.find("me")
2
x.replace("e", "ee")
'zeemeenee'
x.endwith("e")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    x.endwith("e")
AttributeError: 'str' object has no attribute 'endwith'. Did you mean: 'endswith'?
import re
rr = "X-Content-type-message-Body: text/plain"
rr
'X-Content-type-message-Body: text/plain'
re.search()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    re.search()
TypeError: search() missing 2 required positional arguments: 'pattern' and 'string'
x
'zemene'
x.split()
['zemene']
x.split("aa")
['zemene']
x.split("e")
['z', 'm', 'n', '']
