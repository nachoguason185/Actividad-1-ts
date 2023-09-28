# Laboratorio de programacion seccion 17
# 28/09/2023
# Ejercicio: Ciclos for y while
# Diego Ignacio Sanchez Lopez
# Objetivo: Hacer secuencia de numeros 
#Proceso principales: tomar un numero e incrementar en uno a uno

# Usando un bucle for para contar de 1 en 1 desde 1 hasta 25
for i in range(1, 26):
    print(i, end=', ')
print()

# Usando un bucle while para contar de 1 en 1 desde 1 hasta 25
num = 1
while num <= 25:
    print(num, end=', ')
    num += 1
print()

# Usando un bucle for para contar de 5 en 5 desde 5 hasta 50
for i in range(5, 51, 5):
    print(i, end=', ')
print()

# Usando un bucle while para contar de 5 en 5 desde 5 hasta 50
num = 5
while num <= 50:
    print(num, end=', ')
    num += 5
print()

# Usando un bucle for para contar de 2 en 2 desde 20 hasta 0
for i in range(20, -1, -2):
    print(i, end=', ')
print()

# Usando un bucle while para contar de 2 en 2 desde 20 hasta 0
num = 20
while num >= 0:
    print(num, end=', ')
    num -= 2
print()


