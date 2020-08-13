Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a = 10
>>> a
10
>>> type(a)
<class 'int'>
>>> type(a) == int
True
>>> if type(a) == int:
	print("labi")
else:
	print("skaitlis")

	
labi
>>> a = 10
>>> if type(a) == int:
	print("labi")
else:
	print("skaitlis")

	
labi
>>> a =5.5
>>> if type(a) == int:
	print("labi")
else:
	print("skaitlis")

	
skaitlis
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("skaitlis")

	
arī labi
>>> print ("aaa bbb ccc")
aaa bbb ccc
>>> print("aaa\n bbbb\n ccc\n")
aaa
 bbbb
 ccc

>>> clear
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> 
>>> print(letter)
a
>>> len(fruit)
6
>>> last = fruit[length-1]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    last = fruit[length-1]
NameError: name 'length' is not defined
>>> lenght = len(fruit)
>>> last = fruit[length-1]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    last = fruit[length-1]
NameError: name 'length' is not defined
>>> length = len(fruit)
>>> last = fruit[length-1]
>>> print(last)
a
>>> fruit[1]+fruit[3]+fruit[5]
'aaa'
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
b
a
n
a
n
a
>>> for char in fruit:
	print(char)

	
b
a
n
a
n
a
>>> s = 'Monty Python'
>>> print(s[0:5])
Monty
>>> print(s[6:12])
Python
>>> fruit [:3]
'ban'
>>> fruit [3:]
'ana'
>>> fruit [3:3]
''
>>> greeting = 'Hello, World!'
>>> new_greeting = ""
>>> 
>>> new_greeting = 'J' + greeting[1:]
>>> print(new_greeting)
Jello, World!
>>> word = 'banana'
>>> count = 0
>>> for letter in word:
	if letter == 'a':
		count = count + 1
		print(count)

		
1
2
3
>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False
>>> if word == 'banana':
	print('All right, bannanas.')

	
All right, bannanas.
>>> if word < 'banana' :
	print('Your word,'+ word + '  comes before banana.')
elif word > 'banana':
	print('Your word, ' + word + ' comes after banana.')
else:
	print('All right, bananas.'°
	      
SyntaxError: invalid character in identifier
>>> if word < 'banana' :
	print('Your word,'+ word + '  comes before banana.')
elif word > 'banana':
	print('Your word, ' + word + ' comes after banana.')
else:
	print('All right, bananas.')

	      
All right, bananas.
>>> stuff = 'Hello world'
	      
>>> type(stuff)
	      
<class 'str'>
>>> dir(stuff)
	      
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(str.capitalize)
	      
Help on method_descriptor:

capitalize(...)
    S.capitalize() -> str
    
    Return a capitalized version of S, i.e. make the first character
    have upper case and the rest lower case.

>>> new_word = word.upper()
	      
>>> print(new_word)
	      
BANANA
>>> index = word.find('a'°
		      
SyntaxError: invalid character in identifier
>>> index = word.find('a')
		      
>>> print(index)
		      
1
>>> word.find('ņa'°
	      
SyntaxError: invalid character in identifier
>>> word.find('na')
	      
2
>>> word.find('na', 3)
	      
4
>>> line = ' Here we go '
	      
>>> line.strip()
	      
'Here we go'
>>> line.startswith('Here')
	      
False
>>> line.startswith(' Here')
	      
True
>>> line.lower()
	      
' here we go '
>>> for letter in word:
	if letter == 'a':
		count = count + 1
print(count)
	      
SyntaxError: invalid syntax
>>> for letter in word:
	if letter == 'a':
		count = count + 1
     print(count)
	      
SyntaxError: unindent does not match any outer indentation level
>>> for letter in word:
	if letter == 'a':
		count = count + 1
   print(count)
	      
SyntaxError: unindent does not match any outer indentation level
>>> data
	      
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    data
NameError: name 'data' is not defined
>>> camels = 42
	      
>>> '%d' % camels
	      
'42'
>>> 
