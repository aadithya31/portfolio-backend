"""
Pydantic schemas for request/response validation.
"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CounterBase(BaseModel):
    """Base counter schema."""
    name: str = "main"
    count: int = 0


class CounterCreate(CounterBase):
    """Schema for creating a counter."""
    pass


class CounterResponse(CounterBase):
    """Schema for counter response."""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class CounterUpdate(BaseModel):
    """Schema for incrementing counter."""
    increment: int = 1


class HealthResponse(BaseModel):
    """Schema for health check response."""
    status: str
    version: str
    database: str


class MessageResponse(BaseModel):
    """Generic message response."""
    message: str
