import time
from multiprocessing import Pool


def func(n):
    return n * n


if __name__ == '__main__':
    arr = range(100000000)

    t1 = time.time()
    p = Pool()
    pool_result = p.map(func, arr)
    p.close()
    p.join()
    # print('Pool process -> result: {}, time: {}'.format(pool_result, time.time() - t1))
    print('Pool process -> time: {}'.format(time.time() - t1))

    t2 = time.time()
    serial_result = []
    for num in arr:
        serial_result.append(func(num))
    # print('Serial process -> result: {}, time: {}'.format(serial_result, time.time() - t2))
    print('Serial process -> time: {}'.format(time.time() - t2))
