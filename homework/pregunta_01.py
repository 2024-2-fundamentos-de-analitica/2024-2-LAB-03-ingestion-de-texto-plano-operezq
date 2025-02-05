"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    with open("files/input/clusters_report.txt", "r") as file:
        texto = file.readlines()
        info = []
        dataset = {}
        for linea in texto[4:]:
            if linea.strip():  
              columna= linea.split()
              if columna[0].isdigit():
                dataset = {
                    "cluster" : int(columna[0]),
                    "cantidad_de_palabras_clave": int(columna[1]),
                    "porcentaje_de_palabras_clave": float(columna[2].replace(",",".")),
                    "principales_palabras_clave": " ".join(columna[4:]).rstrip(".")
                    }
                info.append(dataset)
                
              else:
                 dataset["principales_palabras_clave"] += ' ' + ' '.join(columna).rstrip(".")


        df = pd.DataFrame(info)

    return df
