from typing import List

from sqlalchemy.orm import Session
from schemas.chinook_schemas import TracksList
from models.album_models import Albums
from models.track_models import Tracks


class AlbumRepo:
    def get_album_song(self, db: Session, album_id: int) -> List[TracksList]:
        track_list: List[TracksList] = db.query(Tracks).filter(Tracks.AlbumId == album_id).all()
        return track_list