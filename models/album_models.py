from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config_db import Base

class Albums(Base):
    __tablename__ = 'Albums'
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey('Artists.ArtistId'))
    Artist = relationship('Artists', back_populates='Albums', lazy='joined')
    Tracks = relationship('Tracks', back_populates='Album', lazy='joined')