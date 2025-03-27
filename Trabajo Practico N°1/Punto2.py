#2. Implemente un programa que a partir del ancho, alto y largo de una habitación
# rectangular calcule cuántos litros de pintura se necesitan para pintarla. Suponiendo
# que 1 litro de pintura sirve para 10m cuadrados y que la habitación tiene sólo una
# puerta de 0,80 de ancho por 2 mts de alto.

ancho = int(input("Ingrese el ancho: "))

alto = int(input("Ingrese el alto: "))

largo = int(input("Ingrese el largo: "))

def calcular_litros_pintura(ancho, alto, largo):
    # Cálculo de las áreas de las paredes
    area_paredes_lado1 = 2 * (alto * ancho)
    area_paredes_lado2 = 2 * (alto * largo)
    
    # Área total de las paredes
    area_total_paredes = area_paredes_lado1 + area_paredes_lado2
    
    # Área de la puerta
    area_puerta = 0.8 * 2
    
    # Área a pintar (total paredes menos la puerta)
    area_a_pintar = area_total_paredes - area_puerta
    
    # Cálculo de los litros de pintura necesarios
    litros_pintura = area_a_pintar / 10
    
    return litros_pintura

# Ejemplo de uso
ancho = float(input("Ingrese el ancho de la habitación en metros: "))
alto = float(input("Ingrese el alto de la habitación en metros: "))
largo = float(input("Ingrese el largo de la habitación en metros: "))

litros = calcular_litros_pintura(ancho, alto, largo)
print(f"Se necesitan {litros:.2f} litros de pintura para pintar la habitación.")