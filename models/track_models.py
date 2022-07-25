from sqlalchemy import Boolean, Column, DateTime, Integer, String , Float, ForeignKey
from sqlalchemy.orm import relationship

from config_db import Base


class Tracks(Base):
    __tablename__ = "tracks"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey('Albums.AlbumId'))
    Album = relationship('Albums', back_populates='Tracks', lazy='joined')
    MediaTypeId = Column(Integer, ForeignKey('media_types.MediaTypeId'))
    MediaType = relationship('MediaTypes', back_populates='Tracks', lazy='joined')
    GenreId = Column(Integer, ForeignKey('Genres.GenreId'))
    Genre = relationship('Genres', back_populates='Tracks', lazy='joined')
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float)