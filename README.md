
<p align=center><img src=https://datascientest.com/es/wp-content/uploads/sites/7/2020/11/illu_machine_learning_blog-19-1024x562.png.webp><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Maching Learning Operation`**</h1>
## <h1 align=center>**`Juan Jose Perez`**</h1>



¡Bienvenidos a mi primer proyecto individual de la etapa de labs! Mi nombre es Juan Jose Pérez y presento en mi trabajo el rol de un ***Data Science***.  

<hr>  

## **Descripción del problema (Contexto y rol a desarrollar)**

## Contexto

Se requiere realizar una proceso de ETL (Extracción, Transformación y Carga) de datos a partir de cuatro archivos en formato csv. Estos archivos poseen la misma estructura de campos lo cual permite unirlos en un solo archivo luego de realizar todas las transformaciones que son requeridas por el area de Analisi de datos de la empresa, estos datos seran  disponibilizados  mediante la elaboración y ejecución de una API para luego alimentar un modelo de clasificacion de maching learning de recomendación.



## Rol a desarrollar

Como parte del equipo de data de la empresa, el área de análisis de datos le solicita al área de Data Engineering al que pertenesco ciertos requerimientos para el óptimo desarrollo de las actividades de analisis y posterior implementación de un modelo de clasificación ML. 



## **Procedimento**

**`Transformaciones`**:  Se requiere estas transformaciones para los datos:


+ Generar campo **`id`**: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`**)

+ Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**

+ Los campos de texto deberán estar en **minúsculas**, sin excepciones

+ El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

<br/>

**`Desarrollo API`**:  Para disponibilizar los datos la empresa usa el framework ***FastAPI***. El analista de datos requiere consultar:

+ Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))

+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))

+ Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))

+ Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))
<br/>


**`Deployment`**: La empresa suele usar Deta Space  para realizar el deploy de sus aplicaciones.
<br/>

<br/>

**`Video`**: El Tech Lead que solicitó esta tarea pidió que sintetice en un video de ***5 minutos*** mi trabajo resaltando cómo este ayuda a los analistas de datos. Ver [aqui](https://youtu.be/gRosvacOKNs) el video sobre el trabajo)


<br/>

## **Criterios de evaluación**

**`Código`**: **`ETL y API`** El codigo esta bien documentado en dos archivos fuentes: el archivo **transformaciones.ipynb** que es un notebook que contiene cada uno de los pasos para realizar las transformaciones requeridas sobre los datos brutos (esta ubicado en el directorio raiz) y el archivo **main.py** que implementa las consultas que luego alimentan a la API (ubicado en el directorio fastapi), ambos archivos estan bien documentados.

**`Maching Learning`** Son los archivos fuentes:  **1_limpiar_datos.ipynb** , **2_escalado_normalizacion.ipynb**, **2_escalado_normalizacion.ipynb** en formato notebook. 

**`Repositorio`**: El link del repositorio engithub esta [aqui](https://github.com/gurufractal/PI01-MachineLearnigOperations.git) 

**`url de la API`**: El link para hacer el deploy de la API que desarrolle esta [aqui](https://peliculas-2-e7945481.deta.app/)



<br/>

