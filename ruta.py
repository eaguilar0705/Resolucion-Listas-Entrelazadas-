# Problema #2
# Version : 1.0
# Fecha : 28/04/2025
# Autores : Diego Urbina, Julio Delgadillo, Emmanuel Aguilar
"""Se requiere automatizar un mapa que contiene las estaciones de una ruta previamente establecida para
una aplicacion que indique, a partir de un punto de la ruta, el tiempo estimado para llegar a un destino determinado de
la misma."""

from estacion import Estacion  # Importamos la clase Estacion

# Clase Ruta (Lista Enlazada)
class Ruta:
    def __init__(self):
        self.inicio = None  # Inicio de la lista de estaciones

    # Metodo para agregar una nueva estacion al final de la ruta
    def agregar_estacion(self, nombre, tiempo_siguiente):
        nueva_estacion = Estacion(nombre, tiempo_siguiente)
        if not self.inicio:
            self.inicio = nueva_estacion  # Si la ruta esta vacia, la nueva estacion es el inicio
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente  # Recorremos hasta el ultimo nodo
            actual.siguiente = nueva_estacion  # Agregamos la nueva estacion al final

    # Metodo para calcular el tiempo desde un punto de origen hasta un destino
    def calcular_tiempo(self, origen, destino):
        actual = self.inicio
        total_tiempo = 0
        encontrado_origen = False  # Bandera para saber si ya pasamos por el origen

        while actual:
            if actual.nombre == origen:
                encontrado_origen = True  # Activamos la suma de tiempos al encontrar el origen
            if encontrado_origen:
                total_tiempo += actual.tiempo_siguiente
                if actual.nombre == destino:
                    return total_tiempo - actual.tiempo_siguiente
                    # Restamos el tiempo extra porque al llegar al destino no se suma el siguiente tramo
            actual = actual.siguiente

        return None  # Si no se encuentra el destino o el origen, se retorna None
