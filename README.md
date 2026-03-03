# Log Monitoring & Alerting Backend

A RESTful backend API built with **FastAPI, SQLAlchemy, and SQLite** to ingest, store, and monitor system logs with CRUD operations and filtering.

---

## 🚀 Features

✨ **Persistent Storage**  
Logs are stored in a SQLite database for persistence across server restarts.

✨ **Create & Retrieve Logs**  
Add logs with severity levels and retrieve all stored logs.

✨ **Automatic Timestamping & Unique IDs**  
Each log entry is assigned a UUID and automatically timestamped.

✨ **Filtering & Query Support**  
Supports querying logs and filtering by severity level.

✨ **Alert Rule Endpoint**  
Triggers an alert when ERROR logs exceed a defined threshold.

✨ **Modular Backend Architecture**  
Clean separation of concerns using models, schemas, and database modules.

---

## 📦 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| FastAPI | REST API Framework |
| SQLAlchemy | ORM for Database Operations |
| SQLite | Lightweight Relational Database |
| Pydantic | Data Validation |
| Uvicorn | ASGI Server |

---

## 📁 Project Structure


log-monitoring-backend/
├── app/
│ ├── main.py # API Routes
│ ├── database.py # Database configuration
│ ├── models.py # SQLAlchemy models
│ └── schemas.py # Pydantic schemas
├── requirements.txt
├── .gitignore
└── README.md


> Note: `logs.db` is intentionally excluded from version control.

---

## ⚙️ Setup Instructions (Run Locally)

1️⃣ Clone the repository:

```bash
git clone https://github.com/srujanaelicherla/log-monitoring-backend.git
cd log-monitoring-backend

2️⃣ Install dependencies:

pip install -r requirements.txt

3️⃣ Start the server:

uvicorn app.main:app --reload

4️⃣ Open API documentation:

http://127.0.0.1:8000/docs
🧪 Example API Usage
➕ Create a Log

POST /logs

{
  "level": "ERROR",
  "message": "Database connection failed"
}
📄 Get All Logs

GET /logs

Returns:

[
  {
    "id": "uuid-value",
    "level": "ERROR",
    "message": "Database connection failed",
    "timestamp": "2026-03-03T12:34:56"
  }
]
🚨 Check Alert Status

GET /alert

Response example:

{
  "alert": "Too many ERROR logs!"
}

or

{
  "alert": "System stable"
}
🧠 Concepts Demonstrated

REST API Design

CRUD Operations

Database Modeling

ORM Usage with SQLAlchemy

Data Validation with Pydantic

Dependency Injection in FastAPI

Modular Backend Architecture

Alert Logic & Query Filtering

UUID-based Unique Identification

Automatic Timestamping

📌 Learning Outcome

This project demonstrates practical backend engineering concepts including:

✔ Building scalable API endpoints
✔ Managing database sessions
✔ Designing persistent storage
✔ Implementing business logic rules
✔ Structuring production-style backend code

👩‍💻 Author

Srujana Elicherla
Computer Science & Engineering Student
GitHub: https://github.com/srujanaelicherla

LinkedIn: https://linkedin.com/in/srujanaelicherla


---
