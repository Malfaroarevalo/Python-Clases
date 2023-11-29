nume = int(input("Ingrese un numero del 1 al 9. \n"))
secu = int(input("Ingrese numeros de manera secuencial, comenzando desde 1 y saltandose los multiplos del numero elegido. \n" ))
if (nume%secu == 0): #Esta funcion hace un calculo para determinar si termina en 0
    print("%i es multiplo de %i"%(nume,secu))
else:
    print("%i no es multiplo de %i"%(nume,secu))
        