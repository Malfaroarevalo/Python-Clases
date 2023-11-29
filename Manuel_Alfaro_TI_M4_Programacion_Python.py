print("Ejercicio 1 Modulo 4")

import re #Se importa librería regular

def verif_sinc(contra): #Se crea una funcion "verif_sinc" para verificar si la constraseña es segura o no
    if 8 <= len(contra) <= 16: #Ciclo if que recorre desde el 8 minimo al 16 maximo
        if re.search('[a-z]', contra) and re.search('[A-Z]', contra): #busca dentro de la librería importada valores asignados dentro de "contra"
            if re.search('[\d]', contra):
                if re.search('[@$#!?_.,+*/]', contra):
                    print("¡Su contraseña es segura!")

    else:
        print("Ésta no es una contraseña segura")


ronizada = input('Escriba una contraseña mayor a 8 y menor a 16 dígitos, incluyendo al menos una mayuscula, un número: ')

print(verif_sinc(ronizada))

#///////////////////////////////////////////////////////////////////////////////////////////////////

print("Ejercicio 2 Modulo 4")

suma=0
num=int(input("Ingrese un número: "))
while num!=0:
    suma=suma+num
    num=int(input("Ingrese otro número(Ingrese 0 para finalizar): "))
print("Suma total:", suma)

#///////////////////////////////////////////////////////////////////////////////////////////////////

print("Ejercicio 3 Modulo 4")

total = 10 #Saldo inicial # Usuario x con tres opciones
print("Sea bienvenido al pequeño Banco Pytho!\n\
Que quieres hacer\n\ 
1.- Ingresar dinero:\n\
2.- Retirar dinero:\n\
3.- Salir: \n")
    
opcion=int(input()) #Input para opciones con los metodos requeridos
if opcion == 1:
    ingreso=float(input("Cuantos dineros desea ingresar?:"))
    total+=ingreso
    print(f"Tu saldo es de {total:.2f}")
elif opcion == 2:
    egreso=float(input("¿Cuanto dinero deseas reStirar?"))
    if total-egreso<0:
        print(f"No dispone de saldo suficiente, su estado actual es {total:.2f}")
    else:
        total-=egreso
        print(f"Tu saldo actual es de {total:.2f}")
elif opcion==3:
    quit()
   