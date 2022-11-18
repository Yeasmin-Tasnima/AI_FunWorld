import time
import multiprocessing


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


if __name__ == '__main__':
    arr = [2, 3, 8, 9]

    start = time.time()

    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cubes, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # calc_square(arr)
    # calc_cubes(arr)

    end = time.time()
    print('done in {} ms.'.format(str((end - start) * 1000)))
