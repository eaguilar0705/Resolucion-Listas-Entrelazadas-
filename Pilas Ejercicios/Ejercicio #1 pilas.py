def separarParImpar(pila):
    pila_pares = []
    pila_impares = []

    # Procesar la pila original
    while pila:
        numero = pila.pop()
        if numero % 2 == 0:
            pila_pares.append(numero)
        else:
            pila_impares.append(numero)

    # Primero se agregan los pares, luego los impares
    resultado = []
    
    # Volteamos las pilas para respetar el orden original
    while pila_pares:
        resultado.append(pila_pares.pop())

    while pila_impares:
        resultado.append(pila_impares.pop())

    return resultado

# Ejemplo de uso
pila = [2, 3, 6, 8, 11, 13, 18, 21]
nueva_pila = separarParImpar(pila.copy())
print("Resultado:", nueva_pila)
