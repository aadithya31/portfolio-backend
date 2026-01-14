"""
Portfolio Backend - FastAPI Application.

This is a FastAPI-based backend that replicates the functionality
of the React + Vite portfolio application frontend.
"""
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.database import engine, Base
from app.routes.counter import router as counter_router
from app.schemas import HealthResponse

# Load environment variables
load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

# Application metadata
APP_NAME = os.getenv("APP_NAME", "Portfolio Backend")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Initialize FastAPI app
app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="FastAPI backend replicating the React + Vite portfolio application",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), "..", "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Setup templates
templates_dir = os.path.join(os.path.dirname(__file__), "..", "templates")
templates = Jinja2Templates(directory=templates_dir) if os.path.exists(templates_dir) else None

# Include routers
app.include_router(counter_router)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serve the main HTML page.
    Replicates the React App component rendering.
    """
    if templates:
        return templates.TemplateResponse("index.html", {"request": request})
    return HTMLResponse(content="""
        <html>
            <head><title>Portfolio Backend</title></head>
            <body>
                <h1>Portfolio Backend API</h1>
                <p>Visit <a href="/docs">/docs</a> for API documentation.</p>
            </body>
        </html>
    """)


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint.
    Returns the status of the application and database connection.
    """
    try:
        # Test database connection
        from sqlalchemy import text
        from app.database import SessionLocal
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"
    
    return HealthResponse(
        status="healthy",
        version=APP_VERSION,
        database=db_status
    )


if __name__ == "__main__":
    import uvicorn
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app.main:app", host=host, port=port, reload=DEBUG)
