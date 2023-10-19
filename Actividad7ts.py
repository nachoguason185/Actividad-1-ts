# Laboratorio de programacion seccion 17
# 19/10/2023
# Ejercicio: Actividad 7
# Diego Ignacio Sanchez Lopez
# Objetivo: Solicite al usuario una palabra, muestre en pantalla una a una, las primeras 3 letras de la cadena ingresada por el usuario. 
# Entrada: Primeras 3 letras
#Proceso: principales 

# Solicitar una palabra al usuario
palabra = input("Ingresa una palabra: ")

# Mostrar las primeras 3 letras de la palabra
primeras_tres_letras = palabra[:3]
print("Las primeras tres letras son:", primeras_tres_letras)

# Almacenar las primeras tres letras en una nueva cadena
nueva_subcadena = primeras_tres_letras

# Solicitar un nuevo texto al usuario
texto = input("Ingresa un nuevo texto: ")

# Reemplazar todas las vocales "O" por la letra "x" en el texto
texto_modificado = texto.replace("o", "x")

# Mostrar el texto modificado
print("Texto modificado:", texto_modificado)
