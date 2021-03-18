import datetime
import json
import hashlib
from Transaction import *
import random


# Encode the Block
# JsonDump convert the dict Block into json format

class BlockEncoder(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, 'jsonDump'):
            return o.jsonDump()
        else:
            return json.JSONEncoder.default(self, o)


"""
create a Block for the Blocckain with parameter
index = index of the Block
timestamp = time the Block was Created
proof = proof calculation as integer
previous_hash = The hash of the previous Block to link the Block between each other
Transactions = a Liste of all transactions for a Block
"""


class Block:
    def __init__(self, index, timestamp, proof, previous_hash, transactions):
        self.Index = index
        self.Timestamp = timestamp
        self.Proof = proof
        self.Previous_hash = previous_hash
        self.Transactions = transactions

    # convert the block data into Json String data an return it
    def jsonDump(self):
        dumped = dict(Index=self.Index, Timestamp=self.Timestamp, Proof=self.Proof, Previous_hash=self.Previous_hash,
                      Transactions=self.Transactions)  # self.__dict__
        return dumped

    # print the Block and all his Transactions
    def __str__(self):
        transStr = ""
        for trans in self.Transactions:
            transStr += f"{trans}\n----\n"
        return f"***** Block {self.Index} **********\n\nTimestamp : {self.Timestamp}\nProof : {self.Proof}\nPreviousHash : {self.Previous_hash}\nTransations : {transStr}\n***** End Block {self.Index} **********"


# create the Blockchain
class Blockchain:
    def __init__(self):  # refer to the object that with create
        self.__MAX_TRANSACTIONS = 1  # Max of transactions before a Block is created
        self.chain = []  # List of Block
        self.transactions = []  # List of transactions
        self.create_block(proof=100, previous_hash='0')  # Genesis-block Chain Initialisation

    # create a Block
    # transactions.copy() give a copy of the transactions
    def create_block(self, proof, previous_hash=None):
        block = Block(len(self.chain) + 1, str(datetime.datetime.now()), proof,
                      previous_hash or self.hash(self.chain[-1]), self.transactions.copy())
        self.chain.append(block)  # add the Block to the chain
        return block

    # get the last block of the current chain
    def get_previous_block(self):
        return self.chain[-1]  # -1 get the last index

    # effectued Transactions
    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

        previous_block = None
        if len(self.get_previous_block().Transactions) < self.__MAX_TRANSACTIONS:
            previous_block = self.get_previous_block()
        else:
            previous_block = self.create_block(
                random.randint(1, 102))  # create the previous Block with a random Proof number

        previous_block.Transactions.append(transaction)
        return previous_block.Index + 1

    # hash funktion for to hash a block
    def hash(self, block):
        encoded_block = json.dumps(block.jsonDump(), cls=BlockEncoder).encode()
        return hashlib.sha256(encoded_block).hexdigest()
