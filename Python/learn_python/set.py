# function call with set literal
ids = set([1, 2, 1, 3, 2, 4, 5])
print(ids)

# general format
ids = {1, 2, 1, 3, 2, 4, 5}
print(ids)

# frozen set
lst = [1, 2]
fs = frozenset(lst)
# couldn't add elements to a frozenset
print(fs)

# mathematical equations
x = {1, 2, 3}
y = {3, 4}

print('Union, x | y: {}'.format(x | y))
print('Intersection, x & y: {}'.format(x & y))
print('Subtraction, x - y: {}'.format(x - y))
