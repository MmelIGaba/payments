CREATE TABLE School (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    bank_account VARCHAR(255) NOT NULL
);

CREATE TABLE Student (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    school_id INTEGER REFERENCES School(id)
);

CREATE TABLE Payment (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES Student(id),
    school_id INTEGER REFERENCES School(id),
    amount DECIMAL(10, 2) NOT NULL,
    knit_fee DECIMAL(10, 2) NOT NULL,
    school_amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) CHECK (status IN ('PENDING', 'SUCCESS', 'FAILED')) DEFAULT 'PENDING',
    reference VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);