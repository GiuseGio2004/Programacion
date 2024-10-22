# 3. Extienda el programa anterior para permitir múltiple cantidad de “manos” de pintura.

def calcular_litros_pintura(ancho, alto, largo, manos):
    # Cálculo de las áreas de las paredes
    area_paredes_lado1 = 2 * (alto * ancho)
    area_paredes_lado2 = 2 * (alto * largo)
    
    # Área total de las paredes
    area_total_paredes = area_paredes_lado1 + area_paredes_lado2
    
    # Área de la puerta
    area_puerta = 0.8 * 2
    
    # Área a pintar (total paredes menos la puerta)
    area_a_pintar = area_total_paredes - area_puerta
    
    # Cálculo de los litros de pintura necesarios por una mano
    litros_pintura_por_mano = area_a_pintar / 10
    
    # Cálculo de los litros de pintura necesarios para todas las manos
    litros_pintura_total = litros_pintura_por_mano * manos
    
    return litros_pintura_total

# Ejemplo de uso
ancho = float(input("Ingrese el ancho de la habitación en metros: "))
alto = float(input("Ingrese el alto de la habitación en metros: "))
largo = float(input("Ingrese el largo de la habitación en metros: "))
manos = int(input("Ingrese la cantidad de manos de pintura: "))

litros = calcular_litros_pintura(ancho, alto, largo, manos)
print(f"Se necesitan {litros:.2f} litros de pintura para pintar la habitación con {manos} manos.")