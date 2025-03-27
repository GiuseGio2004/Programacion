# 2. Escriba una función llamada EsBisiesto que permita ingresar un número de año y
# devuelva verdadero en caso que el año sea bisiesto, o falso cuando no lo es. Un año
# es bisiesto si: es divisible entre cuatro y (no es divisible entre 100 o es divisible entre
# 400). Utilizarlo en un programa que permita ingresar dia, 
# mes y año y muestre por pantalla si la fecha es válida o no.

def EsBisiesto(ano):
    return (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)

def es_fecha_valida(dia, mes, ano):
    # Verificar que el año es bisiesto si es necesario
    bisiesto = EsBisiesto(ano)
    
    # Días máximos para cada mes
    dias_por_mes = [31, 29 if bisiesto else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Verificar el rango de mes
    if mes < 1 or mes > 12:
        return False
    
    # Verificar el rango de día según el mes
    if dia < 1 or dia > dias_por_mes[mes - 1]:
        return False
    
    return True

dia = int(input("Ingresa el día: "))
mes = int(input("Ingresa el mes: "))
ano = int(input("Ingresa el año: "))

if es_fecha_valida(dia, mes, ano):
    print(f"La fecha {dia}/{mes}/{ano} es válida.")
else:
    print(f"La fecha {dia}/{mes}/{ano} no es válida.")