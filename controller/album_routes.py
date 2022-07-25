from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import List

from schemas.chinook_schemas import TracksList
from dependencies import get_db
from repositories.album_repository import AlbumRepo
router = APIRouter(
    tags=["Albums"]
)

@router.get("/albums/{id}/", response_model=List[TracksList], status_code=status.HTTP_200_OK)
def get_track_list(
    id: int,
    db: Session = Depends(get_db),
    album_repo: AlbumRepo = Depends(AlbumRepo)
    ) -> List[TracksList]:
    
    return album_repo.get_album_song(db = db, album_id = id)
