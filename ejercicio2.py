num = int(input("Ingrese un número entre 1 y 9: "))
#Se le solicita al usuario ingresar un numero entre el uno al 9 de manera aleatoria, la cual quedará guardada en la variable num.
i = 1 #variable para llevar el conteo del arreglo a recorrer

arreglo = [[], [1,3,5,7,9], [1,2,4,5,7,8], [1,2,3,5,6,7,9], [1,2,3,4,6,7,8,9], [1,2,3,4,5,7,8,9], [1,2,3,4,5,6,8,9], [1,2,3,4,5,6,7,9], [1,2,3,4,5,6,7,8]]
#arreglos de soluciones para todos los casos

arreglo_ocupar = arreglo[num-1] #se guarda en una variable el arreglo de soluciones que corresponde al numero ingresado por el usuario

while i<=len(arreglo_ocupar): #ciclo que recorre el arreglo de soluciones
    num_ingresado = int(input("Ingrese un numero secuencial que no sea multiplo de "+str(num)+": "))
    #se pide al usuario ingresar un numero secuencial que no sea multiplo del nro ingresado
    if (num_ingresado != arreglo_ocupar[i-1]): #se verifica si el nro es disinto al nro que corresponde ingresar
        print("PERDISTE!!!!! Error en numero ingresado, correspondia ingresar: "+str(arreglo_ocupar[i-1]))
        #ingresa aqui en caso de no haber ingresado el nro correlativo por lo tanto pierde
        break #con esto se sale del ciclo while
    i = i + 1 # en caso de haber ingresado bien el nro se continua con el siguiente nro y se aumenta la variable para avanzar a la siguiente posicion
if i>len(arreglo_ocupar):
    #se pregunta en caso de que la variable que se utilizar para ir recorriendo el arreglo es mayor al largo del arreglo significa que el usuario escribio todas las respuestas correctas
    print("GANASTE!!!! Ingresaste todos los numeros") #mensaje que le dice al usuario que ganó
    
    
    
    