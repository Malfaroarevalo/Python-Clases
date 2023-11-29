# Ejercicio 5 TIM3
print ("Ejercico Nº5 - Módulo 3")

solis=[]

print("Ingrese números que desee sumar, si quiere detener el programa presione enter con un espacio en blanco.\n")

while True:
    salias =input("Ingrese un número: ")
    if salias == " ":
        break
    else:
        try:
         x=int(salias)
         solis.append(x)
        except ValueError:
         print("No has ingresado un número, intentalo nuevamente:")
         
result=0
for i in range(len(solis)):
    result=result+solis[i]

print("La suma de los números ingresados es: " + str(result))
#FIN