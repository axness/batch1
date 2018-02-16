Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> type(100)
<type 'int'>
>>> type(20)
<type 'int'>
>>> bool(10)
True
>>> bool(0)
False
>>> bool(-10)
True
>>> float(10)
10.0
>>> str(10)
'10'
>>> type(10.5)
<type 'float'>
>>> int(10.5)
10
>>> int(10.8)
10
>>> int.__doc__
"int(x=0) -> int or long\nint(x, base=10) -> int or long\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is floating point, the conversion truncates towards zero.\nIf x is outside the integer range, the function returns a long instead.\n\nIf x is not a number or if base is given, then x must be a string or\nUnicode object representing an integer literal in the given base.  The\nliteral can be preceded by '+' or '-' and be surrounded by whitespace.\nThe base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to\ninterpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
>>> int('10', 8)
8
>>> int('10', 10)
10
>>> int('10',16)
16
>>> int(str(20), 16)
32
>>> int('A', 16)
10
>>> int('Z', 16)

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    int('Z', 16)
ValueError: invalid literal for int() with base 16: 'Z'
>>> int('10', 9)
9
>>> int('20', 2)

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int('20', 2)
ValueError: invalid literal for int() with base 2: '20'
>>> type(10.5)
<type 'float'>
>>> str(10.5)
'10.5'
>>> float(10.5)
10.5
>>> int('10.5')

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int('10.5')
ValueError: invalid literal for int() with base 10: '10.5'
>>> int(float('10.5'))
10
>>> int('20')
20
>>> int('20x')

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int('20x')
ValueError: invalid literal for int() with base 10: '20x'
>>> int('20A', 16)
522
>>> int('20A', 8)

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int('20A', 8)
ValueError: invalid literal for int() with base 8: '20A'
>>> int('20A', 12)
298
>>> a = "python"
>>> a
'python'
>>> a = 'don\'t'
>>> a
"don't"
>>> 5
5
>>> id(5)
33619616
>>> a = 5
>>> id(5)
33619616
>>> 5+2
7
>>> 
================== RESTART: D:/training/axness/batch/var.py ==================
5 (1, 2, 3.5, 'python') 10 10 10 20 30 40
>>> 
=============== RESTART: D:/training/axness/batch/arth_int.py ===============
2+3= 5
2-3= -1
2*3= 6
2/3= 0
2//3= 0
3%2= 1
3**2 9
>>> pow(3,2)\
	  
KeyboardInterrupt
>>> pow(3,2)
9
>>> -5 % 3
1
>>> 3/2
1
>>> 3//2
1
>>> 3.0/2
1.5
>>> 3.0//2
1.0
>>> 
=============== RESTART: D:/training/axness/batch/arth_int.py ===============
('2+3=', 5)
2-3= -1
2*3= 6
2/3= 0
2//3= 0
3%2= 1
3**2 9
>>> 
