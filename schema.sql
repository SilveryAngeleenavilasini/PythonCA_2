-- schema.sql

-- Table for appointments
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT NOT NULL,
    appointment_name TEXT NOT NULL,
    doctor_name TEXT NOT NULL,
    appointment_date DATE NOT NULL
);

-- Table for doctors
CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_name TEXT NOT NULL,
    specialization TEXT NOT NULL
);
