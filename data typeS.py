Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#data types
#integers denoted with int
a=9
type(a)
<class 'int'>
b=24
type(b)
<class 'int'>
c=1234567
type(c)
<class 'int'>
#float(Decimals) denoted with "float"
x=2.9
type(x)
<class 'float'>
y=296544.97986
type(y)
<class 'float'>
print(y)
296544.97986
#sting denoted with "str"
d="anil"
type(d)
<class 'str'>
>>> f='talluri'
>>> type(f)
<class 'str'>
>>> #complex denoted with "complex"
>>> h=7+9j
>>> type(h)
<class 'complex'>
>>> i=7+j8
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    i=7+j8
NameError: name 'j8' is not defined
>>> i=7+8j
>>> type(i)
<class 'complex'>
>>> j=j+9
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    j=j+9
NameError: name 'j' is not defined
>>> j=9j+8
>>> type(j)
<class 'complex'>
>>> k=9j
>>> type(k)
<class 'complex'>
>>> #bool denoted with "bool"
>>> 
>>> a=9
>>> type(a)
<class 'int'>
>>> a=False
>>> Type(a)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    Type(a)
NameError: name 'Type' is not defined. Did you mean: 'type'?
>>> type(a)
<class 'bool'>
>>> b=false
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    b=false
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> b=False
>>> type(b)
<class 'bool'>
