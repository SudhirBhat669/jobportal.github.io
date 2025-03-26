from . import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    def get_id(self):
        return str(self.id) 

class Company(db.Model):
    __tablename__ = 'companies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    location = db.Column(db.String(100))
    website = db.Column(db.String(100))
    description = db.Column(db.Text)
    logo = db.Column(db.String(100))
    
    # Relationship to jobs (one-to-many)
    jobs = db.relationship('Job', back_populates='company')

class Job(db.Model):
    __tablename__ = 'jobs'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    posted_date = db.Column(db.String(20))
    location = db.Column(db.String(100))
    salary = db.Column(db.String(50))
    job_type = db.Column(db.String(50))
    shift = db.Column(db.String(50))
    description = db.Column(db.Text)
    requirements = db.Column(db.Text)
    qualifications = db.Column(db.Text)
    skills = db.Column(db.Text)
    description = db.Column(db.Text)
    openings = db.Column(db.Integer)
    posted_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image = db.Column(db.String(100))
    
    # Foreign key to company
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    
    # Relationship to company (many-to-one)
    company = db.relationship('Company', back_populates='jobs')

def initialize_database(app):
    """Initialize the database with sample data"""
    with app.app_context():
        # Create tables
        db.drop_all()
        db.create_all()
        
        # Add sample data if tables are empty
        if not Company.query.first():
            company = Company(
                name="IT Infosys Co",
                location="Mumbai, India",
                website="https://itinfosys.com",
                description="Leading IT services company...",
                logo="it-infosys-logo.png"
            )
            db.session.add(company)
            db.session.commit()

            job = Job(
            title="Senior Web Developer",
            company_id=1,
            location="Mumbai",
            salary="10k -25k",
            job_type="internship",
            shift="night Shift",
            posted_date=datetime(2023, 10, 1),  # Proper datetime object
            description="We are looking for an experienced web developer...",
            requirements="Graduate, 3+ years experience",
            qualifications="Bachelor's degree preferred",
            skills="HTML, CSS, JavaScript",
            image="html-5.png",
            openings=2
        )
        db.session.add(job)
        db.session.commit()

















































