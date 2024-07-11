# Proyecto Final - Recommender Systems

Este repositorio contiene el código necesario para replicar el trabajo del grupo 8 en el proyecto final del curso de Sistemas de Recomendación. Aquí encontrarás instrucciones detalladas sobre los datasets, el procesamiento de datos, y la ejecución del código para obtener los resultados del estudio.

## **Datasets**

Los datasets utilizados en este proyecto provienen de diversas fuentes. A continuación, se presentan los enlaces para acceder a cada uno de ellos:

* Datasets originales (books, anime, lfm, ml): [Zenodo](https://zenodo.org/records/7428435)
* Dataset de Netflix: [Kaggle](https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data)
* Dataset de MyAnimeList 2020: [Kaggle](https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020?select=rating_complete.csv)

## Procesamiento de los Datos

Para los cuatro datasets originales (books, anime, lfm, ml), se utilizaron versiones filtradas disponibles en el paper original.

### Netflix

Para el dataset de Netflix, utilizamos el archivo `Netflix_filter_data.ipynb` para filtrar los datos. Dado que el dataset es muy grande, se crearon subarchivos para evitar problemas de memoria. El procesamiento genera una carpeta llamada `netflix` que contiene todos los archivos `.csv` necesarios.

### MyAnimeList 2020

Para el dataset de MyAnimeList 2020, se creó el archivo `myanime_600k.csv`, que contiene las primeras 633,279 filas del dataset original.

Todos los archivos procesados utilizados en este proyecto están disponibles en las carpetas `data` y `netflix`.

## Ejecución del Código

Para replicar los experimentos y obtener los resultados del estudio, siga las siguientes instrucciones:

1. **Ejecutar los códigos originales:**

   - Ejecute `MMRS_fairness.ipynb` para replicar los experimentos con los cuatro datasets originales. Este notebook permite elegir entre los modelos KNNBasic, KNNWithMeans, NMF y CoClustering. Los resultados obtenidos se incluyen en la última celda del notebook.
2. **Obtener resultados de MyAnimeList 2020 y Netflix:**

   - Ejecute `MMRS_myanime.ipynb` para obtener los resultados del dataset de MyAnimeList 2020.
   - Ejecute `MMRS_netflix.ipynb` para obtener los resultados del dataset de Netflix.
3. **Resultados del modelo Most Popular:**

   - Ejecute `MMRS_most_popular.ipynb` para obtener los resultados del modelo de recomendación basado en popularidad.
4. **Resultados del modelo ALS:**

   - Ejecute `MMRS_ALS.ipynb`. Puede seleccionar el dataset a utilizar (entre los cuatro datasets originales, Netflix y MyAnimeList 2020) comentando y descomentando el código correspondiente.
## Aleatoriedad

Es importante destacar que los resultados obtenidos a partir de los modelos de recomendación presentan un grado de aleatoriedad inherente. Es por esto que al ejecutar los codigos y replicar el experimento los resultados podrian variar.

Asegúrese de seguir las instrucciones específicas dentro de cada notebook para configurar correctamente los entornos y ejecutar los experimentos de manera eficiente.
