from threading import Thread
from time import sleep, time
from multiprocessing import Process

def download(file_name):
    print('Downloading file...', file_name)
    sleep(0.5)
    print('Download complete')

if __name__ == '__main__':
    files = ['video.mp4', 'image.jpg', 'data.csv']

    start = time()
    for f in files:
        download(f)
    end = time()
    print(f"serial time - {end - start:.2f} seconds")

    print()
    print("==================================")
    print()

    threads = []
    for f in files:
        t = Thread(target=download, args=(f,))
        threads.append(t)

    start = time()
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end = time()

    print(f"parallel with threads time - {end - start:.2f} seconds")

    print()
    print("======================================")
    print()

    process = []
    for f in files:
        t = Process(target=download, args=(f,))
        process.append(t)

    start = time()
    for p in process:
        p.start()

    for p in process:
        p.join()

    end = time()

    print(f"parallel with process time - {end - start:.2f} seconds")