"""
SQLAlchemy models for the portfolio application.
"""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base


class Counter(Base):
    """
    Counter model to store the click count.
    Replicates the useState counter from the React application.
    """
    __tablename__ = "counters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, default="main")
    count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Counter(name='{self.name}', count={self.count})>"


class PageVisit(Base):
    """
    Track page visits for analytics.
    """
    __tablename__ = "page_visits"

    id = Column(Integer, primary_key=True, index=True)
    page = Column(String(255), nullable=False)
    visitor_ip = Column(String(45), nullable=True)  # IPv6 compatible
    user_agent = Column(String(500), nullable=True)
    visited_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<PageVisit(page='{self.page}', visited_at={self.visited_at})>"
