from typing import List

from sqlalchemy.orm import Session
from models.track_models import Tracks
from models.genre_models import Genres
from models.mediatype_models import MediaTypes
from schemas.chinook_schemas import TrackDetail


class TrackRepo:
    def get_track_detail(self, db: Session, track_id: int) -> TrackDetail:
        track_detail: TrackDetail = db.query(Tracks).join(Genres,Genres.GenreId == Tracks.GenreId, isouter = True).join(MediaTypes,MediaTypes.MediaTypeId == Tracks.MediaTypeId, isouter =True).filter(Tracks.TrackId == track_id).first()
        
        return track_detail