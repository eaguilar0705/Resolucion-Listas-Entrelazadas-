# Problema #2
# Version : 1.0
# Fecha : 28/04/2025
# Autores : Diego Urbina, Julio Delgadillo, Emmanuel Aguilar
"""Se requiere automatizar un mapa que contiene las estaciones de una ruta previamente establecida para
una aplicacion que indique, a partir de un punto de la ruta, el tiempo estimado para llegar a un destino determinado de
la misma."""

# Clase Estacion (Nodo)
class Estacion:
    def __init__(self, nombre, tiempo_siguiente):
        self.nombre = nombre                    # Nombre de la estacion
        self.tiempo_siguiente = tiempo_siguiente # Tiempo para llegar a la siguiente estacion
        self.siguiente = None                    # Puntero a la siguiente estacion
