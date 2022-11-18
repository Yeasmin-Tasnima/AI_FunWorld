Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> items = ["bread", "pasta", "burger", "pizza"]
>>> items[1]
'pasta'
>>> items[0:2]
['bread', 'pasta']
>>> items[-1]
'pizza'
>>> items[0] = "choco"
>>> items
['choco', 'pasta', 'burger', 'pizza']
>>> 
>>> 
>>> items.append("butter")
>>> items
['choco', 'pasta', 'burger', 'pizza', 'butter']
>>> items.insert(0, "bread")
>>> items
['bread', 'choco', 'pasta', 'burger', 'pizza', 'butter']
>>> 
>>> 
>>> list1 = ["a", "b", "c"]
>>> list2 = ["d", "e"]
>>> sum_of_list = list1 + list2
>>> sum_of_list
['a', 'b', 'c', 'd', 'e']
>>> len(sum_of_list)
5
>>> 
>>> 
>>> "a" in sum_of_list
True
>>> "v" in sum_of_list
False
>>> 