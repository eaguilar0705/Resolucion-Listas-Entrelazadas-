def convBinario(numero):
    if numero == 0:
        return [0]

    pila = []

    while numero > 0:
        residuo = numero % 2
        pila.append(residuo)
        numero //= 2

    binario = []
    while pila:
        binario.insert(0, pila.pop())

    return binario

# Entrada del usuario
try:
    numero = int(input("Ingrese un número entero para convertir a binario: "))
    resultado = convBinario(numero)
    print("Binario:", resultado)
except ValueError:
    print("Por favor, ingrese un número entero válido.")

