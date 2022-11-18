x = input("Enter first number: ")
y = input("Enter second number: ")

try:
    z = x / int(y)
except ZeroDivisionError as e:
    print('Zero Division Error')
    z = None
except Exception as e:
    print('Exception type: {}'.format(type(e).__name__))
    z = None

print('Division is: {}'.format(z))