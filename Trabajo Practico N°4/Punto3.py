class Vinoteca:
    __CapacidadMaxima = 5000
    
    def __init__(self):
        # Inicializa cada sección con la capacidad máxima
        self.__cantJugos = self.__CapacidadMaxima
        self.__cantBlancos = self.__CapacidadMaxima
        self.__cantTintosJovenes = self.__CapacidadMaxima
        self.__cantTintosAnejados = self.__CapacidadMaxima
        
    # Reponer productos (llenar cada sección a su capacidad máxima)
    def reponerJugos(self):
        self.__cantJugos = self.__CapacidadMaxima

    def reponerVinosBlancos(self):
        self.__cantBlancos = self.__CapacidadMaxima

    def reponerVinosTintoJoven(self):
        self.__cantTintosJovenes = self.__CapacidadMaxima

    def reponerVinosTintoAnejado(self):
        self.__cantTintosAnejados = self.__CapacidadMaxima

    # Vender productos (si no hay suficiente, vender lo que se pueda)
    def venderJugos(self, unidades: int):
        if unidades > self.__cantJugos:
            vendidas = self.__cantJugos
            self.__cantJugos = 0
            print(f"Solo se vendieron {vendidas} jugos, no había suficiente stock.")
        else:
            self.__cantJugos -= unidades

    def venderVinosBlancos(self, unidades: int):
        if unidades > self.__cantBlancos:
            vendidas = self.__cantBlancos
            self.__cantBlancos = 0
            print(f"Solo se vendieron {vendidas} vinos blancos, no había suficiente stock.")
        else:
            self.__cantBlancos -= unidades

    def venderVinosTintosJovenes(self, unidades: int):
        if unidades > self.__cantTintosJovenes:
            vendidas = self.__cantTintosJovenes
            self.__cantTintosJovenes = 0
            print(f"Solo se vendieron {vendidas} vinos tintos jóvenes, no había suficiente stock.")
        else:
            self.__cantTintosJovenes -= unidades

    def venderVinosTintosAnejados(self, unidades: int):
        if unidades > self.__cantTintosAnejados:
            vendidas = self.__cantTintosAnejados
            self.__cantTintosAnejados = 0
            print(f"Solo se vendieron {vendidas} vinos tintos añejados, no había suficiente stock.")
        else:
            self.__cantTintosAnejados -= unidades

    # Consultas (getters)
    def obtenerCantidadJugos(self) -> int:
        return self.__cantJugos

    def obtenerCantidadVinosBlancos(self) -> int:
        return self.__cantBlancos

    def obtenerCantidadVinosTintosJovenes(self) -> int:
        return self.__cantTintosJovenes

    def obtenerCantidadVinosTintosAnejados(self) -> int:
        return self.__cantTintosAnejados
    
class TesterVinoteca:
    @staticmethod
    def test():
        # Crear una instancia de la vinoteca
        vinoteca = Vinoteca()
        
        # Mostrar las cantidades iniciales (deberían ser 5000 en todas las secciones)
        print("Cantidad inicial de productos:")
        print(f"Jugos: {vinoteca.obtenerCantidadJugos()}")
        print(f"Vinos Blancos: {vinoteca.obtenerCantidadVinosBlancos()}")
        print(f"Vinos Tintos Jóvenes: {vinoteca.obtenerCantidadVinosTintosJovenes()}")
        print(f"Vinos Tintos Anejados: {vinoteca.obtenerCantidadVinosTintosAnejados()}")
        
        # Vender algunos productos
        vinoteca.venderJugos(1000)
        vinoteca.venderVinosBlancos(900)
        vinoteca.venderVinosTintosJovenes(6000)  # Intentar vender más de lo que hay
        vinoteca.venderVinosTintosAnejados(4000)
        
        # Mostrar las cantidades después de la venta
        print("\nCantidad de productos después de la venta:")
        print(f"Jugos: {vinoteca.obtenerCantidadJugos()}")
        print(f"Vinos Blancos: {vinoteca.obtenerCantidadVinosBlancos()}")
        print(f"Vinos Tintos Jóvenes: {vinoteca.obtenerCantidadVinosTintosJovenes()}")
        print(f"Vinos Tintos Anejados: {vinoteca.obtenerCantidadVinosTintosAnejados()}")
        
        # Reponer los productos
        vinoteca.reponerJugos()
        vinoteca.reponerVinosBlancos()
        vinoteca.reponerVinosTintoJoven()
        vinoteca.reponerVinosTintoAnejado()
        
        # Mostrar las cantidades después de reponer
        print("\nCantidad de productos después de reponer:")
        print(f"Jugos: {vinoteca.obtenerCantidadJugos()}")
        print(f"Vinos Blancos: {vinoteca.obtenerCantidadVinosBlancos()}")
        print(f"Vinos Tintos Jóvenes: {vinoteca.obtenerCantidadVinosTintosJovenes()}")
        print(f"Vinos Tintos Anejados: {vinoteca.obtenerCantidadVinosTintosAnejados()}")

if __name__ == "__main__":
    TesterVinoteca.test()