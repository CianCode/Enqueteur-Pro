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
    link_investigation INT REFERENCES Investigation(id_investigation),
    description TEXT
);

-- Table: Person
CREATE TABLE Person (
    id_personne SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    description TEXT,
    alibi TEXT,
    link_investigation INT REFERENCES Investigation(id_investigation),
    type_personne INT REFERENCES TypePersonne(id)
);

CREATE TABLE links_investigation_person (
    id_personne INT REFERENCES Person(id_personne),
    id_investigation INT REFERENCES Investigation(id_investigation)
);

-- Table: Report
CREATE TABLE Report (
    id_report SERIAL PRIMARY KEY,
    date_creation DATE,
    content TEXT,
    investigation_relation INT REFERENCES Investigation(id_investigation)
);

-- Inserting into TypeCrime
INSERT INTO TypeCrime (label) VALUES
('Theft'),
('Assault'),
('Burglary'),
('Murder');

-- Inserting into TypeEvidence
INSERT INTO TypeEvidence (label) VALUES
('Fingerprint'),
('DNA'),
('Weapon'),
('Footprint');

-- Inserting into TypePersonne
INSERT INTO TypePersonne (label) VALUES
('Suspect'),
('Witness'),
('Victim'),
('Investigator');

-- Inserting into Investigation
INSERT INTO Investigation (name, type_crime, status, date_open, date_close) VALUES
('Investigation into Theft at Store', 1, 'open', '2024-10-01', NULL),
('Assault Investigation at Park', 2, 'closed', '2024-08-15', '2024-10-10'),
('Burglary at 123 Elm Street', 3, 'open', '2024-09-05', NULL),
('Murder Investigation: John Doe', 4, 'closed', '2024-07-20', '2024-10-05');

-- Inserting into Evidence
INSERT INTO Evidence (id_type_evidence, link_investigation, description) VALUES
(1, 1, 'Fingerprint found on the window'),
(2, 2, 'DNA sample found at the crime scene'),
(3, 1, 'Knife with blood stains'),
(4, 3, 'Footprint matching size 10 shoe found near the house');

-- Inserting into Person
INSERT INTO Person (first_name, last_name, description, alibi, link_investigation, type_personne) VALUES
('John', 'Smith', 'A suspect in the theft case', 'Was at home during the incident', 1, 1),
('Jane', 'Doe', 'Witness to the assault', 'Saw the event but did not intervene', 2, 2),
('Mark', 'Taylor', 'Victim of the burglary', 'Home at the time of the break-in', 3, 3),
('Sarah', 'Connor', 'Lead Investigator', 'Working on case', 4, 4);

-- Inserting into Report
INSERT INTO Report (date_creation, content, investigation_relation) VALUES
('2024-10-02', 'Witness statement from Jane Doe describing the assault.', 2),
('2024-10-12', 'Fingerprint analysis report from the theft investigation.', 1),
('2024-09-20', 'Initial report on the burglary at Elm Street with evidence collected.', 3),
('2024-10-06', 'Summary of the investigation into the murder of John Doe, case closed.', 4);
