import os
from pprint import pprint

def lista_ficheros (ruta_inicial=os.path.dirname(os.path.realpath(__file__)), carpeta="genomas"):
    """
    Proveer una lista de los ficheros
    :param ruta_inicial: carpeta donde se explorarán los ficheros. El valor predeterminado es la carpeta inicial donde está el script.
    :return: lista con dos elementos: la lista de subcarpetas y la lista de ficheros .txt
    Se presupone que en las carpetas y subcarpetas hay sólo ficheros .txt
    """
    # Lista vacía que contendrá las subcarpetas y los ficheros
    output = [None, None]

    # Hallar el directoio actual y concatenar la carpeta
    ruta = ruta_inicial + "/" + carpeta

    # Hallamos la lista de ficheros en la subcarpeta, así como los que sean .txt (los que vamos a analizar)
    print("Lista de subcarpetas en la carpeta {0}".format(carpeta))
    lista               = os.listdir(ruta)
    lista_subcarpetas   = [ruta_inicial + "\\" + x for x in lista if not os.path.isfile(x)]
    lista_txt           = [ruta_inicial + "\\" + x for x in lista if ".txt" in x]

    output[0], output[1] = lista_subcarpetas, lista_txt
    pprint(output)
    return output

def main (ruta_inicial=os.path.dirname(os.path.realpath(__file__)), carpeta="genomas"):
    """
    Explorar todo el árbol de carpetas
    :param ruta_inicial: inicio donde están todas las subcarpetas y ficheros a explorar
    :param carpeta: carpeta donde se van a buscar los ficheros
    :return:
    """

if __name__ == "__main__":
    print("Corriendo script...")
    main()

