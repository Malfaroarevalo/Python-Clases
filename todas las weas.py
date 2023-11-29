# Ejercicio Nº1
print ('Ejercicios Modulo Nº3')
print ('Ejercicio Nº1')
numeros = []

print ("Ingrese de 10 a 20 números, cuando haya superado los 10 números puede ingresar 0 para finalizar el programa: ")
while len(numeros)<20 :
	num = int(input("Ingrese cualquier número "))
	if len(numeros) > 9 and num==0:
		break
	elif num == 0:
		print ("Aún no puede detener el programa, usted no ha ingresado 10 o más números")
	else:
		numeros.append(num)

print("A continuación se presentan los números que usted ingresó de mayor a menor")

numeros.sort(reverse=True)

print(*numeros)
print ('Finaliza el Ejercicio Nº1')

# Ejercicio Nº2
# Escribir un programa que almacene palabras ingresadas por el usuario.
# Debe recibir ingreso de palabras hasta que el usuario ingrese tres asteriscos ***. 
# Luego de esto, las palabras se deben mostrar por pantalla una única vez. 
# Es decir que, si el usuario ingresó palabras repetidas, se deben mostrar solo una vez.
print ('Ejercicio Nº2')
palabras = []

while True:
    palabra = input("Ingrese una palabra: ")
    if palabra == "***":
        break
    else:
        palabras.append(palabra)

palabras_sin_repetir = []

for i in palabras:
    if i not in palabras_sin_repetir:
        palabras_sin_repetir.append(i)

print(palabras_sin_repetir)
print ('Finaliza el Ejercicio Nº2')

# Ejercicio 3
print ('Comienza el Ejercicio Nº3')
string = input("Ingrese una palabra: ")
suma =[0,0,0,0,0,0,0]
# se deben crear las listas#
lista_1=["a","e","i","l","n","o","r","s","t","u"] 
lista_2=["d","g"]
lista_3=["b","c","m","p"]
lista_4=["f","h","v","w","y"]
lista_5=["k"]
lista_6=["j","x"]
lista_7=["q","z"]

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

suma_total=0
for i in range(len(suma)):
    suma_total= suma_total+ suma[i]

print("El puntaje de la palabra ingresada es: " + str(suma_total))
print ('Finaliza el Ejercicio Nº3')

# Ejercicio 4

# crear programas que determinee si dos palabras son anagramas
print ('Comienza el Ejercicio Nº4')
print("Ingrese 2 palabras ")
palabra_1=input("Ingrese la primera palabra ")
palabra_2=input("Ahora ingrese la segunda palabra ")

if len(palabra_1) != len(palabra_2):
    print("estas 2 palabras no coinciden, por lo tanto no son anagramas")
else:
    if sorted(palabra_1) == sorted(palabra_2):
        print("Estas palabras son anagramas")
    else:
        print("Estas palabras no son anagramas")

print ('Finaliza el Ejercicio Nº4')        
# Ejercicio 5
print ('Comienza el Ejercicio Nº5')
numeros=[]

print("Ingrese números que desee sumar, si quiere detener el programa presione enter con un espacio en blanco ")

while True:
    numero =input("Indrese un número: ")
    if numero == " ":
        break
    else:
        try:
         x=int(numero)
         numeros.append(x)
        except ValueError:
         print("No has ingresado un número, intentalo nuevamente:")

suma=0
for i in range(len(numeros)):
    suma=suma+numeros[i]

print("la suma de los números ingresados es: " + str(suma))
print ('Finaliza el Ejercicio Nº5')