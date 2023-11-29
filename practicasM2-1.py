#programa para encontrar el mayor
x = int (input ('ingresar primer número: '))
y = int (input ('ingresar segundo número: '))
z = int (input ('ingresar tercer número: '))

if x > y and x > z:
    print ('el primer número es el mayor ',x)
else:
    if y > x and y > z:
        print ('el segundo número es el mayor ',y)
    else:
        if z > x and z > y:
            print ('el tercer número es el mayor ',z)

#calculadora
x = int (input ('ingresar primer número: '))
y = int (input ('ingresar segundo número: '))

print ('opción 1 para sumar')
print ('opción 2 para restar')
print ('opción 3 para multiplicar')
print ('opción 4 para dividir')

opcion = int(input('ingresar opción de operación a realizar: '))
if opcion == 1:
    print(x+y)
elif opcion == 2:
    print(x-y)
elif opcion == 3:
    print(x*y)
elif opcion == 4:
    print(x/y)

#recorro string
palabra = input ('ingrese una palabra: ')
for i in range(len(palabra)):
    print(palabra[i])

#comparar
opcion = input('ingresar tu lenguaje de programación preferido: ')
lisLenguaje = ['python','js','java','php']
if opcion in lisLenguaje:
    print('ok, hay coincidencia')
else:
    print('no hay coincidencia')

#password
password=input('ingresar password: ')
while(password!='1234a/j'):
    print('password incorrecta, vuelva a intentar')
    password=input('ingresar password nuevamente: ')
print('password ingresada correctamente')

#trabajando con arreglos
listado = list()
listado = [1,2,'programando',3,4,[5,6,7]]
for i in range(len(listado)):
    print(listado[i])

#agregando
listado.append('agregado')
listado.extend([8,9,10,'otro más'])
for i in range(len(listado)):
    print(listado[i])
listado.insert(3,'insertar')
listado.remove(1)
for i in range(len(listado)):
    print(listado[i])

#concatenando 
a = 10
b = 2.7
c = a+b
palabra = 'cpncatenamos'
texto = 'imprimo el valor de a: '+str(a)
print (texto)
print ('imprimo diferentes variables %i + %.2f = %.3f colocando una palabra almacenada %s'% (a,b,c,palabra))
nombre = 'natalia'
edad = 25
print ('mi nombre es '+nombre+ ' y mi edad es '+str(edad)+ 'años')

#programa para comparar string
name1 = input ('ingresar nombre alumno 1: ')
name2 = input ('ingresar nombre alumno 2: ')
name3 = input ('ingresar nombre alumno 3: ')

if name1 <= name2 and name1 <= name3 and name2 <= name3:
    print ('el nombre del alumno 1 va primero y el nombre 2 va segundo y el nombre 3 va último')
else:
    if name2 <= name1 and name2 <= name3 and name1 <= name3:
        print ('el nombre del alumno 2 va primero y el nombre 1 va segundo y el nombre 3 va último')
    else:
        if name3 <= name1 and name3 <= name2:
            print ('el nombre del alumno 3 va primero')