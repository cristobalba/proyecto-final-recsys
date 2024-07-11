# proyecto-final-recsys

En el siguiente repositorio se encuentrar los codigos para poder recrear el paper del grupo 8 en el proyecto final.

## **Datasets **

- Los links para los dataset original (books, anime, lfm, ml) , se encuentran en los siguientes links: https://zenodo.org/records/7428435
- El dataset de netflix se encuentra en: https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data
- El dataset de myanimelist 2020 se encuentra en: https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020?select=rating_complete.csv

## Procesamiento de los datos

En cuanto a los 4 datasets originales; books, anime, lfm, ml. Estos se encuentrar filtrados desde el paper original.

Para netflix ocupamos el archivo Netflix_filter_data.ipynb para filtrar los datos. Estos cuentan con una gran cantidad de datos por lo que creamos sub archivos para el caso en que estos podrian crashear. De este archivo obtenemos la carpeta netflix con todos los archivos .csv necesarios.

Para myanimelist 2020 creamos el archivo myanime_600k.csv el cual contiene las primeras 633279 filas.

## Ejecucion de codigo

1. Para ejecutar los codigos de originales se debe correr MMRS_fairness.ipynb. En este se puede elegir entre los 4 datasets originales. El cual tiene los modelos KNNBasic, KNNWithMeans, NMF y COClustering. En la ultima celda se incluyen los resultados obtenidos
2. Para obtener los resultados de MyAnimeList 2020 y netflix se deben ejecutar los archivos MMRS_nyanime.ipynb y MMRS_netflix.ipynb respectivamente.
3. Para los resultados de most popular se debe ejecutar el archivo MMRS_most_popular.ipynb
4. Para ALS, se debe correr el archivo MMRS_ALS, en este se puede seleccionar comentando el codigo que dataset ocupar entre los 4 dataset originales, netflix y myanimelist2024
