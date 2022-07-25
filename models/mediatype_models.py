from sqlalchemy import Boolean, Column, DateTime, Integer, String 
from sqlalchemy.orm import relationship
from config_db import Base

class MediaTypes(Base):
    __tablename__ = 'media_types'
    MediaTypeId = Column(Integer, primary_key=True)
    Name = Column(String)
    Tracks = relationship('Tracks', back_populates='MediaType', lazy='joined')