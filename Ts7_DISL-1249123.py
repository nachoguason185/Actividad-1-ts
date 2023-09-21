# Laboratorio de programacion seccion 17
# 5/09/2023
# Ejercicio: uso de variables python
# Diego Ignacio Sanchez Lopez
# Objetivo: Agregue una instrucción que muestre su nombre completo, Solicite al usuario que ingrese un número en el rango de 1 a 10, verifique que esté en el rango correcto.
# Entrada: Numero de 1 a 10
#Proceso: principales 

# Mostrar el nombre completo
print("Mi nombre completo es Diego Ignacio Sánchez López")

while True:
    # Solicitar al usuario un número en el rango de 1 a 10
    numero = int(input("Ingrese un número entre 1 y 10: "))
    
    # Verificar que el número esté en el rango correcto
    if 1 <= numero <= 10:
        # Utilizar la instrucción for para mostrar la tabla de multiplicar
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} X {i} = {resultado}")
        
        # Preguntar al usuario si desea generar la tabla de otro número
        respuesta = input("¿Desea generar la tabla de otro número? (SALIR para terminar): ").upper()
        if respuesta == "SALIR":
            break
    else:
        print("El número no está en el rango correcto (1-10). Inténtelo de nuevo.")