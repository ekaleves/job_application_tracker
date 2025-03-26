from pydantic import BaseModel
from datetime import date
from typing import Optional


# Shared fields used across multiple schemas
class JobApplicationBase(BaseModel):
    job_title: str
    company: str
    application_date: Optional[date] = None
    status: Optional[str] = "applied"
    contact_person: Optional[str] = None
    notes: Optional[str] = None


# Schema for creating a new job application
class JobApplicationCreate(JobApplicationBase):
    pass


# Schema for reading a job application, including its ID
class JobApplication(JobApplicationBase):
    id: int

    class Config:
        from_attributes = True  # Allow loading data from ORM models


# Schema for updating only the provided fields (partial update)
class JobApplicationUpdate(BaseModel):
    job_title: Optional[str] = None
    company: Optional[str] = None
    application_date: Optional[date] = None
    status: Optional[str] = None
    contact_person: Optional[str] = None
    notes: Optional[str] = None
