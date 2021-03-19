import random
from threading import *
import time
from blockchain import *
from CustomThreads import SchedulableThread

"""
execute Transaction by Worker
Start and Stop Workers to Simulate High availability
"""


class StartWorker(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None):
        super(StartWorker, self).__init__()

        self.__paused = False
        self.__running = True
        self.target = target
        self.name = name
        self.__blockchain = Blockchain()
        return

    def isRunning(self):
        return self.__running

    def paused(self):
        return self.__paused

    def run(self):

        while self.__running:
            if self.__paused:
                continue
            if len(self.__blockchain.transactions) > 0:
                print(f"Worker : {self.name}\nActual Chain : \n")

            # print the block when Worker already get Transactions
            for block in self.__blockchain.chain:
                print(f"{self.name} ====> {block}\n")
            time.sleep(random.randint(1, 5))

    # print received transaction from the Blockchain
    def receiveTransaction(self, transaction: Transaction):
        self.__blockchain.add_transaction(transaction)
        print(f"New Transaction requirement received by {self.name}")

    # pause Workers to run
    def pause(self):
        self.__paused = True
        print(f"{self.name} ist ausgefallen.\n")

    # restart the stopping Workers to join the execution process
    def resume(self):
        self.__paused = False
        print(f"{self.name} ist nun wieder funktionsfähig\n")

    def stop(self):
        # self.__resumeFlag.set()
        self.__running = False
