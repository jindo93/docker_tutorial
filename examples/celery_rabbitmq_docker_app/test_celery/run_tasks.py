from .tasks import longtime_add
import time

if __name__ == '__main__':
    urls = ['https://www.naver.com', 'https://www.google.com', 'https://www.yahoo.com',
            'https://www.bc.edu', 'https://www.bloomberg.com', 'https://www.amazon.com']

    for url in urls:
        start = time.time()
        result = longtime_add.delay(url)
        end = time.time()
        print('It took: ', end-start, ' seconds')
        print('Task result: ', result.get())
