# Knit Payment System

A minimal payment processing system that enables parents to pay school fees digitally. The system records transactions, ensures idempotency, and calculates fees and school amounts accurately.

## Setup Instructions

### Prerequisites

- Python 3.7+
- Node.js 14+
- PostgreSQL

### Backend Setup

1. **Clone the repository**:
   ```
   git clone https://github.com/MmelIGaba/payment.git
   cd payment
   ```

2. **Navigate to the backend directory**:
    ```
    cd backend
    ```
3. **Create a virtual environment and activate it**:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. **Install dependencies**:
    ```
    pip install -r requirements.txt
    ```
5. **Set up the PostgreSQL database:**:
- Install PostgreSQL and pgAdmin.
- Create a new database named knit.
- Run the SQL script to create tables:
    ```
    psql -U postgres -d knit -f sql/create_tables.sql
    ```
6. **Update the .env file**:
    ```
    DATABASE_URL=postgresql://postgres:mysecretpassword@localhost:5432/knit
    ```
7. **Run the backend server**:
    ```
    python -m uvicorn app.main:app --reload
    ```
### Frontend Setup

1. **Navigate to the frontend directory**:
    ```
    cd ../frontend
    ``
2. **Install dependencies**:
    ```
    npm install
    ```
3. **Update the .env file**:
    ```
    REACT_APP_API_URL=http://localhost:8000
    ```
4. **Run the frontend server**:
    ```
    npm start
    ```
### Assumptions Made
- The PostgreSQL database is running locally.
- The backend server is running on http://localhost:8000.
- The frontend server is running on http://localhost:3000.
- The DATABASE_URL in the .env file is correctly configured.

#### What I’d Improve with More Time
- Database Transactions: Implement database transactions to ensure atomicity.
- Logging: Add comprehensive logging for better monitoring and debugging.
- Validation: Use Pydantic for input validation to ensure data integrity.
- Unit Tests: Add more unit tests to cover edge cases and ensure robustness.
- FAILED Payment Scenario: Implement a scenario where a payment fails and handle it gracefully.
- Webhook Endpoint: Add an endpoint to update payment status via webhooks.
- Security: Implement authentication and authorization for the API.
- Deployment: Set up CI/CD pipelines for automated testing and deployment.
- Documentation: Improve documentation for better developer experience.
- Performance: Optimize database queries and API performance.






