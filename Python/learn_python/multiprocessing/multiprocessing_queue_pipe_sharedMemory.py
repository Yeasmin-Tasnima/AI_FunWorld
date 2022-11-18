import time
import multiprocessing


def calc_square(numbers, q):
    print('Calculating squares:')
    for n in numbers:
        q.put(n * n)


if __name__ == '__main__':
    arr = [2, 3, 8, 9]

    start = time.time()
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=calc_square, args=(arr, q))
    p1.start()
    p1.join()
    end = time.time()

    print('Multiprocessing Queue result:')
    while q.empty() is False:
        print(q.get())

    print('done in {} ms.'.format(str((end - start) * 1000)))
