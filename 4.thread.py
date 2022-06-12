'''
说明: 就是单纯的实现一下, 看是否按顺序打印
'''
from threading import Thread

from loguru import logger


def req_1(i):
    if i == 20:
        for i in range(100000000):
            i += 1
    logger.info(i)
    pass


def main():
    logger.remove(handler_id=None)
    logger.add('logs/thread.log', enqueue=True)

    tasks = [Thread(target=req_1, args=(i, )) for i in range(1, 100)]
    for i in tasks:
        i.start()
    for i in tasks:
        i.join()

    pass


if __name__ == '__main__':
    main()
