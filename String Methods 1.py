Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = "Python"
>>> x.startswith("P")
True
>>> x.startswith("X")
False
>>> x.endswith("X")
False
>>> # String Slicing
>>> x[0:5]
'Pytho'
>>> x = "Hello World"
>>> x[0:5]
'Hello'
>>> x[0:5:1]
'Hello'
>>> x[0:5:2]
'Hlo'
>>> x
'Hello World'
>>> x[::-1]
'dlroW olleH'
>>> x
'Hello World'
>>> x.split()
['Hello', 'World']
>>> x.split()[0]
'Hello'
>>> x.split()[1]
'World'
>>> x = ["hello", "students", "how", "are", "you"]
>>> x
['hello', 'students', 'how', 'are', 'you']
>>> " ".join(x)
'hello students how are you'
>>> "$".join(x)
'hello$students$how$are$you'
>>> x
['hello', 'students', 'how', 'are', 'you']
>>> x = "hello"
>>> x.count("l")
2
>>> x = "hello"
>>> x.isalpha()
True
>>> x = "fsdfsde23ew4"
>>> x.isalnum()
True
>>> x = "HEY"
>>> x.islower()
False
>>> x.isupper()
True
>>> x = "Python"
>>> len(x)
6
>>> x.center(7)
' Python'
>>> x.center(20)
'       Python       '
>>> x.center(21)
'        Python       '
>>> x.center(21, "*")
'********Python*******'
