from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class TaskActivityLog(Base):
    __tablename__ = "task_activity_logs"

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    actor_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    action = Column(String(100), nullable=False)
    old_value = Column(String)
    new_value = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    task = relationship("Task")
    actor = relationship("User")
