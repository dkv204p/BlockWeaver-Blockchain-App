from flask import Flask, jsonify, request, render_template # type: ignore
from blockchain import Blockchain

# Instantiate the Flask app
app = Flask(__name__)

# Create an instance of the Blockchain class
blockchain = Blockchain()

# Route for rendering the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to mine a new block
@app.route('/mine', methods=['GET'])
def mine_block():
    last_block = blockchain.get_last_block()
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # We reward the miner by adding a new transaction
    blockchain.add_transaction(sender="0", recipient="your_address", amount=1)

    block = blockchain.create_block(proof, blockchain.hash_block(last_block))
    response = {
        'message': 'New block has been mined',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200

# Route to add a new transaction
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # Required fields for a transaction
    required = ['sender', 'recipient', 'amount']
    if not all(field in values for field in required):
        return 'Missing fields', 400

    # Create a new transaction
    index = blockchain.add_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

# Route to return the full blockchain
@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
