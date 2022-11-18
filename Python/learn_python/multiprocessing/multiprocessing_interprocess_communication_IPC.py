import time
import multiprocessing


result = []


def calc_square(numbers):
    print('Calculating squares:')
    for n in numbers:
        print('square of {}: {}'.format(n, n * n))
        result.append(n * n)
    print('result within process: {}'.format(result))


if __name__ == '__main__':
    arr = [2, 3, 8, 9]

    start = time.time()
    p1 = multiprocessing.Process(target=calc_square, args=(arr, ))
    p1.start()
    p1.join()
    end = time.time()

    print('result outside of process: {}'.format(result))
    print('done in {} ms.'.format(str((end - start) * 1000)))
