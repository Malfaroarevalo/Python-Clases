# ejercicio 3

lab1 = float(input("Ingrese la primera nota de Laboratorio :"))
lab2 = float(input("Ingrese la segunda nota de Laboratorio :"))
lab3 = float(input("Ingrese la tercera nota de Laboratorio :"))
nota1 = float(input("Ingrese la primera nota de Tarea :"))
nota2 = float(input("Ingrese la segunda nota de Tarea :"))
nota3 = float(input("Ingrese la tercera nota de Tarea :"))
sole1 = float(input("Ingrese la primera nota de Solemne :"))
sole2 = float(input("Ingrese la segunda nota de Solemne :"))

proml = (lab1+lab2+lab3)/3
promn = (nota1+nota2+nota3)/3
proms1 = (sole1)
proms2 = (sole2)
prese = (proml*0.15+promn*0.15+proms1*0.35+proms2*0.35)

print("La nota de presentación es :" +str(prese))