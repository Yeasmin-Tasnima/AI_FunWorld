import json

book = {}

book['tom'] = {
    'address': 'dhaka',
    'phone': 1234
}

book['bob'] = {
    'address': 'dinajpur',
    'phone': 5678
}

s = json.dumps(book)

# writing
with open('book.txt', 'w') as f:
    f.write(s)

# read json file as a string
f = open('book.txt', 'r')
book = f.read()
print(type(book))
print(book)

# read json file as a dictionary
book = json.loads(book)
print(type(book))
print(book)
