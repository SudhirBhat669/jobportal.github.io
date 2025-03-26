from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Job, Company
from . import db, mail, login_manager
from flask_mail import Message
from datetime import datetime
from flask import current_app
import json


main_routes = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Add this function to create test users and sample data
def add_test_data(app):
    """Initialize test users, companies and jobs"""
    with app.app_context():
        if not User.query.filter_by(email='test1@example.com').first():
            # Create test users
            user1 = User(username='testuser1', email='test1@example.com', password='password1')
            user2 = User(username='testuser2', email='test2@example.com', password='password2')
            db.session.add_all([user1, user2])
            
            # Create sample company if none exists
            if not Company.query.first():
                company = Company(name="IT Infosys Co.", location="Mumbai, India")
                db.session.add(company)
                
                # Create sample jobs
                jobs = [
                    Job(
                        title="Senior Web Developer",
                        company=company,
                        location="Mumbai",
                        salary="10000 - 25000 per month",
                        job_type="part-time",
                        schedule="day shift",
                        posted_date=datetime(2023, 10, 1),
                        description="We are looking for an experienced web developer...",
                        requirements=json.dumps({
                            "education": "graduate",
                            "age": "25+",
                            "languages": "hindi, english",
                            "experience": "3+ years"
                        }),
                        qualifications=json.dumps([
                            "Bachelor's (Preferred)",
                            "PHP: 1 year (Preferred)",
                            "Web design: 1 year (Preferred)"
                        ]),
                        skills=json.dumps(["HTML5", "CSS", "JavaScript", "React"]),
                        openings=2
                    ),
                    Job(
                        title="Junior Developer",
                        company=company,
                        location="Bangalore",
                        salary="5000 - 10000 per month",
                        job_type="full-time",
                        schedule="flexible",
                        posted_date=datetime.utcnow(),
                        description="Entry level developer position...",
                        requirements=json.dumps({
                            "education": "diploma",
                            "age": "20+",
                            "languages": "english",
                            "experience": "0-1 years"
                        }),
                        qualifications=json.dumps([
                            "Diploma in Computer Science",
                            "Basic programming knowledge"
                        ]),
                        skills=json.dumps(["Python", "Django", "SQL"]),
                        openings=5
                    )
                ]
                db.session.add_all(jobs)
                db.session.commit()

# Home Page
@main_routes.route('/')
def index():
    companies = Company.query.all()
    return render_template('index.html', companies=companies)

# About Page
@main_routes.route('/about')
def about():
    return render_template('about.html')

# Jobs Page
@main_routes.route('/jobs')
def jobs():
    jobs = Job.query.all()
    return render_template('jobs.html', jobs=jobs)

# Contact Page
@main_routes.route('/contact')
def contact():
    return render_template('contact.html')

# Login Page
@main_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pass')
        
        if not email or not password:
            flash('Email and password are required', 'error')
            return redirect(url_for('main.login'))
            
        user = User.query.filter_by(email=email).first()
        
        if user and user.password == password:  # In production, use password hashing
            login_user(user)
            flash('Logged in successfully!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.index'))
            
        flash('Invalid email or password', 'error')
        
    return render_template('login.html')

# Logout Route
@main_routes.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))

# Register Page
@main_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not all([username, email, password]):
            flash('All fields are required', 'error')
            return redirect(url_for('main.register'))
            
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('main.register'))
            
        new_user = User(username=username, email=email, password=password)  # Hash password in production
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('main.login'))
        
    return render_template('register.html')

# Company Page
@main_routes.route('/company/<int:company_id>')
def view_company(company_id):
    company = Company.query.get_or_404(company_id)
    jobs = Job.query.filter_by(company_id=company.id).all()
    return render_template('view_company.html', company=company, jobs=jobs)

# Job Details Page
@main_routes.route('/job/<int:job_id>')
def view_job(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('view_job.html',
                         job=job,
                         requirements=json.loads(job.requirements),
                         qualifications=json.loads(job.qualifications),
                         skills=json.loads(job.skills))

# Apply for Job
@main_routes.route('/job/<int:job_id>/apply', methods=['POST'])
@login_required
def apply_job(job_id):
    job = Job.query.get_or_404(job_id)
    try:
        msg = Message(
            subject=f"Application for {job.title}",
            recipients=[current_user.email],
            sender=current_app.config['MAIL_DEFAULT_SENDER']
        )
        msg.body = f"You have applied for {job.title} at {job.company.name}"
        mail.send(msg)
        flash(f'Application submitted for {job.title}', 'success')
    except Exception as e:
        flash(f'Failed to send application email: {str(e)}', 'error')
    return redirect(url_for('main.view_job', job_id=job.id))


# Save Job
@main_routes.route('/job/<int:job_id>/save', methods=['POST'])
@login_required
def save_job(job_id):
    job = Job.query.get_or_404(job_id)
    flash(f'Job saved: {job.title}', 'success')
    return redirect(url_for('main.view_job', job_id=job.id))

# API Endpoints
@main_routes.route('/api/jobs', methods=['GET'])
def api_jobs():
    jobs = Job.query.all()
    return jsonify([{
        'id': job.id,
        'title': job.title,
        'company': job.company.name,
        'location': job.location,
        'salary': job.salary,
        'type': job.job_type
    } for job in jobs])

@main_routes.route('/api/job/<int:id>', methods=['GET'])
def api_job(id):
    job = Job.query.get_or_404(id)
    return jsonify({
        'id': job.id,
        'title': job.title,
        'company': job.company.name,
        'location': job.location,
        'salary': job.salary,
        'type': job.job_type,
        'description': job.description,
        'requirements': json.loads(job.requirements),
        'qualifications': json.loads(job.qualifications),
        'skills': json.loads(job.skills),
        'posted_date': job.posted_date.isoformat()
    })

