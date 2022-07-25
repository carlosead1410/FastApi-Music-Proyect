from sqlalchemy import Boolean, Column, DateTime, Integer, String 
from sqlalchemy.orm import relationship
from config_db import Base

class Artists(Base):
    __tablename__ = 'Artists'
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)
    Albums = relationship('Albums', back_populates='Artist', lazy='joined')