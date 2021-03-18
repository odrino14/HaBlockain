import threading
import time
import random


class TestThread(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(TestThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # The flag used to pause the thread
        self.__flag.set()  # Set to True
        self.__running = threading.Event()  # Used to stop the thread identification
        self.__running.set()  # Set running to True
        self.__paused = False

    def run(self):
        while self.__running.isSet():
            print(f"Working..{self.name}")
            time.sleep(random.randint(3, 10))

    def isRunning(self):
        return self.__running.isSet()

    def isPaused(self):
        self.__paused

    def pause(self):
        self.__flag.clear()  # Set to False to block the thread
        self.__paused = True
        print(f"Paused..{self.name}")

    def resume(self):
        self.__flag.set()  # Set to True, let the thread stop blocking
        print(f"Resumed..{self.name}")
        self.__paused = False

    def stop(self):
        self.__flag.set()  # Resume the thread from the suspended state, if it is already suspended
        self.__running.clear()  # Set to False
        print(f"Stopped..{self.name}")


if __name__ == '__main__':
    thr1 = TestThread(name="Test1")
    thr2 = TestThread(name="Test2")
    thr1.start()
    thr2.start()
    for i in range(1000):
        paused1 = random.randint(0, 1)
        paused2 = random.randint(0, 1)
        if thr1.isRunning():
            if paused1 and not thr1.isPaused():
                thr1.pause()
            else:
                thr1.resume()
        if i < 100:
            if thr2.isRunning():
                if paused2 and not thr2.isPaused():
                    thr2.pause()
                else:
                    thr2.resume()
        elif i < 150:
            if thr2.isRunning():
                thr2.stop()
        else:
            if not thr2.isRunning():
                thr2.start()
