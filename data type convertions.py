Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#data type conversations
#integer
a=9
type(a)
<class 'int'>
int(9)
9
float(8.9)
8.9
str('nani')
'nani'
str(nani)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    str(nani)
NameError: name 'nani' is not defined
complex(8+9j)
(8+9j)
int(8.9)
8
int('nani')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    int('nani')
ValueError: invalid literal for int() with base 10: 'nani'
int(8+9j)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    int(8+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(8j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    int(8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(8j+9)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    int(8j+9)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(False)
0
int(True)
1
#float
float(8)
8.0
float(8.9)
8.9
float(88766.8763)
88766.8763
float('anilkumar')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    float('anilkumar')
ValueError: could not convert string to float: 'anilkumar'
float(9=5j)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
float(7+8j)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(7+8j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#string (str)
str(9)
'9'
>>> str(9.8)
'9.8'
>>> str('venkata ramana')
'venkata ramana'
>>> str(9+6j)
'(9+6j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(9)
(9+0j)
>>> complex(9.8)
(9.8+0j)
>>> complex('answer')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    complex('answer')
ValueError: complex() arg is a malformed string
>>> complex(9+5j)
(9+5j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> complex(8j)
8j
>>> #bool
>>> bool(5)
True
>>> bool(5.7)
True
>>> bool('name')
True
>>> bool(8+2j)
True
>>> bool(8j)
True
>>> bool(True)
True
>>> bool(false)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    bool(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
