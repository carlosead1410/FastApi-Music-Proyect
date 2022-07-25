from repositories.artist_repository import ArtistRepo
from config_db import SessionLocal

def get_artist_repo():
    return ArtistRepo()


# función helper para obtener una session de la bd
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()