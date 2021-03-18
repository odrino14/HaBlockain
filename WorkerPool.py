from Worker import *
from Master import *

"""
Pool of Workers
"""


class WorkerPool(Thread):
    def __init__(self, master: Master):
        super().__init__()
        self.__Workers = set()
        self.WorkOn = True
        self.Master = master

    def addWorker(self, worker: StartWorker):
        self.__Workers.add(worker)

    def run(self):
        while self.WorkOn:
            pass
