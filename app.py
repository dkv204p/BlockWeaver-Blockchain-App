from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from blockchain import Blockchain
from config import SECRET_KEY
from models import User, create_user

app = Flask(__name__)
app.secret_key = SECRET_KEY
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Blockchain instance
blockchain = Blockchain()

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        try:
            create_user(username, password)
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception:
            flash('Username already exists. Please choose a different one.', 'danger')
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.authenticate(username, password)
        if user:
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

# Route to submit a new transaction
@app.route('/transactions/new', methods=['GET', 'POST'])
@login_required
def submit_transaction():
    if request.method == 'POST':
        values = request.form
        required = ['sender', 'recipient', 'amount']
        if not all(field in values for field in required):
            flash('Missing fields in the transaction form', 'danger')
            return redirect(url_for('submit_transaction'))
        index = blockchain.add_transaction(values['sender'], values['recipient'], float(values['amount']))
        flash(f'Transaction will be added to Block {index}', 'success')
        return redirect(url_for('submit_transaction'))
    return render_template('submit_transaction.html')

# Route to mine a new block
@app.route('/mine', methods=['GET'])
@login_required
def mine_block():
    last_block = blockchain.get_last_block()
    last_proof = last_block['proof'] if last_block else 1
    proof = blockchain.proof_of_work(last_proof)
    blockchain.add_transaction(sender="0", recipient=current_user.username, amount=1)
    block = blockchain.create_block(proof, blockchain.hash_block(last_block) if last_block else '0')
    flash('New block has been mined', 'success')
    return render_template('mine_block.html', block=block)

# Route to view the full blockchain
@app.route('/chain', methods=['GET'])
def full_chain():
    return render_template('view_blockchain.html', chain=blockchain.chain)

# ---------------------
# API Routes
# ---------------------

# API endpoint to retrieve the full blockchain
@app.route('/api/chain', methods=['GET'])
def api_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

# API endpoint to submit a new transaction
@app.route('/api/transactions/new', methods=['POST'])
@login_required
def api_new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return jsonify({'message': 'Missing values'}), 400

    index = blockchain.add_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

# API endpoint to mine a new block
@app.route('/api/mine', methods=['GET'])
@login_required
def api_mine_block():
    last_block = blockchain.get_last_block()
    last_proof = last_block['proof'] if last_block else 1
    proof = blockchain.proof_of_work(last_proof)

    blockchain.add_transaction(sender="0", recipient=current_user.username, amount=1)
    block = blockchain.create_block(proof, blockchain.hash_block(last_block) if last_block else '0')

    response = {
        'message': 'New Block Mined!',
        'block': block
    }
    return jsonify(response), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
