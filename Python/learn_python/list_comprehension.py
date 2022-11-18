numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [i for i in numbers if i % 2 == 0]
odd = [i for i in numbers if i % 2 != 0]

print('List of Even numbers: {}'.format(even))
print('List of odd numbers: {}'.format(odd))
