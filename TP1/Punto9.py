# Se desea realizar una aplicación que solicite al usuario tres números enteros
# positivos (A, B, y X), y que muestre por pantalla todos los múltiplos de X que estén
# entre A y B inclusive. 

A = int(input("Ingrese el valor de A (inicio del rango): "))
B = int(input("Ingrese el valor de B (fin del rango): "))
X = int(input("Ingrese el valor de X (múltiplo): "))

if A > 0 and B > 0 and X > 0 and A <= B:
    print(f"Los múltiplos de {X} entre {A} y {B} son:")
    for i in range(A, B + 1):
        if i % X == 0:
            print(i, end=" ")
else:
    print("Por favor, asegúrese de que A, B y X sean números positivos y que A sea menor o igual que B.")