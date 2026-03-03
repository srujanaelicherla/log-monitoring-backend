# Log Monitoring & Alerting Backend

A RESTful backend system built using FastAPI, SQLAlchemy, and SQLite to ingest, persist, and monitor system logs.

## Features

- Create logs via POST endpoint
- Retrieve logs via GET endpoint
- Persistent storage using SQLite
- Unique ID generation for each log
- Automatic timestamp recording
- Alert endpoint that triggers when ERROR logs exceed threshold
- Modular project architecture

## Tech Stack

- Python
- FastAPI
- SQLAlchemy (ORM)
- SQLite
- Pydantic

## Run Locally

1. Clone repository
2. Install dependencies:

pip install -r requirements.txt

3. Run server:

uvicorn app.main:app --reload

4. Visit:

http://127.0.0.1:8000/docs

## Architecture

- app/database.py → DB connection
- app/models.py → Database models
- app/schemas.py → Pydantic schemas
- app/main.py → API routes
