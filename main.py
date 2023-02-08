import os
from pprint import pprint

def estructura_completa(ruta_inicial=os.path.dirname(os.path.realpath(__file__))):
    """
    Retorna una lista con todos los ficheros en las carpetas que estén dentro de ruta_inicial
    :param ruta_inicial: directorio raíz donde se explorará
    :return: lista de ficheros
    """
    ficheros, ficheros_normalizados = [], []
    for root, dirs, files in os.walk(ruta_inicial):
        ficheros = ficheros + [root + "\\" + f for f in files]

    ficheros_relativos = [f.replace(os.path.dirname(os.path.realpath(__file__))+"\\", "") for f in ficheros]

    return ficheros_relativos

def leer_txt(fichero_entrada):
    """
    Lee un fichero de texto y lo convierte en una cadena de texto
    :param fichero_entrada: ruta del fichero (relativa)
    :return: cadena de texto de lo que haya en el fichero
    """
    with open(fichero_entrada, "r") as f:
        lineas = f.readlines()
        texto = "".join(lineas)
    return texto

def mostrar_ficheros_relevantes(lista_ficheros, cadena):
    """
    Muestra los ficheros que contengan la cadena de texto cadena
    :param lista_ficheros: lista de ficheros a explorar
    :param cadena: cadena
    :return: lista de ficheros
    """
    # Lista de ficheros .txt con el texto relevante
    lista_ficheros_relevantes = []
    for f in lista_ficheros:
        texto = leer_txt(f)
        if cadena in texto:
            lista_ficheros_relevantes.append("\n" + f + "\n" + texto)
    return lista_ficheros_relevantes

def buscar (carpeta="genomas", cadena="wax synthase"):
    """
    Explorar todo el árbol de carpetas
    :param carpeta: carpeta donde se van a buscar los ficheros
    :param cadena: texto a buscar
    :return:
    """

    # Hallar el directoio actual y concatenar la carpeta
    ruta = os.path.dirname(os.path.realpath(__file__)) + "\\" + carpeta
    # Mostrar estructura completa
    ficheros_todos = estructura_completa(ruta)
    # Leer todos los ficheros y buscar el texto especificado
    ficheros_relevantes = mostrar_ficheros_relevantes(ficheros_todos, cadena)
    # Mostrar ficheros
    print(ficheros_relevantes)

    return ficheros_relevantes

if __name__ == "__main__":
    print("Corriendo script...")
    output = buscar()
