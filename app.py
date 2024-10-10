from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from blockchain import Blockchain
from config import SECRET_KEY, DB_CONFIG
import psycopg2

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Create an instance of the Blockchain class
blockchain = Blockchain()

# Route for rendering the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to submit a new transaction
@app.route('/transactions/new', methods=['GET', 'POST'])
def submit_transaction():
    if request.method == 'POST':
        values = request.form

        # Required fields for a transaction
        required = ['sender', 'recipient', 'amount']
        if not all(field in values for field in required):
            flash('Missing fields in the transaction form', 'danger')
            return redirect(url_for('submit_transaction'))

        # Create a new transaction
        index = blockchain.add_transaction(values['sender'], values['recipient'], float(values['amount']))
        flash(f'Transaction will be added to Block {index}', 'success')
        return redirect(url_for('submit_transaction'))

    return render_template('submit_transaction.html')

# Route to mine a new block
@app.route('/mine', methods=['GET'])
def mine_block():
    last_block = blockchain.get_last_block()
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # Reward the miner
    blockchain.add_transaction(sender="0", recipient="your_address", amount=1)

    block = blockchain.create_block(proof, blockchain.hash_block(last_block))
    flash('New block has been mined', 'success')
    return render_template('mine_block.html', block=block)

# Route to return the full blockchain
@app.route('/chain', methods=['GET'])
def full_chain():
    return render_template('view_blockchain.html', chain=blockchain.chain)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
