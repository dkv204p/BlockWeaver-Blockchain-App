# BlockWeaver - Blockchain Explorer v1.1

BlockWeaver is a blockchain explorer built using Flask and PostgreSQL. This application allows users to submit transactions, mine new blocks, and view the blockchain in a user-friendly interface enhanced with Bootstrap.

## Features

- **Submit Transactions**: Users can input sender, recipient, and amount to create new transactions.
- **Mine New Blocks**: Users can mine new blocks that include pending transactions.
- **View Blockchain**: Users can view the entire blockchain, including details for each block.

## Technologies Used

- **Backend**: Python, Flask
- **Database**: PostgreSQL
- **Frontend**: HTML, Bootstrap

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- PostgreSQL

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dkv204p/BlockWeaver-Blockchain-App.git
   cd BlockWeaver-Blockchain-App
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .venv\Scripts\activate.ps1
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the database**:
   - Create a PostgreSQL database (e.g., `blockweaver_db`).
   - Run the following SQL to create the necessary table:
     ```sql
     CREATE TABLE blocks (
         id SERIAL PRIMARY KEY,
         timestamp TIMESTAMP WITHOUT TIME ZONE NOT NULL,
         proof INT NOT NULL,
         previous_hash TEXT NOT NULL
     );
     ```

6. **Configure the application**:
   - Update the `config.py` file with your database connection details:
     ```python
     SECRET_KEY = 'your_secret_key'

     DB_CONFIG = {
         'dbname': 'blockweaver_db',
         'user': 'your_username',
         'password': 'your_password',
         'host': 'localhost',
         'port': '5432',
     }
     ```

### Running the Application

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to `http://localhost:5000` to access the application.

## Usage

- **Submit Transaction**: Fill out the form with sender, recipient, and amount, then click "Submit Transaction."
- **Mine New Block**: Click the "Mine Block" button to mine a new block.
- **View Blockchain**: Click the "View Blockchain" button to see the entire blockchain.

## License

This project is licensed under the Creative Commons CC0 1.0 Universal license - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Bootstrap](https://getbootstrap.com/)
