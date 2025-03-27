class Color:
    # Constructor por defecto: inicializa los valores de rojo, verde y azul en 255 (blanco)
    def __init__(self, rojo=255, verde=255, azul=255):
        self.__rojo = rojo
        self.__verde = verde
        self.__azul = azul

    # Comandos para variar el color
    def variar(self, valor: int):
        self.__rojo = min(255, max(0, self.__rojo + valor))
        self.__verde = min(255, max(0, self.__verde + valor))
        self.__azul = min(255, max(0, self.__azul + valor))

    def variarRojo(self, valor: int):
        self.__rojo = min(255, max(0, self.__rojo + valor))

    def variarVerde(self, valor: int):
        self.__verde = min(255, max(0, self.__verde + valor))

    def variarAzul(self, valor: int):
        self.__azul = min(255, max(0, self.__azul + valor))

    # Comandos para establecer un valor específico para cada color
    def establecerRojo(self, valor: int):
        self.__rojo = min(255, max(0, valor))

    def establecerVerde(self, valor: int):
        self.__verde = min(255, max(0, valor))

    def establecerAzul(self, valor: int):
        self.__azul = min(255, max(0, valor))

    # Consulta para obtener valores de los componentes
    def obtenerRojo(self) -> int:
        return self.__rojo

    def obtenerVerde(self) -> int:
        return self.__verde

    def obtenerAzul(self) -> int:
        return self.__azul

    # Consulta: esRojo() retorna True si el color es completamente rojo
    def esRojo(self) -> bool:
        return self.__rojo == 255 and self.__verde == 0 and self.__azul == 0

    # Consulta: esGris() retorna True si todos los componentes son iguales (gris)
    def esGris(self) -> bool:
        return self.__rojo == self.__verde == self.__azul

    # Consulta: esNegro() retorna True si el color es completamente negro
    def esNegro(self) -> bool:
        return self.__rojo == 0 and self.__verde == 0 and self.__azul == 0

    # Consulta: complemento() retorna el color complemento (R=255-R, G=255-G, B=255-B)
    def complemento(self) -> 'Color':
        return Color(255 - self.__rojo, 255 - self.__verde, 255 - self.__azul)

    # Consulta: esIgualQue(otroColor) retorna True si ambos colores son iguales
    def esIgualQue(self, otroColor: 'Color') -> bool:
        return (self.__rojo == otroColor.obtenerRojo() and
                self.__verde == otroColor.obtenerVerde() and
                self.__azul == otroColor.obtenerAzul())

    # Comando: clonar() retorna un nuevo objeto con los mismos valores
    def clonar(self) -> 'Color':
        return Color(self.__rojo, self.__verde, self.__azul)

    # Comando: copiar otro color en este
    def copiar(self, otroColor: 'Color'):
        self.__rojo = otroColor.obtenerRojo()
        self.__verde = otroColor.obtenerVerde()
        self.__azul = otroColor.obtenerAzul()

# Clase Tester para verificar el comportamiento de la clase Color
class TesterColor:
    def __init__(self):
        # Crear varios colores para pruebas
        self.color1 = Color(255, 0, 0)  # Rojo
        self.color2 = Color(0, 0, 0)    # Negro
        self.color3 = Color(50, 50, 50) # Gris

    def probar_variar(self):
        print("\n--- Pruebas de Variación de Colores ---")
        print(f"Color antes de variar: R={self.color1.obtenerRojo()}, G={self.color1.obtenerVerde()}, B={self.color1.obtenerAzul()}")
        self.color1.variar(-50)
        print(f"Color después de variar: R={self.color1.obtenerRojo()}, G={self.color1.obtenerVerde()}, B={self.color1.obtenerAzul()}")

    def probar_complemento(self):
        print("\n--- Pruebas del Color Complemento ---")
        complemento_color1 = self.color1.complemento()
        print(f"Complemento del color: R={complemento_color1.obtenerRojo()}, G={complemento_color1.obtenerVerde()}, B={complemento_color1.obtenerAzul()}")

    def probar_comparacion(self):
        print("\n--- Pruebas de Comparación de Colores ---")
        if self.color1.esIgualQue(self.color2):
            print(f"Los colores son iguales.")
        else:
            print(f"Los colores no son iguales.")

    def probar_esRojo(self):
        print("\n--- Pruebas de esRojo, esGris y esNegro ---")
        if self.color1.esRojo():
            print("El color es rojo.")
        else:
            print("El color no es rojo.")

        if self.color3.esGris():
            print("El color es gris.")
        else:
            print("El color no es gris.")

        if self.color2.esNegro():
            print("El color es negro.")
        else:
            print("El color no es negro.")

# Ejecución de pruebas
tester = TesterColor()
tester.probar_variar()
tester.probar_complemento()
tester.probar_comparacion()
tester.probar_esRojo()