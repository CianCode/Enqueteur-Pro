-- Create ENUM type for status
CREATE TYPE StatusType AS ENUM ('open', 'closed');

-- Table: TypeCrime
CREATE TABLE TypeCrime (
    id_crime SERIAL PRIMARY KEY,
    label TEXT UNIQUE
);

-- Table: TypeEvidence
CREATE TABLE TypeEvidence (
    id_type_evidence SERIAL PRIMARY KEY,
    label TEXT UNIQUE
);

-- Table: TypePersonne
CREATE TABLE TypePersonne (
    id SERIAL PRIMARY KEY,
    label TEXT UNIQUE
);

-- Table: Investigation
CREATE TABLE Investigation (
    id_investigation SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    type_crime INT REFERENCES TypeCrime(id_crime),
    status StatusType NOT NULL,
    date_open DATE,
    date_close DATE
);

-- Table: Evidence
CREATE TABLE Evidence (
    id_evidence SERIAL PRIMARY KEY,
    id_type_evidence INT REFERENCES TypeEvidence(id_type_evidence),
    description TEXT
);

-- Table: Person
CREATE TABLE Person (
    id_personne SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    description TEXT,
    alibi TEXT,
    type_personne INT REFERENCES TypePersonne(id)
);

-- Table: Report
CREATE TABLE Report (
    id_report SERIAL PRIMARY KEY,
    date_creation DATE,
    content TEXT,
    investigation_relation INT REFERENCES Investigation(id_investigation)
);
