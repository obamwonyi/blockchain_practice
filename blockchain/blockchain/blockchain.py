import json
import random
import datetime
from hashlib import sha256


class Blockchain(object):
    """
    This class represent the blockchain
    """
    def __init__(self) -> None:
        """
        Initialize properties and create the genesis
        block for the blockchain
        """
        self.chain = []
        self.pending_transactions = []

        # print message and create the genesis block.
        print("Creating genesis block")
        self.new_block()

    def new_block(self, previous_hash=None):
        """
        Generates a new block and adds it to the chain
        """
        block = {
            "index": len(self.chain),
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "transactions": self.pending_transactions,
            "previous_hash": self.last_block["hash"] if self.last_block else None,
            "nonce" : format(random.getrandbits(64), "x"),
        }

        # Get the hash of this new block, and add it to the block
        block_hash = self.hash(block)
        block["hash"] = block_hash

        # Reset the list of pending transactions
        self.pending_transactions = []

        return block
    
    @staticmethod
    def hash(block):
        """
        Hashes a block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        return the last block on the chain(if there are blocks)
        """
        # return self.chain[-1] if self.chain else None
        if (self.chain):
            return self.chain[-1]
        return None
    def new_transaction(self, sender, recipient, amount):
        """
        Adds a new transaction to the list of pending transactions
        """
        self.pending_transactions.append(
            {
                "recipient" : recipient,
                "sender" : sender,
                "amount" : amount
            }
        )

    def proof_of_work(self):
        """
        Checks for the proof of work
        """
        while True:
            new_block = self.new_block()
            if self.valid_block(new_block):
                break
        self.chain.append(new_block)
        print("Found a new block: ", new_block)

    @staticmethod
    def valid_block(block):
        """
        Checks if a block's hash starts with 0000
        """
        return block["hash"].startswith("0000")
    
    