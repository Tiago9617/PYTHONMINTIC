"""
Descripción y requerimientos:
Como consultor en recursos cinematográficos se le ha solicitado que organice la información necesaria que
contenga:

Entrada:
Países (Country)    Lengua Nativa (Language)    Monto Bruto (Gross Earnings) en ganancias
        str                 str                                 float

Esto, con el fin de conocer los recursos que han salido de nuestro suelo y, en consecuencia, tomar en un
futuro próximo la decisión de contratar recursos locales e iniciar la reactivación económica producto de la
crisis pandémica

En adición, usted cuenta con el archivo de datos “movies.csv” disponible desde:

https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true

En ese sentido, escriba una función que contenga la ruta de este archivo (descrita arriba) para su consulta
y/o manipulación. A partir de estos datos, utilice los métodos pd.read_csv() y pivot_table()y
cualquier otro método que ud. necesite para importar los datos del archivo .csv y crear una tabla dinámica
en base a los datos solicitados, finalmente, mostrar los resultados finales.

Salida:

Tipo de retorno     Descripción
Lista               Lista de valores indexados por ‘Country’ y ‘Languaje’ (Solo 10
                    registros) y la columna ‘Gross Earnings’

"""

import pandas as pd
import requests as r
import io

import os
# ruta file csv
rutaFileCsv ='https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'
##rutaFileCsv="main=xlsx"
def listaPeliculas(rutaFileCsv: str) -> str:
    root, extension = os.path.splitext(rutaFileCsv)
    global dict
    if "csv" in extension:#devuelve true si la cadena se encuentra
        try:
            f=r.get(rutaFileCsv).content
            dataSet=pd.read_csv(io.StringIO(f.decode('utf-8')))
            dict = dict(pd.Series(["Country", "Language", "Gross Earnings"]))
            print("{:<8}   {:<8}   {:<8}".format(dict[0], dict[1], dict[2]))
            for fila in range(10 +1):
                print("{:<8}   {:<8}   {:<8}".format(dataSet["Country"][fila], dataSet["Language"][fila], dataSet["Gross Earnings"][fila]) )
    
        except FileNotFoundError :
            print( "Error al leer el archivo de datos.")
    else:    
        return print("extension no valida")

if __name__ == "__main__":
    listaPeliculas(rutaFileCsv)