from threading import Thread
from time import sleep

def hello():
    for i in range(5):
        print("Hello ->", i+1)
        sleep(0.3)


def hi():
    for i in range(5):
        print("Hi ->", i+1)
        sleep(0.3)

if __name__ == '__main__':
    t1 = Thread(target=hello)
    t2 = Thread(target=hi)

    t1.start()
    t2.start()

    t1.join() # this means we're saying that first complete that
    t2.join()

    print("BYE")