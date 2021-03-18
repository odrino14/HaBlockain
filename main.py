from Master import *
from Worker import *
import random
import sys
import time

"""
Main of the implementation 
execute the Implementation.
"""


# create a Transaction with parameter

def createTransaction():
    sender = input("Sender : ")
    receiver = input("Receiver: ")
    amount = int(input("Amount: "))
    return sender


if __name__ == '__main__':
    master = Master(name="Master")
    master.start()  # start the Master Thread
    senders_receivers = ["Marc", "Luc", "Antoine", "Mathieu", "Jean", "Patrick", "Stephane",
                         "Junior"]  # list of Person to execute Transactions request
    maxAmount = sys.maxsize  # initial Amount to the biggest interger in the system
    workers = []  # workers initialisations
    failedWorkers = []  # failed or malicious Workers
    workerNumber = 5  # numbers of Workers

    for i in range(1, workerNumber + 1):
        workers.append(StartWorker(name=f"Worker {i}"))
        master.addWorker(workers[i - 1])  # Present Workers to the Master

    for i in range(100):
        indexSender = random.randint(0, len(senders_receivers) - 1)  # set Senderindex
        indexReceiver = random.randint(0, len(senders_receivers) - 1)  # set Receiverindex
        while indexReceiver == indexSender:
            indexReceiver = random.randint(0, len(
                senders_receivers) - 1)  # give another index to Receiver if it is the same as Sender

        sender = senders_receivers[indexSender]
        receiver = senders_receivers[indexReceiver]
        amount = random.randint(0, maxAmount)  # give a random number as Amount

        master.add_transaction(sender, receiver, amount)  # add transactions

        failedWorkersIndexes = []  # initialise a Liste of failed Workers
        i = 0

        # add failed Workers into list
        for worker in workers:
            if worker.paused():
                failedWorkersIndexes.append(i)
            i = i + 1

        if len(failedWorkersIndexes) > 0:
            selectedIndex = random.randint(0, len(failedWorkersIndexes) - 1)  # give a new index to the failed Worker
            reparedWorkerIndex = failedWorkersIndexes[selectedIndex]

            workers[reparedWorkerIndex].resume()  # restart the failed Workers
        time.sleep(0.5)
        failedWorkerIndex = random.randint(0, workerNumber - 1)
        workers[failedWorkerIndex].pause()  # stop a Worker from Worker list
