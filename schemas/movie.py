from pydantic import BaseModel, Field
from typing import Optional, List


class Movie(BaseModel):
     id: Optional[int] = None
     title: str = Field(min_length= 5, max_length=15)
     overview: str = Field(min_length= 15, max_length=50)
     year: int  = Field(le=2022)
     rating: float = Field(ge=1, le=10) 
     category: str = Field(min_length=5, max_length=15)

     class Config:
        schema_extra = { # AQUI SI COLOCO json_schema_extra si se organiza las clases como debe epro no funcionan las comprobaciones
            "example": {
              "id": 1,
              "tittle": "Mi Pelicula",
              "overview": "Descripcion de la Pelicula",
              "year": 2022,
              "rating": 9.8,
              "category": "Accion"
            }
        }