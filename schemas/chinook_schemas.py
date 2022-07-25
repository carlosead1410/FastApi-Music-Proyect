from datetime import datetime
from typing import Optional, Text
from pydantic import BaseModel


#Esta clase es la respuesta que se le envia al cliente (Lista de Artistas)
class ArtistInfo (BaseModel):
	Name: Optional[Text]
 
	class Config:
		orm_mode = True
		

#Esta clase es la respuesta que se le envia al cliente (Lista de Albunes del artista)
class ArtistAlbum(BaseModel):
	AlbumId: int
	Title: Optional[Text]
	
	class Config:
		orm_mode = True
		

#Esta clase es la respuesta que se le envia al cliente (Lista de Tracks del album - Lista de Tracks de Un Artista)
class TracksList(BaseModel):
	Name: Optional[Text]
	Milliseconds: Optional[int]
	Bytes: Optional[int]
	UnitPrice: Optional[float]
	Composer: Optional[Text]
	AlbumId: Optional[int]
	MediaTypeId: Optional[int]
	GenreId: Optional[int]
 
	class Config:
		orm_mode = True
  

#Esta clase es la respuesta que se le envia al cliente (Detalle de Una Cancion)

class GenreSchema(BaseModel):
	GenreId: Optional[int]
	Name: Optional[Text]
	class Config:
		orm_mode = True
  

class MediaTypeSchema(BaseModel):
	MediaTypeId: Optional[int]
	Name: Optional[Text]
 
	class Config:
		orm_mode = True
  


class TrackDetail(BaseModel):
	Name: Optional[Text]
	Milliseconds: Optional[int]
	Bytes: Optional[int]
	UnitPrice: Optional[float]
	Composer: Optional[Text]
	AlbumId: Optional[int]
	MediaTypeId: Optional[int]
	Genre: Optional[GenreSchema]
	MediaType: Optional[MediaTypeSchema]
 
	class Config:
		orm_mode = True
  