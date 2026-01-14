# Portfolio Backend

A FastAPI-based backend application that replicates the functionality of a React + Vite portfolio application.

## Features

- **FastAPI Framework**: Modern, fast Python web framework
- **PostgreSQL Database**: Persistent storage with SQLAlchemy ORM
- **Jinja2 Templates**: Server-side HTML rendering
- **Static Files**: CSS, JavaScript, and images served directly
- **Counter API**: RESTful API endpoints for counter functionality
- **Health Check**: Endpoint for monitoring application status

## Project Structure

```
portfolio-backend/
├── app/
│   ├── __init__.py
│   ├── database.py       # Database configuration
│   ├── main.py           # FastAPI application
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   └── routes/
│       ├── __init__.py
│       └── counter.py    # Counter API routes
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── images/
│   │   ├── react.svg
│   │   └── vite.svg
│   └── js/
│       └── app.js
├── templates/
│   └── index.html
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.9+
- PostgreSQL 12+
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aadithya31/portfolio-backend.git
   cd portfolio-backend
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL database**
   ```bash
   # Create database (run in psql)
   CREATE DATABASE portfolio_db;
   ```

5. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

## Running the Application

```bash
# Development mode with auto-reload
uvicorn app.main:app --reload --port 8000

# Production mode
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Main HTML page |
| GET | `/health` | Health check |
| GET | `/api/counter` | Get current counter value |
| POST | `/api/counter` | Increment counter |
| POST | `/api/counter/reset` | Reset counter to 0 |
| GET | `/docs` | Swagger API documentation |
| GET | `/redoc` | ReDoc API documentation |

## Testing with curl

```bash
# Get counter value
curl http://localhost:8000/api/counter

# Increment counter
curl -X POST http://localhost:8000/api/counter

# Reset counter
curl -X POST http://localhost:8000/api/counter/reset

# Health check
curl http://localhost:8000/health
```

## License

MIT
