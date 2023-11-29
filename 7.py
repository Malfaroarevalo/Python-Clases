#Ejercico 3 Modulo 2

fech1 = int(input( "Introduzca el año de nacimiento: ")) #Print preguntando el año inicial
fech2 = int(input("Introduzca el año actual: ")) #Print preguntando por el segundo dato
años_bi = []  # Crea una matriz vacía

if fech1 < fech2:
    print ("Los años biciestos dentro de", fech1, "a", fech2, "son: ") #Print que retorna la fecha y los años biciestos
    
    while fech1 <= fech2:
        if fech1 % 4 ==0 and fech1 % 100 !=0: #Calculo de año biciesto
            años_bi.append(fech1)  # Añade el año a la lista
            
        if fech1 % 100 ==0 and fech1 % 400 ==0: 
            años_bi.append(fech1)  # Añade el año a la lista
        fech1 += 1

    print(años_bi, len(años_bi)) #Imprime en pantalla cuantos años biciestos ha vivido.