# Pedir al usuario un número n
n = int(input("Introduce un número: "))

# Inicializar variables
contador = 1
suma = 0

# Mientras contador sea menor o igual que n
while contador <= n:
    suma += contador
    contador += 1

# Mostrar el resultado
print("La suma de los", n, "primeros números es:", suma)
