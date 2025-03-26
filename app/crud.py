from sqlalchemy.orm import Session
from app import models, schemas
from sqlalchemy import and_
from datetime import date


# Create a new job application
def create_job_application(db: Session, job_data: schemas.JobApplicationCreate):
    new_job = models.JobApplication(**job_data.dict())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job


# Get all job applications
def get_job_applications(db: Session):
    return db.query(models.JobApplication).all()


# Update a job application (full update using PUT)
def update_job_application(db: Session, job_id: int, job_data: schemas.JobApplicationCreate):
    job = db.query(models.JobApplication).filter(models.JobApplication.id == job_id).first()
    if job is None:
        return None
    for key, value in job_data.dict().items():
        setattr(job, key, value)
    db.commit()
    db.refresh(job)
    return job


# Delete a job application by ID
def delete_job_application(db: Session, job_id: int):
    job = db.query(models.JobApplication).filter(models.JobApplication.id == job_id).first()
    if job is None:
        return None
    db.delete(job)
    db.commit()
    return job


# Get a single job application by ID
def get_job_by_id(db: Session, job_id: int):
    return db.query(models.JobApplication).filter(models.JobApplication.id == job_id).first()


# Filter job applications by optional parameters
def filter_jobs(
    db: Session,
    company: str = None,
    status: str = None,
    start_date: date = None,
    end_date: date = None,
):
    query = db.query(models.JobApplication)

    if company:
        query = query.filter(models.JobApplication.company.ilike(f"%{company}%"))
    if status:
        query = query.filter(models.JobApplication.status == status)
    if start_date and end_date:
        query = query.filter(and_(
            models.JobApplication.application_date >= start_date,
            models.JobApplication.application_date <= end_date,
        ))

    return query.all()


# Partially update a job application (only provided fields)
def partial_update_job(db: Session, job_id: int, job_data: schemas.JobApplicationUpdate):
    job = db.query(models.JobApplication).filter(models.JobApplication.id == job_id).first()
    if job is None:
        return None

    for key, value in job_data.dict(exclude_unset=True).items():
        setattr(job, key, value)

    db.commit()
    db.refresh(job)
    return job
