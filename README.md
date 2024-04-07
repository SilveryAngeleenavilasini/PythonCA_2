# Hospital Management System

The Hospital Management System is a web-based application developed using Python, Flask, SQLite, and Bootstrap. It provides a user-friendly interface for managing doctors, appointments, and patient information in a hospital setting.

## Contributor 

| Name      | Student ID  |
| ----------- | ----------- |
| Silvery Angeleena Vilasini   | 20000282       |

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

- The `static` directory contains the static assets such as CSS and JavaScript files.
- The `templates` directory contains the HTML templates used for rendering the web pages.
- `app.py` is the main Flask application file that defines the routes and handles the logic.
- `database.py` contains the database connection and query functions.
- `setup_database.py` is a script to set up the initial database tables.
- `requirements.txt` lists the required Python dependencies.
- `README.md` provides information about the project.

## Database Schema

The application uses an SQLite database to store information about doctors and appointments. The database schema consists of two tables:

### Doctors Table

| Column         | Type    | Description                 |
|----------------|---------|----------------------------|
| id             | INTEGER | Primary key (auto-increment) |
| name           | TEXT    | Name of the doctor           |
| specialty      | TEXT    | Specialty of the doctor      |
| contact_number | TEXT    | Contact number of the doctor |
| email          | TEXT    | Email address of the doctor  |

### Appointments Table

| Column           | Type    | Description                                         |
|------------------|---------|-----------------------------------------------------|
| id               | INTEGER | Primary key (auto-increment)                         |
| patient_name     | TEXT    | Name of the patient                                  |
| doctor_id        | INTEGER | Foreign key referencing the doctor's ID              |
| appointment_date | DATE    | Date of the appointment                              |
| time_slot        | TEXT    | Time slot of the appointment (e.g., "9:00 AM")       |

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
