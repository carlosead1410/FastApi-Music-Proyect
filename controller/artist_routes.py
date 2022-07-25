from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import List

from schemas.chinook_schemas import ArtistInfo, ArtistAlbum, TracksList
from dependencies import get_db
from repositories.artist_repository import ArtistRepo

router = APIRouter(
    tags=["Artist"]
)

@router.get("/singers/", response_model=List[ArtistInfo], status_code=status.HTTP_200_OK)
def get_artist_list(db: Session = Depends(get_db),
    artist_repo: ArtistRepo = Depends(ArtistRepo)
    ) -> List[ArtistInfo]:
    
    return artist_repo.get_all_artist(db=db)

@router.get("/singers/{id}/", response_model=List[ArtistAlbum], status_code=status.HTTP_200_OK)
def get_artist_album(
    id: int,
    db: Session = Depends(get_db),
    artist_repo: ArtistRepo = Depends(ArtistRepo)
    ) -> List[ArtistInfo]:
    
    return artist_repo.get_artist_albums(db = db, artist_id = id)

@router.get("/singer/", response_model=List[TracksList], status_code=status.HTTP_200_OK)
def get_artist_tracks(
    id: int,
    db: Session = Depends(get_db),
    artist_repo: ArtistRepo = Depends(ArtistRepo)
    ) -> List[TracksList]:
    
    return artist_repo.get_artist_tracks(db = db, artist_id = id)