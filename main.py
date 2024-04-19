from lib import *
import openpyxl 
import pandas as pd

def procesar_archivo_xlsx(archivo_xlsx):
    nombre_archivo = input("¿Cual es el nombre del archivo a procesar?: ")
    try:
        workbook = openpyxl.load_workbook(archivo_xlsx)
        sheet = workbook.active

        df = pd.read_excel(archivo_xlsx, index_col=0)

        vertices = list(df.columns)
        aristas = [(row, col, df.at[row, col]) for row in df.index for col in df.columns if df.at[row, col] > 0]

        grafo = Grafo(vertices, aristas)

        print("Matriz de Adyacencia Ponderada:")
        print(df)

        print("\nVértices:", vertices)
        print("Aristas:", aristas)

        # Imprimir el grafo
        print("\nGrafo:")
        print(grafo)

        # Realizar el algoritmo de Dijkstra
        inicio = 'B'
        fin = 'H'
        grafo.dijkstra(inicio, fin)

    except FileNotFoundError:
        print("El archivo '{}' no se encontro.".format(nombre_archivo))

nombre_archivo = "datos-Eval-3.xlsx"
procesar_archivo_xlsx(nombre_archivo)