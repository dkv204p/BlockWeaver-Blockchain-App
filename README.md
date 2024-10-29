# BlockWeaver - Blockchain Explorer v1.2

BlockWeaver is a blockchain explorer built using Flask and PostgreSQL. The application allows users to submit transactions, mine new blocks, and view the blockchain in a user-friendly interface enhanced with Bootstrap. In version 1.2, we have introduced user authentication, improved data storage, and added a RESTful API for interacting with the blockchain programmatically.

## New Features in v1.2

- **User Authentication**: Users can register, log in, and log out. Only authenticated users can submit transactions and mine blocks.
- **Improved Data Storage**: Transactions are now stored in the database with each block, allowing for better data management and querying.
- **RESTful API**: Added endpoints for programmatic interaction with the blockchain.
- **Enhanced Frontend**: Improved form validation, authentication checks, and detailed transaction views for each block.
- **Docker Support**: Added Docker configuration for easy setup and deployment.

## Technologies Used

- **Backend**: Python, Flask
- **Database**: PostgreSQL
- **Frontend**: HTML, Bootstrap
- **Authentication**: Flask-Login, Flask-Bcrypt
- **Environment Management**: python-dotenv

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- PostgreSQL
- Docker (optional, for Docker setup)

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
   - Run the following SQL to create the necessary tables:
     ```sql
     CREATE TABLE blocks (
         id SERIAL PRIMARY KEY,
         timestamp TIMESTAMP WITHOUT TIME ZONE NOT NULL,
         proof INT NOT NULL,
         previous_hash TEXT NOT NULL
     );

     CREATE TABLE transactions (
         id SERIAL PRIMARY KEY,
         block_id INT REFERENCES blocks(id) ON DELETE CASCADE,
         sender TEXT NOT NULL,
         recipient TEXT NOT NULL,
         amount FLOAT NOT NULL
     );

     CREATE TABLE users (
         id SERIAL PRIMARY KEY,
         username TEXT UNIQUE NOT NULL,
         password_hash TEXT NOT NULL
     );
     ```

6. **Configure the application**:
   - Create a `.env` file based on the `.env.example` file and update it with your database connection details:
     ```plaintext
     SECRET_KEY=your_secret_key
     DB_NAME=blockweaver_db
     DB_USER=your_username
     DB_PASSWORD=your_password
     DB_HOST=localhost
     DB_PORT=5432
     ```

### Running the Application

1. **Start the Flask application**:
   ```bash
   python app.py
   ```

2. **Open your browser and navigate to `http://localhost:5000`** to access the application.

### Using Docker

1. **Build the Docker image**:
   ```bash
   docker build -t blockweaver .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -d -p 5000:5000 --env-file .env blockweaver
   ```

The application should now be accessible at `http://localhost:5000`.

## RESTful API Endpoints

- **GET /api/chain**: Retrieve the full blockchain.
- **POST /api/transactions/new**: Submit a new transaction. Requires a JSON payload with `sender`, `recipient`, and `amount`.
- **GET /api/mine**: Mine a new block. Authenticated users only.

## Usage

- **Register and Login**: Create an account or log in to submit transactions and mine blocks.
- **Submit Transaction**: Fill out the form with sender, recipient, and amount, then click "Submit Transaction."
- **Mine New Block**: Click the "Mine Block" button to mine a new block.
- **View Blockchain**: Click the "View Blockchain" button to see the entire blockchain.

## Running Tests

1. **Install testing dependencies** (if not already installed):
   ```bash
   pip install pytest
   ```

2. **Run the tests**:
   ```bash
   pytest
   ```

## Security Notes

- Ensure that the `.env` file is not committed to version control.
- Use a strong `SECRET_KEY` for the Flask app.

## License

This project is licensed under the Creative Commons CC0 1.0 Universal license - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
- [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)
- [Docker](https://www.docker.com/)
