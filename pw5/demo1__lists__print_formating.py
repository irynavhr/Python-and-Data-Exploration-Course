Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = [1, 2, 3, 4, 55, 66, 8]
x
[1, 2, 3, 4, 55, 66, 8]
x[2]
3
x[3:]
[4, 55, 66, 8]
x[-1]
8
y = "aven"
x[1] = "jjjjj"
x
[1, 'jjjjj', 3, 4, 55, 66, 8]
x2 = 22
x22 = x2
x2
22
x22 = 3
x22
3
x2
22
x
[1, 'jjjjj', 3, 4, 55, 66, 8]
x[1] = 234
x
[1, 234, 3, 4, 55, 66, 8]
y = x
y[0] =0
x
[0, 234, 3, 4, 55, 66, 8]
y
[0, 234, 3, 4, 55, 66, 8]
z = x.copy()
z[0] = 100
z
[100, 234, 3, 4, 55, 66, 8]
x
[0, 234, 3, 4, 55, 66, 8]
y
[0, 234, 3, 4, 55, 66, 8]
x + z
[0, 234, 3, 4, 55, 66, 8, 100, 234, 3, 4, 55, 66, 8]
x.append(88)
x
[0, 234, 3, 4, 55, 66, 8, 88]
x.count()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    x.count()
TypeError: list.count() takes exactly one argument (0 given)
x
[0, 234, 3, 4, 55, 66, 8, 88]
x.count(7)
0
x.append(0)
x.count(0)
2
2
2
>>> x.index(0)
0
>>> x.index(0, 2)
8
>>> 
>>> x
[0, 234, 3, 4, 55, 66, 8, 88, 0]
>>> x.pop()
0
>>> x
[0, 234, 3, 4, 55, 66, 8, 88]
>>> x.pop()
88
>>> x
[0, 234, 3, 4, 55, 66, 8]
>>> x.pop(0)
0
>>> x
[234, 3, 4, 55, 66, 8]
>>> x.remove()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    x.remove()
TypeError: list.remove() takes exactly one argument (0 given)
>>> x.remove(4)
>>> x
[234, 3, 55, 66, 8]
>>> x.reverse
<built-in method reverse of list object at 0x000002CE79904A40>
>>> x
[234, 3, 55, 66, 8]
>>> x.reverse()
>>> x
[8, 66, 55, 3, 234]
>>> x.sort()
>>> x
[3, 8, 55, 66, 234]
>>> 55 in x
True
>>> manuf = "Valmiera"
>>> berries = "zemenes"
>>> w = 400
>>> "++ {} {} {}".format("MANUFACTURER: ".ljust(18, "."), BERRIEAS: ".ljust(10, ".")", WEIGHT:")
...                      
SyntaxError: unterminated string literal (detected at line 1)
>>> "++ {} {} {}".format("MANUFACTURER: ".ljust(18, "."), BERRIEAS: ".ljust(10, ".")", WEIGHT:)
...                      
SyntaxError: invalid syntax
