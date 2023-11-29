#calculadora
# creamos la clase
class Calculadora:
    # iniciamos con el método __init__
    def __init__(self):
        self.valor1=int(input("Ingrese el primer valor: "))
        self.valor2=int(input("Ingrese el segundo valor: "))
 
    # función para sumar
    def suma(self):
        suma=self.valor1+self.valor2
        print("El resultado de la suma de los valores es: ",suma) 
 
    # función para imprimir
    def imprimir(self):
        print("Los valores son: ")
        print("Valor 1: ",self.valor1)
        print("Valor 2: ",self.valor2)
while True:
    palabra = input("Ingrese una palabra: ")
    if palabra == " ":#termina el programa ingresando los datos entregados
        break 
 
# bloque principal
calcular=Calculadora()
calcular.imprimir()
calcular.suma()