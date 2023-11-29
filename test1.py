#Programa 1 - TIM3 //no ordena la lista, falta poder ingresar 0 para finalizar.

cubo = [] #Lista para guardar numeros ingresados
nums = int(input("\n   ¿Cuantos numeros desea ordenar?: ")) #Ingreso de limite de numeros
vall2 = 0 #Valor inicial de variable
vall3 = 0 #Valor inicial de variable

while nums > 0: #Ciclo while para guardar los valores ingresados
        vall3+=1 #Valor inicial de variable
        vall2 = str(input(f"   {vall3}. Numero: ")) #Ordena la lista de numeros ingresados en pantalla
        cubo.append(vall2) #Agrega los valores al final de la lista
        cubo.sort() #Ordena la lista ingresada
        nums-=1 
print(cubo)#Imprime la lista ingresada