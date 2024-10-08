# BlockWeaver - A Blockchain Flask App

**BlockWeaver** is a basic blockchain implementation built using Python and Flask. It allows users to perform the following actions:
- Submit new transactions
- Mine new blocks
- View the entire blockchain

## Features
- Basic blockchain functionality (Proof of Work, transaction management, and block mining)
- Flask-based API with web interface
- Simple HTML interface to interact with the blockchain

## Prerequisites
- Python 3.x
- Flask

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dkv204p/BlockWeaver.git
   cd BlockWeaver
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate.ps1     # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the app:**
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## API Endpoints

- **GET /chain**: Returns the entire blockchain.
- **POST /transactions/new**: Submits a new transaction.
- **GET /mine**: Mines a new block and adds it to the chain.

## Usage

- Navigate to `http://127.0.0.1:5000/` to access the web interface.
- Use the form to submit transactions and mine new blocks.
- View the blockchain by clicking "View Blockchain."

## License

This project is licensed under the **CC0 1.0 Universal**, allowing you to freely use, modify, and distribute this work without any restrictions; for full license details, refer to the [CC0 Legal Code](https://creativecommons.org/publicdomain/zero/1.0/legalcode).
