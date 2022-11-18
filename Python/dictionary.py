Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dictionary = {"a": 10, "b": 20, "c": 30}
>>> dictionary
{'a': 10, 'b': 20, 'c': 30}
>>> dictionary["a"]
10
>>> dictionary["b"] = 50
>>> dictionary
{'a': 10, 'b': 50, 'c': 30}
>>> 
>>> 
>>> for key in dictionary:
	print("key: {}, value: {}".format(key, dictionary[key]))

	
key: a, value: 10
key: b, value: 50
key: c, value: 30
>>> 
>>> 
>>> for k, v in dictionary.items():
	print("key: {}, value: {}".format(k, v))

	
key: a, value: 10
key: b, value: 50
key: c, value: 30
>>> 
>>> 
>>> "a" in dictionary
True
>>> "e" in dictionary
False
>>> 
>>> 
>>> dictionary.clear()
>>> dictionary
{}
>>> 