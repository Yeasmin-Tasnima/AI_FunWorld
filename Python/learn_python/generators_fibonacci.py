def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
for itr in fib:
    if itr > 50:
        break
    print(itr)
    