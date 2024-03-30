# app/services.py

import sqlite3
from datetime import datetime

DB_NAME = 'hospital.db'

def get_statistics():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM appointments')
        appointments_count = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM doctors')
        doctors_count = cursor.fetchone()[0]

    return appointments_count, doctors_count

def get_today_appointments():
    today_date = datetime.now().date().strftime('%Y-%m-%d')

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM appointments WHERE DATE(appointment_date) = ?', (today_date,))
        today_appointments = cursor.fetchall()

    return today_appointments