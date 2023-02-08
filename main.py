import os
from pprint import pprint

def lista_ficheros  (ruta_inicial=os.path.dirname(os.path.realpath(__file__)), carpeta="genomas"):
    """
    Proveer una lista de los ficheros
    :param ruta_inicial: carpeta donde se explorarán los ficheros. El valor predeterminado es la carpeta inicial donde está el script.
    :return: diccionario con la estructura de los ficheros
    """
    # Diccionario vacío que contendrá los ficheros
    lista_ficheros = list()
    # Booleanos para saber si es una subcarpeta vacía o si contiene ficheros .txt
    subcarpeta_txt      = False
    subcarpeta_vacia    = True

    # Hallar el directoio actual y concatenar la carpeta
    ruta = ruta_inicial + "/" + carpeta

    # Hallamos la lista de ficheros en la subcarpeta, así como los que sean .txt (los que vamos a analizar)
    print("Lista de subcarpetas en la carpeta {0}".format(carpeta))
    lista_ficheros  = os.listdir(ruta)
    lista_txt       = [x for x in lista_ficheros if ".txt" in x]

    # Llenar los booleanos
    if len(lista_txt) == 0:
        subcarpeta_vacia = True
    if len(lista_txt) == len(lista_ficheros):
        subcarpeta_txt = True

    pprint(lista_ficheros)

if __name__ == "__main__":
    print("Corriendo script...")
    lista_ficheros()

