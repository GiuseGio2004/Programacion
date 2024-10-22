# 12. Escriba un programa que permita el ingreso de números enteros positivos, 
# finalizando el ingreso con 0, y luego indique si 
# la secuencia estaba ordenada de menor a mayor.

numeros = []

while True:
    numero = int(input("Ingrese un número entero positivo (o 0 para finalizar): "))
    
    if numero == 0:
        break
    
    numeros.append(numero) 

if numeros == sorted(numeros):
    print("La secuencia está ordenada de menor a mayor.")
else:
    print("La secuencia no está ordenada de menor a mayor.")