Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "ice cream"
>>> text
'ice cream'
>>> text[0]
'i'
>>> text[0:3]
'ice'
>>> text[4:9]
'cream'
>>> text[4:]
'cream'
>>> text[:3]
'ice'
>>> text[0] = 'g'
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    text[0] = 'g'
TypeError: 'str' object does not support item assignment
>>> text = "hello"
>>> text
'hello'
>>> text = 'hello'
>>> text
'hello'
>>> text = 'let's play'
SyntaxError: invalid syntax
>>> text = "let's play"
>>> text
"let's play"
>>> text = 'hello "world"'
>>> text
'hello "world"'
>>> address = "dhaka
SyntaxError: EOL while scanning string literal
>>> address = '''dhaka,
Bangladesh.'''
>>> address
'dhaka,\nBangladesh.'
>>> print(address)
dhaka,
Bangladesh.
>>> 
>>> s1 = "Hello"
>>> s2 = "world"
>>> s = s1 + " " + s2
>>> s
'Hello world'
>>> 
>>> s1 = "Number # "
>>> num1 = 10
>>> s = s1 + num1
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s = s1 + num1
TypeError: can only concatenate str (not "int") to str
>>> s = s1 + str(num1)
>>> s
'Number # 10'
>>> 