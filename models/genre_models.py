from sqlalchemy import Boolean, Column, DateTime, Integer, String 
from sqlalchemy.orm import relationship
from config_db import Base

class Genres(Base):
    __tablename__ = 'Genres'
    GenreId = Column(Integer, primary_key=True)
    Name = Column(String)
    Tracks = relationship('Tracks', back_populates='Genre', lazy='joined')