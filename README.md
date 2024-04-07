# Hospital Management System

The Hospital Management System is a web-based application developed using Python, Flask, SQLite, and Bootstrap. It provides a user-friendly interface for managing doctors, appointments, and patient information in a hospital setting.

## Features

- Doctor Management:
  - Add new doctors with their name, specialty, contact number, and email
  - Edit and update doctor information
  - Delete doctors from the system

- Appointment Management:
  - Schedule new appointments by selecting a doctor, patient name, appointment date, and time slot
  - Edit and update existing appointments
  - Delete appointments from the system
  - View a list of all appointments with doctor and patient details
  - Dynamically update available time slots based on the selected doctor and date
  - Prevent scheduling appointments on previous dates

- Home Page:
  - Display statistics such as the total number of doctors and appointments
  - Show a table of today's appointments

## Technologies Used

- Python
- Flask (Web Framework)
- SQLite (Database)
- Bootstrap (Front-end CSS Framework)
- jQuery (JavaScript Library)

## Installation

1. Clone the repository:
git clone https://github.com/SilveryAngeleenavilasini/PythonCA_2.git

2. Change into the project directory:
cd PythonCA_2

3. Install the required dependencies:
pip install -r requirements.txt

4. Start the Flask development server:
python app.py

5. Open a web browser and navigate to http://localhost:5000 to access the application.

## Project Structure

hospital-management-system/
    ├── static/
    │   ├── css/
    │   │   └── bootstrap.min.css
    ├── templates/
    │   ├── base.html
    │   ├── home.html
    │   ├── doctors.html
    │   ├── add_doctor.html
    │   ├── edit_doctor.html
    │   ├── appointments.html
    │   ├── add_appointment.html
    │   └── edit_appointment.html
    |   └── today_appointments.html
    ├── app.py
    ├── database.py
    ├── requirements.txt
    └── README.md

