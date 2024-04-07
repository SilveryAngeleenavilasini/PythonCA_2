from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from database import create_connection, create_tables
import json
from datetime import date

app = Flask(__name__)
Bootstrap(app)

# Home page route
@app.route('/')
def home():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM doctors")
    num_doctors = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM appointments")
    num_appointments = cursor.fetchone()[0]
    cursor.execute('''
        SELECT a.id, a.patient_name, d.name AS doctor_name, a.appointment_date, a.time_slot
        FROM appointments a
        JOIN doctors d ON a.doctor_id = d.id
        WHERE a.appointment_date = DATE('now')
    ''')
    todays_appointments = cursor.fetchall()
    conn.close()
    return render_template('home.html', num_doctors=num_doctors, num_appointments=num_appointments, todays_appointments=todays_appointments)

# Doctors page route
@app.route('/doctors')
def doctors():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    conn.close()
    return render_template('doctors.html', doctors=doctors)

# Appointments page route
@app.route('/appointments')
def appointments():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT a.id, a.patient_name, d.name, a.appointment_date, a.time_slot FROM appointments a JOIN doctors d ON a.doctor_id = d.id")
    appointments = cursor.fetchall()
    conn.close()
    return render_template('appointments.html', appointments=appointments)

# Add doctor route
@app.route('/add_doctor', methods=['GET', 'POST'])
def add_doctor():
    if request.method == 'POST':
        name = request.form['name']
        specialty = request.form['specialty']
        contact_number = request.form['contact_number']
        email = request.form['email']
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO doctors (name, specialty, contact_number, email) VALUES (?, ?, ?, ?)",
                       (name, specialty, contact_number, email))
        conn.commit()
        conn.close()
        return redirect(url_for('doctors'))
    return render_template('add_doctor.html')

# Add appointment route
@app.route('/add_appointment', methods=['GET', 'POST'])
def add_appointment():
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        doctor_id = request.form['doctor']
        appointment_date = request.form['appointment_date']
        time_slot = request.form['time_slot']
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO appointments (patient_name, doctor_id, appointment_date, time_slot) VALUES (?, ?, ?, ?)",
                       (patient_name, doctor_id, appointment_date, time_slot))
        conn.commit()
        conn.close()
        return redirect(url_for('appointments'))
    else:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM doctors")
        doctors = cursor.fetchall()
        time_slots = ['9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '4:00 PM']
        conn.close()
        today_date = date.today().strftime('%Y-%m-%d')
        return render_template('add_appointment.html', doctors=doctors, time_slots=json.dumps(time_slots), today_date=today_date)

@app.route('/get_available_time_slots', methods=['POST'])
def get_available_time_slots():
    doctor_id = request.form['doctor_id']
    appointment_date = request.form['appointment_date']
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT time_slot
        FROM appointments
        WHERE doctor_id = ? AND appointment_date = ?
    ''', (doctor_id, appointment_date))
    booked_slots = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify({'booked_slots': booked_slots})

@app.route('/edit_appointment/<int:appointment_id>', methods=['GET', 'POST'])
def edit_appointment(appointment_id):
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        doctor_id = request.form['doctor']
        appointment_date = request.form['appointment_date']
        time_slot = request.form['time_slot']
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE appointments
            SET patient_name = ?, doctor_id = ?, appointment_date = ?, time_slot = ?
            WHERE id = ?
        ''', (patient_name, doctor_id, appointment_date, time_slot, appointment_id))
        conn.commit()
        conn.close()
        return redirect(url_for('appointments'))
    else:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM appointments WHERE id = ?', (appointment_id,))
        appointment = cursor.fetchone()
        cursor.execute('SELECT id, name FROM doctors')
        doctors = cursor.fetchall()
        time_slots = ['9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '4:00 PM']
        conn.close()
        today_date = date.today().strftime('%Y-%m-%d')
        return render_template('edit_appointment.html', appointment=appointment, doctors=doctors, time_slots=json.dumps(time_slots), today_date=today_date)

@app.route('/delete_appointment/<int:appointment_id>')
def delete_appointment(appointment_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM appointments WHERE id = ?', (appointment_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('appointments'))

@app.route('/edit_doctor/<int:doctor_id>', methods=['GET', 'POST'])
def edit_doctor(doctor_id):
    if request.method == 'POST':
        name = request.form['name']
        specialty = request.form['specialty']
        contact_number = request.form['contact_number']
        email = request.form['email']
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE doctors
            SET name = ?, specialty = ?, contact_number = ?, email = ?
            WHERE id = ?
        ''', (name, specialty, contact_number, email, doctor_id))
        conn.commit()
        conn.close()
        return redirect(url_for('doctors'))
    else:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM doctors WHERE id = ?', (doctor_id,))
        doctor = cursor.fetchone()
        conn.close()
        return render_template('edit_doctor.html', doctor=doctor)

@app.route('/delete_doctor/<int:doctor_id>')
def delete_doctor(doctor_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM doctors WHERE id = ?', (doctor_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('doctors'))


if __name__ == '__main__':
    create_tables()
    app.run(debug=True)