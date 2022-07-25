from typing import List

from sqlalchemy.orm import Session
from schemas.chinook_schemas import ArtistInfo, ArtistAlbum, TracksList
from models.artist_models import Artists
from models.album_models import Albums
from models.track_models import Tracks


class ArtistRepo:
    def get_all_artist(self, db: Session) -> List[ArtistInfo]:
        artist_list: List[ArtistInfo] = db.query(Artists).all()
        return artist_list
    
    def get_artist_albums(self, db: Session, artist_id: int) -> List[ArtistAlbum]:
        artist_albums: List[ArtistAlbum] = db.query(Albums).filter(Albums.ArtistId == artist_id).all()
        return artist_albums

    def get_artist_tracks(self, db: Session, artist_id: int) -> List[TracksList]:
        artist_tracks: List[TracksList] = db.query(Tracks).join(Albums, Albums.AlbumId == Tracks.AlbumId).join(Artists, Artists.ArtistId == Albums.ArtistId).filter(Artists.ArtistId == artist_id).all()
        return artist_tracks