from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
from typing import Optional
from datetime import date

router = APIRouter()


# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create a new job application
@router.post("/jobs/", response_model=schemas.JobApplication)
def created_job(job: schemas.JobApplicationCreate, db: Session = Depends(get_db)):
    return crud.create_job_application(db=db, job_data=job)


# Get all job applications
@router.get("/jobs/", response_model=list[schemas.JobApplication])
def read_jobs(db: Session = Depends(get_db)):
    return crud.get_job_applications(db=db)


# Fully update a job application
@router.put("/jobs/{job_id}", response_model=schemas.JobApplication)
def update_job(job_id: int, job: schemas.JobApplicationCreate, db: Session = Depends(get_db)):
    updated_job = crud.update_job_application(db, job_id, job)
    if updated_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return updated_job


# Delete a job application
@router.delete("/jobs/{job_id}", response_model=schemas.JobApplication)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    deleted_job = crud.delete_job_application(db, job_id)
    if deleted_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return deleted_job


# Get a single job application by ID
@router.get("/jobs/{job_id}", response_model=schemas.JobApplication)
def read_job(job_id: int, db: Session = Depends(get_db)):
    job = crud.get_job_by_id(db, job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found.")
    return job


# Filter job applications by company, status, and/or date range
@router.get("/jobs/search", response_model=list[schemas.JobApplication])
def search_jobs(
    company: Optional[str] = None,
    status: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    db: Session = Depends(get_db),
):
    return crud.filter_jobs(db, company, status, start_date, end_date)


# Partially update a job application (PATCH)
@router.patch("/jobs/{job_id}", response_model=schemas.JobApplication)
def patch_job(job_id: int, job: schemas.JobApplicationUpdate, db: Session = Depends(get_db)):
    updated = crud.partial_update_job(db, job_id, job)
    if updated is None:
        raise HTTPException(status_code=404, detail="Job not found.")
    return updated
