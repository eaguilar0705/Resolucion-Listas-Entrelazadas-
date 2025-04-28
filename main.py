# Problema #2
# Version : 1.0
# Fecha : 28/04/2025
# Autores : Diego Urbina, Julio Delgadillo, Emmanuel Aguilar
"""Se requiere automatizar un mapa que contiene las estaciones de una ruta previamente establecida para
una aplicacion que indique, a partir de un punto de la ruta, el tiempo estimado para llegar a un destino determinado de
la misma."""

from ruta import Ruta  # Importamos la clase Ruta

# Creamos la ruta
ruta = Ruta()

# Agregamos las estaciones
ruta.agregar_estacion("A", 5)
ruta.agregar_estacion("B", 10)
ruta.agregar_estacion("C", 8)
ruta.agregar_estacion("D", 7)

# Calculamos el tiempo desde la estacion A hasta la estacion C
tiempo = ruta.calcular_tiempo("A", "C")

# Mostramos el resultado
if tiempo is not None:
    print(f"El tiempo estimado de A a C es: {tiempo} minutos")
else:
    print("No se pudo calcular el tiempo, revise las estaciones.")
