import time


def calc_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('{} tooks {} ms.'.format(func.__name__, str((end - start) * 1000)))
        return result
    return wrapper


@calc_time
def calc_square(numbers):
    result = []
    for i in numbers:
        result.append(i * i)
    return result


@calc_time
def calc_cube(numbers):
    result = []
    for i in numbers:
        result.append(i * i * i)
    return result


numbers_list = range(0, 10000)
# print('Squares of numbers: {}'.format(calc_square(numbers_list)))
# print('Cubes of numbers: {}'.format(calc_cube(numbers_list)))

calc_square(numbers_list)
calc_cube(numbers_list)
