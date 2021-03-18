from threading import Thread, Event


# create to restart a threads because it is not possible to start twice

class SchedulableThread(Thread):
    def __init__(self):
        self._startEvent = Event()
        self._runTerminated = Event()
        self._terminationRequired = False
        Thread.__init__(self)

    def restart(self):
        self._startEvent.set()

    def join(self):
        self._runTerminated.wait()
        self._runTerminated.clear()

    def terminate(self):
        self._terminationRequired = True
        self.restart()
        self.join()
