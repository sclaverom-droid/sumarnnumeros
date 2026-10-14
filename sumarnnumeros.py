def sumar_n_primeros_numeros(n):
    # Inicialización de las variables
    contador = 1
    suma = 0
    
    # Bucle MIENTRAS (while)
    while contador <= n:
        suma = suma + contador
        contador = contador + 1
        
    # DEVOLVER: suma
    return suma

# Ejemplo de uso:
# resultado = sumar_n_primeros_numeros(5)
# print(resultado)  # Devolverá 15 (1+2+3+4+5)