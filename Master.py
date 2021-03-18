import queue
from Worker import *
from Transaction import *

"""
create Thread for Master or Master thread
"""


class Master(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        super(Master, self).__init__()
        self.target = target
        self.name = name
        self.__WorkerPool = []  # list of all Worker, who are going to execute the Transactions and create the Block
        self.__WorkerPoolRunners = []  # List of Worker who are Running
        self.__TransactionQueue = queue.Queue()  # Put the Transactions to be execute by the Worker into a Queue

    def run(self):
        while True:
            if not self.__TransactionQueue.full():
                self.__WorkerPoolRunners = []
                for worker in self.__WorkerPool:

                    # Check if the Thread Worker is running from the WorkerPool
                    # fill it into the pool of running Workers

                    if worker.is_alive():
                        self.__WorkerPoolRunners.append(worker)
                workerLen = len(self.__WorkerPoolRunners)
                if workerLen > 0:
                    workerIndex = random.randint(0, workerLen - 1)  # Master give a Random index to workers
                    self.__WorkerPoolRunners[workerIndex]. \
                        receiveTransaction(
                        self.__TransactionQueue.get())  # Running Workers get Transactions from the Queue
        return

    # Create Transactions and fill it into TransactionQueue
    def add_transaction(self, sender, receiver, amount):
        self.__TransactionQueue.put(Transaction(sender, receiver, amount))

    # From the Class StartWorker start the Workers threads and put it into the WorkerPool
    def addWorker(self, worker: StartWorker):
        worker.start()
        self.__WorkerPool.append(worker)
