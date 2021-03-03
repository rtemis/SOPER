from semaforos import semaphore
import threading 

buf = ['a','b','c','d','e','f','g','h','i','j']
pantry = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
empty = semaphore(0)
mutex = semaphore(1)
pantryCount = 0

def producer():
    global buf 
    global pantryCount
    global pantry
    global empty
    global mutex

    count = 0
    while True:
        if count == 10:
            count = 0
        item = buf[count]
        count += 1
        mutex.down()
        if pantryCount == 30:
            pantryCount = 0
        pantry[pantryCount] = item
        print ('Made object: ' + pantry[pantryCount])
        pantryCount += 1
        print (pantry)
        print (pantryCount)
        mutex.up()
        empty.up()


def consumer():
    global buf 
    global pantryCount
    global pantry
    global empty
    global mutex
     
    while True:
        empty.down()
        mutex.down()
        item = pantry[pantryCount]
        print ('Ate object: ' + item)
        pantry[pantryCount] = 0
        if pantryCount == 0:
            pantryCount = 30
        pantryCount -= 1
        print (pantry)
        mutex.up()

def Launcher(threads,*funcs):
    for func in funcs:
        t = threading.Thread(target=func)
        threads.append(t)
    for thr in threads:
        thr.start()

threads = []
Launcher(threads, producer, consumer)
