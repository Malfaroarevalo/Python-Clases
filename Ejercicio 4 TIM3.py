# Ejercicio 4 TIM3

print ("Ejercico Nº4 - Módulo 3")
# Se ingresan variables para que el usuario pueda ingresar palabras por teclado y determinar si estas son anagramas
print("Ingrese dos palabras:")
popis_1=input("Ingrese la primera palabra:")
popis_2=input("Ahora ingrese la segunda palabra:")

#Recorre ambas variables para contar el valor y que estos coinicidan.
if len(popis_1) != len(popis_2):
    print("Estas 2 palabras no coinciden!, por lo tanto no son anagramas.")
else:#Imprime los valores
    if sorted(popis_1) == sorted(popis_2):
        print("Estas palabras son anagramas!")
    else:
        print("Estas palabras no son anagramas!")

print ('Finaliza el Ejercicio Nº4') 