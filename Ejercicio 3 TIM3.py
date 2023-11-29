# Ejercicio 3 TIM3

print ("Ejercico Nº3 - Módulo 3")

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

print("El puntaje de los datos ingresados es: " + str(suma_total)"!")
#


