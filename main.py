from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config_db import Base, engine
from controller.artist_routes import router as artist_router
from controller.album_routes import router as album_router
from controller.track_routes import router as track_router

def get_application():
	
	Base.metadata.create_all(bind=engine)
	
	app = FastAPI(title="API TuEncavaMusic", version="1.0.0")
	
	app.add_middleware(
		CORSMiddleware,
		allow_origins=["*"],
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)
 
	app.include_router(artist_router, prefix="/music-store/api/v1")
	app.include_router(album_router, prefix="/music-store/api/v1")
	app.include_router(track_router, prefix="/music-store/api/v1")
	return app

app = get_application()

@app.get("/")
def home() -> dict:
	return {"message": "Hello World"}