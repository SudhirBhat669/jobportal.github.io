Project Overview
This is a comprehensive job portal application built with Flask, SQLAlchemy, and Bootstrap. The application allows users to:

Browse job listings
View company profiles
Register and login to accounts
Search and filter jobs
View detailed job information

Features
User Authentication: Register, login, and logout functionality
Job Listings: Browse all available jobs with filtering options
Company Profiles: View detailed company information
Responsive Design: Works on desktop and mobile devices
Database Integration: SQLite database with SQLAlchemy ORM
Email Configuration: Ready for email functionality
API Endpoints: JSON endpoints for job data

Installation
Follow these steps to set up the project locally:
Clone the repository
git clone https://github.com/SudhirBhat669/jobportal.github.io.git
cd (job-portal)

Create a virtual environment
python -m venv venv
source venv/bin/activate  On Linux
On Windows use `venv\Scripts\activate`

Install dependencies
pip install -r requirements.txt
Database Setup
The application uses SQLite with SQLAlchemy. To initialize the database:
Run the application which will automatically create the database:
python run.py
Database will be created at instance/job_portal.db with sample data.

File Structure
job-portal/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── (various image files)
├── templates/
│   ├── index.html          # Home page
│   ├── about.html          # About page
│   ├── jobs.html           # All jobs listing
│   ├── contact.html        # Contact page
│   ├── login.html          # Login page
│   ├── register.html       # Registration page
│   ├── view_company.html   # Company details
│   └── view_job.html       # Job details
├── app/
│   ├── __init__.py         # Flask app initialization
│   ├── models.py           # Database models
│   └── routes.py           # Application routes
├── run.py                  # Application entry point
└── requirements.txt        # Dependencies
Usage
Start the development server:
python run.py
Access the application at http://localhost:port number

Default test users:
Email: test1@example.com, Password: password1
Email: test2@example.com, Password: password2

Configuration
Configure the application by modifying these settings in app/__init__.py:
SECRET_KEY: Change to a secure random key
SQLALCHEMY_DATABASE_URI: Database connection string
MAIL_* settings: Configure for your email provider

API Endpoints
The application provides these JSON endpoints:
GET /api/jobs: Returns all jobs
GET /api/job/<id>: Returns a specific job by ID

Templates
index.html
Home page with job categories and latest job listings
Navigation to all major sections

about.html
Information about the job portal
Testimonials from users

jobs.html
Complete job listings with filtering options
Search functionality

contact.html
Contact form with validation
Company contact information

login.html
User login form
Link to registration page

register.html
User registration form
Link to login page

view_company.html
Detailed company profile
List of jobs offered by the company

view_job.html
Complete job details
Application form

Dependencies
Flask
Flask-SQLAlchemy
Flask-Login
Flask-Mail
Flask-Migrate
Bootstrap 5
Font Awesome

This README provides comprehensive documentation for setting up, running, and understanding the Job Portal application. For additional questions, please open an issue in the repository.






















































