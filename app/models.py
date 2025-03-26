from sqlalchemy import Column, Integer, String, Date, Text
from app.database import Base


# JobApplication model representing the 'job_applications' table in the database
class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    application_date = Column(Date)
    status = Column(String, default="applied")
    contact_person = Column(String, nullable=True)
    notes = Column(Text, nullable=True)
