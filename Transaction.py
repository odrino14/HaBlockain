"""
set Transactions for the Block
"""


class Transaction:
    def __init__(self, sender, receiver, amount):
        self.Sender = sender
        self.Receiver = receiver
        self.Amount = amount

    def __str__(self):
        return f"Sender: {self.Sender}\nReceiver: {self.Receiver}\nAmount: {self.Amount}"  # format the parameter of Transactions

    def jsonDump(self):
        return dict(Sender=self.Sender, Receiver=self.Receiver, Amount=self.Amount)
