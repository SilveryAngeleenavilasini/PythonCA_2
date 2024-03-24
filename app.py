from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from services import get_statistics, get_today_appointments
from db import init_db, get_db
from datetime import date

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    # Logic to fetch and display data
    return render_template('home.html', appointments_count=10, doctors_count=5)

@app.route('/appointments')
def appointments():
    # Logic to fetch and display appointment data
    return render_template('appointments.html', appointments=[])

@app.route('/doctors')
def doctors():
    # Logic to fetch and display doctor data
    return render_template('doctors.html', doctors=[])

# Route to render today's appointments page
@app.route('/today_appointments', endpoint='render_today_appointments')
def render_today_appointments():
    # Get the current date in the format 'YYYY-MM-DD'
    current_date = date.today().isoformat()

    # Fetch today's appointments from the database
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM appointments WHERE appointment_date = ?", (current_date,))
    today_appointments_from_db = cursor.fetchall()
    
    return render_template('today_appointments.html', today_appointments_from_db=today_appointments_from_db)



# Other routes for CRUD operations, forms, etc.

@app.route('/add_appointment', methods=['POST'])
def add_appointment():
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        appointment_name = request.form['appointment_name']
        doctor_name = request.form['doctor_name']
        appointment_date = request.form['appointment_date']

        # Insert the new appointment into the database
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO appointments (patient_name, appointment_name, doctor_name, appointment_date) VALUES (?, ?, ?, ?)",
            (patient_name, appointment_name, doctor_name, appointment_date)
        )
        db.commit()

        # Redirect to the home page after adding the appointment
        return redirect(url_for('home'))


if __name__ == '__main__':
    init_db(app)
    app.run(debug=True)
