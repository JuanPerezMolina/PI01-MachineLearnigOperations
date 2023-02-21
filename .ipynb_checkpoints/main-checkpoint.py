from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import pandas as pd
app = FastAPI()

class Pelicula(BaseModel):
    titulo: str
    director: str
    fecha_lanzamiento: Optional[str]
    duracion: int

# http://127.0.0.1:8000
@app.get('/')
def index():
    return('Aplicacion ETL')


@app.get('/peliculas/{plataforma} {keyword}')
def get_word_count(plataforma,keyword):
    '''
    Función que cuenta la cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
    '''
    df_movies = pd.read_csv('movies.csv')
    id_requerido = plataforma[0].str.lower()
    df_movies_plataforma = df_movies[(df_movies['id'][0]==id_requerido)&(keyword in df_movies['title'])]
    cant = int(df_movies_plataforma.shape[1])
    return{'Plataforma':plataforma, 'Cantidad':cant}

@app.post('/peliculas/')
def insertar_pelicula(pelicula:Pelicula):
    return{'Message':f"Pelicula {pelicula.titulo} insertada"}