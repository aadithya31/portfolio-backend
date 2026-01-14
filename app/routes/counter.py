"""
API routes for counter functionality.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Counter
from app.schemas import CounterResponse, CounterUpdate

router = APIRouter(prefix="/api", tags=["counter"])


@router.get("/counter", response_model=CounterResponse)
async def get_counter(db: Session = Depends(get_db)):
    """
    Get the current counter value.
    Creates a default counter if none exists.
    """
    counter = db.query(Counter).filter(Counter.name == "main").first()
    if not counter:
        counter = Counter(name="main", count=0)
        db.add(counter)
        db.commit()
        db.refresh(counter)
    return counter


@router.post("/counter", response_model=CounterResponse)
async def increment_counter(
    update: CounterUpdate = CounterUpdate(),
    db: Session = Depends(get_db)
):
    """
    Increment the counter by a specified amount (default: 1).
    Replicates the React useState setCount behavior.
    """
    counter = db.query(Counter).filter(Counter.name == "main").first()
    if not counter:
        counter = Counter(name="main", count=0)
        db.add(counter)
        db.commit()
        db.refresh(counter)
    
    counter.count += update.increment
    db.commit()
    db.refresh(counter)
    return counter


@router.post("/counter/reset", response_model=CounterResponse)
async def reset_counter(db: Session = Depends(get_db)):
    """
    Reset the counter to 0.
    """
    counter = db.query(Counter).filter(Counter.name == "main").first()
    if not counter:
        counter = Counter(name="main", count=0)
        db.add(counter)
    else:
        counter.count = 0
    db.commit()
    db.refresh(counter)
    return counter
