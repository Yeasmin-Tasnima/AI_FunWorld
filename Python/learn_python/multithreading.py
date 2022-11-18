import time
import threading


def calc_square(numbers):
    print('Calculating squares:')
    for n in numbers:
        time.sleep(0.2)
        print('square of {}: {}\n'.format(n, n * n))


def calc_cubes(numbers):
    print('Calculating cubes:')
    for n in numbers:
        time.sleep(0.2)
        print('cube of {}: {}\n'.format(n, n * n * n))


arr = [2, 3, 8, 9]

start = time.time()

t1 = threading.Thread(target=calc_square, args=(arr, ))
t2 = threading.Thread(target=calc_cubes, args=(arr, ))

t1.start()
t2.start()

t1.join()
t2.join()

# calc_square(arr)
# calc_cubes(arr)

end = time.time()
print('done in {} ms.'.format(str((end - start) * 1000)))
