from main import *

class Grafo:
    def init(self, vertices, aristas):
        self.vertices = vertices
        self.aristas = aristas
        self.grafo = {}

        for v in vertices:
            self.grafo[v] = {}
        for inicio, fin, peso in aristas:
            self.grafo[inicio][fin] = peso
            self.grafo[fin][inicio] = peso  

    def str(self):
        resultado = "Vértices: {}\n".format(self.vertices)
        resultado += "Aristas: {}\n".format(self.aristas)
        return resultado

    def dijkstra(self, inicio, fin):
        # Inicializar las estructuras de datos
        distancia = {v: float('inf') for v in self.vertices}
        distancia[inicio] = 0
        visitados = set()

        # Algoritmo de Dijkstra
        while len(visitados) < len(self.vertices):
            # Encontrar el vértice no visitado con la distancia mínima
            min_vertice = None
            for v in self.vertices:
                if v not in visitados and (min_vertice is None or distancia[v] < distancia[min_vertice]):
                    min_vertice = v

            # Marcar el vértice como visitado
            visitados.add(min_vertice)

            # Actualizar las distancias de los vértices adyacentes
            for vecino, peso in self.grafo[min_vertice].items():
                nueva_distancia = distancia[min_vertice] + peso
                if nueva_distancia < distancia[vecino]:
                    distancia[vecino] = nueva_distancia

        # Reconstruir el camino más corto
        camino = []
        actual = fin
        while actual != inicio:
            camino.append(actual)
            for vecino in self.grafo[actual]:
                if distancia[vecino] + self.grafo[actual][vecino] == distancia[actual]:
                    actual = vecino
                    break
        camino.append(inicio)

        # Mostrar el camino más corto
        print("El camino más corto desde {} hasta {} es:".format(inicio, fin))
        print(" -> ".join(camino[::-1]))
        print("Peso total:", distancia[fin])
