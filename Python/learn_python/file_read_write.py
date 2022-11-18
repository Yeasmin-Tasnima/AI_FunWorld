with open('json/book.txt', 'r') as f:
    for line in f:
        print(line)
print('*******************')

with open('json/book.txt', 'a') as f:
    f.write('\nI love python\n')

with open('json/book.txt', 'r') as f:
    txt = f.read()
    print(txt)
print('*******************')

with open('json/book.txt', 'r') as f:
    lines = f.read().split('\n')
    print(lines)