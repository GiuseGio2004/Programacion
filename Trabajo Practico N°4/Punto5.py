class MascotaVirtual:
    MAX_VALOR = 100
    MIN_VALOR = 0

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.energia = MascotaVirtual.MAX_VALOR
        self.diversion = MascotaVirtual.MAX_VALOR
        self.higiene = MascotaVirtual.MAX_VALOR
        self.dormido = False
        self.cantActividadesDesgaste = 0

    # Comandos
    def comer(self):
        if not self.dormido:
            self.energia = min(self.energia + 20, MascotaVirtual.MAX_VALOR)
            self.resetearContador()
            print(f"{self.nombre} ha comido. Energía: {self.energia}.")
        else:
            print(f"{self.nombre} está durmiendo y no puede comer.")

    def beber(self):
        if not self.dormido:
            self.energia = min(self.energia + 10, MascotaVirtual.MAX_VALOR)
            self.resetearContador()
            print(f"{self.nombre} ha bebido. Energía: {self.energia}.")
        else:
            print(f"{self.nombre} está durmiendo y no puede beber.")

    def dormir(self):
        self.dormido = True
        self.energia = min(self.energia + 20, MascotaVirtual.MAX_VALOR)
        self.diversion = max(self.diversion - 10, MascotaVirtual.MIN_VALOR)
        self.resetearContador()
        print(f"{self.nombre} está durmiendo. Energía: {self.energia}, Diversión: {self.diversion}.")

    def despertar(self):
        self.dormido = False
        print(f"{self.nombre} se ha despertado.")

    def jugar(self):
        if self.verificarActividadDesgaste():
            self.diversion = min(self.diversion + 40, MascotaVirtual.MAX_VALOR)
            self.energia = max(self.energia - 20, MascotaVirtual.MIN_VALOR)
            self.higiene = max(self.higiene - 15, MascotaVirtual.MIN_VALOR)
            print(f"{self.nombre} ha jugado. Diversión: {self.diversion}, Energía: {self.energia}, Higiene: {self.higiene}.")
        else:
            self.dormir()

    def caminar(self):
        if self.verificarActividadDesgaste():
            self.diversion = min(self.diversion + 20, MascotaVirtual.MAX_VALOR)
            self.energia = max(self.energia - 10, MascotaVirtual.MIN_VALOR)
            self.higiene = max(self.higiene - 8, MascotaVirtual.MIN_VALOR)
            print(f"{self.nombre} ha caminado. Diversión: {self.diversion}, Energía: {self.energia}, Higiene: {self.higiene}.")
        else:
            self.dormir()

    def saltar(self):
        if self.verificarActividadDesgaste():
            self.diversion = min(self.diversion + 10, MascotaVirtual.MAX_VALOR)
            self.energia = max(self.energia - 15, MascotaVirtual.MIN_VALOR)
            self.higiene = max(self.higiene - 10, MascotaVirtual.MIN_VALOR)
            print(f"{self.nombre} ha saltado. Diversión: {self.diversion}, Energía: {self.energia}, Higiene: {self.higiene}.")
        else:
            self.dormir()

    def bañar(self):
        if not self.dormido:
            self.higiene = min(self.higiene + 40, MascotaVirtual.MAX_VALOR)
            self.diversion = max(self.diversion - 10, MascotaVirtual.MIN_VALOR)
            self.resetearContador()
            print(f"{self.nombre} se ha bañado. Higiene: {self.higiene}, Diversión: {self.diversion}.")
        else:
            print(f"{self.nombre} está durmiendo y no puede bañarse.")

    # Consultas
    def obtenerNombre(self):
        return self.nombre

    def obtenerEnergia(self):
        return self.energia

    def obtenerDiversion(self):
        return self.diversion

    def obtenerHigiene(self):
        return self.higiene

    def estaDormido(self):
        return self.dormido

    def obtenerHumor(self):
        if self.energia > 70 and self.diversion > 70 and self.higiene > 70:
            return "Feliz"
        elif self.contarMayoresQue(50, 70) >= 2:
            return "Alegre"
        elif self.contarMayoresQue(30, 50) >= 2:
            return "Neutral"
        elif self.contarMayoresQue(10, 30) >= 2:
            return "Triste"
        elif self.contarMayoresQue(0, 10) >= 2:
            return "Muy Triste"
        else:
            return "Indefinido"

    def estaVivo(self):
        return self.energia > 0

    # Métodos auxiliares
    def verificarActividadDesgaste(self):
        if not self.estaVivo():
            print(f"{self.nombre} ya no está vivo.")
            return False

        if self.dormido:
            print(f"{self.nombre} está durmiendo y no puede realizar esta acción.")
            return False

        if self.cantActividadesDesgaste < 3:
            self.cantActividadesDesgaste += 1
            return True
        else:
            print(f"{self.nombre} ha realizado muchas actividades de desgaste y ahora dormirá.")
            return False

    def resetearContador(self):
        self.cantActividadesDesgaste = 0

    def contarMayoresQue(self, limiteInferior, limiteSuperior):
        estados = [self.energia, self.diversion, self.higiene]
        return sum(limiteInferior < valor <= limiteSuperior for valor in estados)


# Ejemplo de uso
if __name__ == "__main__":
    mascota = MascotaVirtual("Tommy")
    mascota.jugar()
    mascota.caminar()
    mascota.saltar()
    mascota.dormir()
    mascota.despertar()
    mascota.jugar()
    print(f"El humor de {mascota.obtenerNombre()} es: {mascota.obtenerHumor()}")