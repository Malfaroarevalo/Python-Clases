# Ejercicio Nº1 TIM3

print ("Programa N° 1 - Módulo 3")

nums = []

print ("Ingrese de 10 a 20 números, luego de los 10 números puede ingresar 0 para finalizar el programa:")
while len(nums)<20 : #Ciclo while que recorre la matriz nums hasta que sea menor a 20.
    num = int(input("Ingrese un número cualquiera:"))
    if len(nums) > 9 and num==0: #Ciclo if que indica si hay más de 9 números y termina el programa.
        break
    elif num == 0:# a menos que, el usuario no haya ingresado lo requerido.
        print ("Aún no puede detener el programa, usted no ha ingresado 10 o más números")
    else:
        nums.append(num)

print("A continuación se presentan los números que usted ingresó de mayor a menor")

#Ordena los números ingresados y muestra los datos ingresados en pantalla, ordenandolos de mayor a menor.
nums.sort(reverse=True)

print(*nums)
#FIN
#----------------------------------------------------------------------------------------------------------
# Ejercicio Nº2 TIM3

print ("Programa Nº2 - Módulo 3")

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
#FIN
#----------------------------------------------------------------------------------------------------------

# Ejercicio 3 TIM3

print ("Programa Nº3 - Módulo 3")

string = input("Ingrese una palabra: ")
suma =[0,0,0,0,0,0,0]

# Se crean las listas del diccionario
lista_1=["a","e","i","l","n","o","r","s","t","u"] 
lista_2=["d","g"]
lista_3=["b","c","m","p"]
lista_4=["f","h","v","w","y"]
lista_5=["k"]
lista_6=["j","x"]
lista_7=["q","z"]

#Ciclo for que llama a las variables string y suma
for i in range(len(lista_1)):
    suma[0] = suma[0] + string.count(lista_1[i])

for i in range(len(lista_2)):
    suma[1] = suma[1] + 2*string.count(lista_2[i])

for i in range(len(lista_3)):
    suma[2] = suma[2] + 3*string.count(lista_3[i])

for i in range(len(lista_4)):
    suma[3] = suma[3] + 4*string.count(lista_4[i])

for i in range(len(lista_5)):
    suma[4] = suma[4] + 5*string.count(lista_5[i])

for i in range(len(lista_6)):
    suma[5] = suma[5] + 8*string.count(lista_6[i])

for i in range(len(lista_7)):
    suma[6] = suma[6] + 10*string.count(lista_7[i])
    
#Calcula el total para mostrar el resultado en pantalla
suma_total=0
for i in range(len(suma)):
    suma_total= suma_total+ suma[i]

print("El puntaje de los datos ingresados es: " + str(suma_total))
#FIN
#----------------------------------------------------------------------------------------------------------

# Ejercicio 4 TIM3
print ("Programa Nº4 - Módulo 3")
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

#

# Ejercicio 5 TIM3
print ("Programa Nº5 - Módulo 3")

solis=[]

print("Ingrese números que desee sumar, si quiere detener el programa presione enter con un espacio en blanco.")

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