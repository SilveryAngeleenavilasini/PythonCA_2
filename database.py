import sqlite3

def create_connection():
    conn = sqlite3.connect('hospital.db')
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS doctors')
    cursor.execute('''
        CREATE TABLE doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            specialty TEXT,
            contact_number TEXT,
            email TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT,
            doctor_id INTEGER,
            appointment_date DATE,
            time_slot TEXT,
            FOREIGN KEY (doctor_id) REFERENCES doctors (id)
        )
    ''')
    conn.commit()
    conn.close()