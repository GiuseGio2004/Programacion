#Realizar un programa que pida los tres lados de un triángulo e indique el tipo de
# triángulo que es según sus lados: Equilátero (tres lados iguales), Isósceles (dos
# lados iguales) o Escaleno (tres lados distintos).

lado1 = float(input("Ingrese el primer lado: "))

lado2 = float(input("Ingrese el segundo lado: "))

lado3 = float(input("Ingrese el tercer lado: "))

if lado1 == lado2 and lado2 == lado3:
    print("El triángulo es equilátero.")

if lado1 == lado2 and lado2 != lado3:
    print("El triángulo es isósceles.")

if lado1 != lado2 and lado2 != lado3:
    print("El triángulo es escaleno.")