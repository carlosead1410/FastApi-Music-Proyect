from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import List

from schemas.chinook_schemas import TrackDetail
from dependencies import get_db
from repositories.track_repository import TrackRepo

router = APIRouter(
    tags=["Tracks"]
)

@router.get("/song/{id}/", response_model=TrackDetail, status_code=status.HTTP_200_OK)
def get_track_detail(
    id: int,
    db: Session = Depends(get_db),
    track_repo: TrackRepo = Depends(TrackRepo)
    ) -> TrackDetail:
    
    return track_repo.get_track_detail(db = db, track_id = id)