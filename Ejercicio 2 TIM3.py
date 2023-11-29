# Ejercicio Nº2 TIM3

print ("Ejercicio Nº2 - Módulo 3")

palabras = []
#Ciclo while para guardar las palabras ingresadas por usuario
while True:
    palabra = input("Ingrese una palabra: ")
    if palabra == "***":#termina el programa ingresando los datos informados
        break
    else:
        palabras.append(palabra)
#Luego guarda las palabras para determinar que no se repitan e imprime solo las palabras únicas.
palabras_sin_repetir = []

for i in palabras:
    if i not in palabras_sin_repetir:
        palabras_sin_repetir.append(i)

print(palabras_sin_repetir)
#
