#Ejercico 1 Modulo 2

filas = int(input("Ingrese número de Filas: ")) #Variable para solicitar filas por teclado
columnas = int(input("Ingrese número de Columnas: ")) #Variable para solicitar columnas por teclado

for i in range(filas): #For para repetir la operación dentro de filas
    for j in range(columnas): # For para repetir la operación dentro del rango en columnas
    print("|--", end="--") # Datos que imprimirá con los datos ingresados anteriormente
    print("|")# Imprime en pantalla un puntito final para la estetica.