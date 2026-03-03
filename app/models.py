from sqlalchemy import Column, String, DateTime
from datetime import datetime
from app.database import Base

class LogDB(Base):
    __tablename__ = "logs"

    id = Column(String, primary_key=True)
    level = Column(String)
    message = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)