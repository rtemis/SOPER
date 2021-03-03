import threading 

class semaphore:
    sem = 0

    def __init__(self, value):
        self.sem = threading.Semaphore(value)

    def up(self):
        self.sem.release()

    def down(self):
        self.sem.acquire()
