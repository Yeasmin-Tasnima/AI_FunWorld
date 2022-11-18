import time
import multiprocessing


def calc_square(numbers, result, value):
    value.value = 1.23
    print('Calculating squares:')
    for idx, n in enumerate(numbers):
        result[idx] = n * n
    print('result within process: {}'.format(result[:]))


if __name__ == '__main__':
    arr = [2, 3, 8, 9]

    start = time.time()
    result = multiprocessing.Array('i', 4)  # 'i' = data type(integer), 4 = data size
    value = multiprocessing.Value('d', 0.0)  # 'd' = data type(double), 0.0 = assigned value
    p1 = multiprocessing.Process(target=calc_square, args=(arr, result, value))
    p1.start()
    p1.join()
    end = time.time()

    print('result outside of process: {}'.format(result[:]))
    print('Multiprocessing return value: {}'.format(value.value))
    print('done in {} ms.'.format(str((end - start) * 1000)))
