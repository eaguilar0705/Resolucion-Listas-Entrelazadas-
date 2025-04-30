# Problema #2
# Version : 1.0
# Fecha : 30/04/2025
# Autores : Diego Urbina, Julio Delgadillo, Emmanuel Aguilar
"""Implementa un método llamado “ordena” que reciba una pila de enteros como parámetro
y devuelva la pila ordenada de mayor (fondo de la pila) a menor (top de la pila).
Ejemplo:
Entrada -> [ 1, 3, 2, 4]
Salida -> [ 4, 3, 2, 1]
"""

def ordena(pila):
    # PRimero vaciamos la pila y pasamos los elementos a una lista auxiliar
    lista_aux = []
    while pila:
        lista_aux.append(pila.pop())

    # Despues ordenamos la lista de mayor a menor
    lista_aux.sort(reverse=True)

    # Finalmente econstruimos la pila ordenada (mayor al fondo, menor al tope)
    for elemento in lista_aux:
        pila.append(elemento)

    return pila

# Ejemplo de uso
pila_original = [1, 3, 2, 4]
pila_ordenada = ordena(pila_original)
print(pila_ordenada)  # Salida: [4, 3, 2, 1]

