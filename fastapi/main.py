from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import pandas as pd
from collections import Counter

app = FastAPI()

class Pelicula(BaseModel):
    titulo: str
    director: str
    fecha_lanzamiento: Optional[str]
    duracion: int

# http://127.0.0.1:8000
@app.get('/')
def index():
    return('API para consultar las plataformas de películas')

@app.get('/get_max_duration/{anno} {plataforma} {tipo_duracion} ')
def get_max_duration(anno, plataforma, tipo_duracion ):
    ''' 
    Esta 1ra función indica la película que más duró según: año, plataforma y tipo de duración 
    '''
    df_movies = pd.read_csv('datasets\movies.csv')
    id_plataforma = plataforma[0].lower()
    # Creamos un dataframe df_plataforma solo con los registros de la plataforma indicada
    df_plataforma = df_movies[df_movies['id'].str[0] == id_plataforma] 
    # Creamos un df_filtered solo con las condiciones solicitadas
    df_filtered = df_plataforma[(df_plataforma['duration_type']==tipo_duracion)&(df_plataforma['release_year']==anno)] 
    # Ordenamos  df_filtered desendentemente por la columna duration_int 
    df_filtered = df_filtered.sort_values(by=['duration_int'], ascending=[False])
    pelicula_max = df_filtered.iloc[0, df_filtered.columns.get_loc('title')]
    
    return{'Pelicula que mas duró':pelicula_max}



@app.get('/get_score_count/{plataforma} {score} {anno}')
def get_score_count(plataforma, score, anno):
    ''' 
    Esta 2da función cuenta la cantidad de películas por plataforma con un puntaje 
    mayor a score (puntaje por reseñas) en determinado año
    '''
    df_movies = pd.read_csv('datasets\movies.csv')
    id_plataforma = plataforma[0].lower()
    # Creamos un dataframe df_plataforma solo con los registros de la plataforma indicada
    df_plataforma = df_movies[df_movies['id'].str[0] == id_plataforma] 
    # Creamos un df_filtered solo con las condiciones solicitadas
    df_filtered = df_plataforma[(df_plataforma['review_score'] > score)&(df_plataforma['release_year']==anno)] 
    #Contamos el numero de registros del dataframe que cumple todas las condiciones
    cantidad = int(df_filtered.shape[0])
    return{'Cantidad':cantidad}


@app.get('/get_count_platform/{plataforma}')
def get_count_platform(plataforma):
    ''' 
    Esta 3ra función cuenta la cantidad de series y películas por platafoma 
    '''
    df_movies = pd.read_csv('datasets\movies.csv')
    id_plataforma = plataforma[0].lower()
    # Crear un dataframe solo con los registros del rating (clasificacion) indicado
    df_plataforma= df_movies[df_movies['id'].str[0] == id_plataforma]
    #Contamos el numero de registros del dataframe que cumple todas las condiciones
    cantidad= int(df_plataforma.shape[0])
    return{'Cantidad':cantidad}



@app.get('/get_actor/{plataforma} {anno}')
def get_actor(plataforma, anno):
    ''' 
    Actor que más se repite según plataforma y año.
    '''
    df_movies = pd.read_csv('datasets\movies.csv')
    id_plataforma = plataforma[0].lower()
    # Crear un dataframe solo con los registros de la plataforma indicada
    df_plataforma= df_movies[(df_movies['id'].str[0] == id_plataforma)
                            &(df_movies['release_year']==anno)] 
    # Creamos una lista con todas las palabras en el campo 'actores'
    palabras = [palabra for registro in str(df_plataforma['cast']) for palabra in registro.split(',') if palabra.strip() ]

    # Contamos las ocurrencias de cada palabra en la lista
    conteo_palabras = Counter(palabras)
    # Obtenemos la palabra que más se repite
    actor_max = conteo_palabras.most_common(1)[0][0]
    
    return{'Actor que mas aparece en estas peliculas':actor_max}
