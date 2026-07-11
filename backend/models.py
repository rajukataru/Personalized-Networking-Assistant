from sqlalchemy import Column, Integer, String, Text
from backend.database import Base


class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    event = Column(String)
    interests = Column(String)
    conversation = Column(Text)


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    conversation = Column(Text)
    feedback = Column(String)