def process_file():
    try:
        f = open('json/book.txt')
        x = 1/0
    except FileNotFoundError as e:
        print('Exception type: {}'.format(type(e).__name__))
    except ZeroDivisionError as e:
        print('Exception type: {}'.format(type(e).__name__))
    finally:
        print('Cleaning up the files')
        f.close()


process_file()
