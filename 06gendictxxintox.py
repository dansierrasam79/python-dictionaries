Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

======= RESTART: C:/Users/daniel/Desktop/python-dictionaries/06gendict.py ======
Traceback (most recent call last):
  File "C:/Users/daniel/Desktop/python-dictionaries/06gendict.py", line 3, in <module>
    init_dict = {x:x*x for i in range(0,5)}
NameError: name 'x' is not defined

======= RESTART: C:/Users/daniel/Desktop/python-dictionaries/06gendict.py ======
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

==== RESTART: C:/Users/daniel/Desktop/python-dictionaries/07dictofsquares.py ===
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
init_list = [n for n in range(1,11) if type(n/2) != type(1)]
print(init_list)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
init_list = [n for n in range(1,11) if type(n/2) != type(1.2)]
print(init_list)
[]

===== RESTART: C:/Users/daniel/Desktop/python-dictionaries/08mergedicts.py =====
Traceback (most recent call last):
  File "C:/Users/daniel/Desktop/python-dictionaries/08mergedicts.py", line 3, in <module>
    final_dict.copy(init_dict)
NameError: name 'final_dict' is not defined. Did you mean: 'init_dict'?

===== RESTART: C:/Users/daniel/Desktop/python-dictionaries/08mergedicts.py =====
Traceback (most recent call last):
  File "C:/Users/daniel/Desktop/python-dictionaries/08mergedicts.py", line 4, in <module>
    final_dict.copy(init_dict)
TypeError: dict.copy() takes no arguments (1 given)
>>> 
===== RESTART: C:/Users/daniel/Desktop/python-dictionaries/08mergedicts.py =====
>>> 
===== RESTART: C:/Users/daniel/Desktop/python-dictionaries/08mergedicts.py =====
{'a': 1, 'b': 2, 'c': 3}
>>> 
==== RESTART: C:/Users/daniel/Desktop/python-dictionaries/09iteratedicts.py ====
Traceback (most recent call last):
  File "C:/Users/daniel/Desktop/python-dictionaries/09iteratedicts.py", line 3, in <module>
    for key,value in init_dict:
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
==== RESTART: C:/Users/daniel/Desktop/python-dictionaries/09iteratedicts.py ====
a 1
b 2
c 3
d 4
e 5
>>> 
=== RESTART: C:/Users/daniel/Desktop/python-dictionaries/10sumitemsindict.py ===
55
>>> 
= RESTART: C:/Users/daniel/Desktop/python-dictionaries/11multiplyitemsindict.py
Traceback (most recent call last):
  File "C:/Users/daniel/Desktop/python-dictionaries/11multiplyitemsindict.py", line 6, in <module>
    for key,value in init_dict:
TypeError: cannot unpack non-iterable int object
>>> 
= RESTART: C:/Users/daniel/Desktop/python-dictionaries/11multiplyitemsindict.py
55 385
>>> 
== RESTART: C:/Users/daniel/Desktop/python-dictionaries/12removekeyfrmdict.py ==
{'b': 2, 'c': 3, 'd': 4, 'e': 5}
>>> aList = [1,2,3]
>>> bList = [4,5,6]
>>> final_list = zip(aList,bList)
