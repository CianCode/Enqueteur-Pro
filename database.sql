-- database.sql

-- 1. Create investigations table
CREATE TABLE IF NOT EXISTS investigations_test (
    id SERIAL PRIMARY KEY,
    case_number VARCHAR(50) UNIQUE NOT NULL,
    case_name VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Create evidence table
CREATE TABLE IF NOT EXISTS evidence (
    id SERIAL PRIMARY KEY,
    investigation_id INTEGER REFERENCES investigations(id) ON DELETE CASCADE,
    evidence_type VARCHAR(100) NOT NULL,
    description TEXT,
    date_collected TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    location VARCHAR(255)
);

-- 3. Create investigators table
CREATE TABLE IF NOT EXISTS investigators (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    role VARCHAR(50),
    phone_number VARCHAR(20),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Insert initial data
INSERT INTO investigations (case_number, case_name, description, status) VALUES
('INV-001', 'Missing Person', 'Investigation into a missing person case.', 'open'),
('INV-002', 'Bank Robbery', 'Investigation into a recent bank robbery.', 'open');

INSERT INTO investigators (first_name, last_name, role, phone_number, email) VALUES
('John', 'Doe', 'Lead', '555-1234', 'john.doe@example.com'),
('Jane', 'Smith', 'Support', '555-5678', 'jane.smith@example.com');
