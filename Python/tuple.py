Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> point = (0, 1)
>>> point
(0, 1)
>>> point[0]
0
>>> point[1]
1
>>> point[0] = 3
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    point[0] = 3
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> some_important_topic = '''List: All values have similiar meaning (Homogeneous),
Example: every item is an expanse, every name is a name of a person.

Tuple: All values have different meaning (Heterogeneous).
Example: (x_coordinate, y_coordinate), (street, city, zip_code).'''
>>> some_important_topic
'List: All values have similiar meaning (Homogeneous),\nExample: every item is an expanse, every name is a name of a person.\n\nTuple: All values have different meaning (Heterogeneous).\nExample: (x_coordinate, y_coordinate), (street, city, zip_code).'
>>> print(some_important_topic)
List: All values have similiar meaning (Homogeneous),
Example: every item is an expanse, every name is a name of a person.

Tuple: All values have different meaning (Heterogeneous).
Example: (x_coordinate, y_coordinate), (street, city, zip_code).
>>> 