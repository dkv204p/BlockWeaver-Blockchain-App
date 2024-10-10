import hashlib
import json
from time import time
import psycopg2
from config import DB_CONFIG

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.connection = psycopg2.connect(**DB_CONFIG)
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        cursor = self.connection.cursor()
        timestamp = time()
        cursor.execute(
            "INSERT INTO blocks (timestamp, proof, previous_hash) VALUES (to_timestamp(%s), %s, %s) RETURNING id",
            (timestamp, proof, previous_hash)
        )
        self.connection.commit()
        block_id = cursor.fetchone()[0]
        cursor.close()

        block = {
            'index': block_id,
            'timestamp': timestamp,
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, recipient, amount):
        self.pending_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.get_last_block()['index'] + 1

    def proof_of_work(self, last_proof):
        proof = 0
        while self.is_valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    def is_valid_proof(self, last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def hash_block(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self):
        previous_block = self.chain[0]
        block_index = 1

        while block_index < len(self.chain):
            block = self.chain[block_index]
            if block['previous_hash'] != self.hash_block(previous_block):
                return False
            if not self.is_valid_proof(previous_block['proof'], block['proof']):
                return False
            previous_block = block
            block_index += 1
        return True
