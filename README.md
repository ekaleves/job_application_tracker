# 📌 Job Application Tracker API

A FastAPI-based backend for managing job applications — allowing you to create, update, delete, and search through your job entries with filters like company, status, or date range.

---

## ⚙️ Tech Stack

- Python 3.12  
- FastAPI  
- SQLAlchemy  
- PostgreSQL  
- Pydantic v2  
- Uvicorn  
- Tested using Swagger UI (`/docs`)

---

## 📝 Note on Dates

When sending dates (like `application_date` or search filters), use the **ISO format**:

`YYYY-MM-DD` → example: `2025-03-26`

This format is required for all requests.

---
