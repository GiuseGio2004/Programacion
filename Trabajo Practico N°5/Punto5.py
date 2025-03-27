class Especie:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.machos = 0
        self.hembras = 0
        self.ritmo = 0.0

    # Comandos
    def establecerHembras(self, cantHembras: int):
        if cantHembras >= 0:
            self.hembras = cantHembras

    def establecerMachos(self, cantMachos: int):
        if cantMachos >= 0:
            self.machos = cantMachos

    def establecerRitmo(self, ritmo: float):
        self.ritmo = ritmo

    def actualizarHembras(self, cantHembras: int):
        self.hembras = max(0, self.hembras + cantHembras)

    def actualizarMachos(self, cantMachos: int):
        self.machos = max(0, self.machos + cantMachos)

    def actualizarRitmo(self, ritmo: float):
        self.ritmo += ritmo

    # Consultas
    def poblacionActual(self) -> int:
        return self.machos + self.hembras

    def poblacionEstimada(self, anios: int) -> int:
        return int(self.poblacionActual() * (1 + self.ritmo) ** anios)

    def aniosParaPoblacion(self, poblacion: int) -> int:
        anios = 0
        poblacion_actual = self.poblacionActual()
        while poblacion_actual < poblacion:
            anios += 1
            poblacion_actual = int(poblacion_actual * (1 + self.ritmo))
        return anios

    def riesgo(self) -> str:
        if self.ritmo > 0:
            return "verde"
        elif self.ritmo == 0:
            return "amarillo"
        else:
            return "rojo"

    def masHembras(self) -> bool:
        return self.hembras > self.machos

    def mayorRitmo(self, otraEspecie) -> 'Especie':
        return self if self.ritmo > otraEspecie.ritmo else otraEspecie

    def clonar(self) -> 'Especie':
        clon = Especie(self.nombre)
        clon.establecerHembras(self.hembras)
        clon.establecerMachos(self.machos)
        clon.establecerRitmo(self.ritmo)
        return clon

    def toString(self) -> str:
        return f"Especie: {self.nombre}, Machos: {self.machos}, Hembras: {self.hembras}, Ritmo: {self.ritmo:.2f}"
    
import random

class TesterEspecie:
    def __init__(self):
        self.especies = []

    def crearEspecie(self):
        nombre = input("Ingrese el nombre de la especie: ")
        ritmo = float(input("Ingrese el ritmo de crecimiento de la especie: "))
        
        machos = random.randint(0, 100)
        hembras = random.randint(0, 100)
        
        especie = Especie(nombre)
        especie.establecerMachos(machos)
        especie.establecerHembras(hembras)
        especie.establecerRitmo(ritmo)
        
        self.especies.append(especie)

    def mostrarEspecies(self):
        for especie in self.especies:
            print(especie.toString())

    def realizarPruebas(self):
        if not self.especies:
            print("No hay especies registradas.")
            return

        for especie in self.especies:
            print(f"\nPruebas para la especie {especie.nombre}:")
            print(f"Población actual: {especie.poblacionActual()}")
            print(f"Riesgo de extinción: {especie.riesgo()}")
            
            anios = random.randint(1, 10)
            print(f"Población estimada en {anios} años: {especie.poblacionEstimada(anios)}")
            
            poblacion_meta = random.randint(100, 1000)
            print(f"Años para alcanzar una población de {poblacion_meta}: {especie.aniosParaPoblacion(poblacion_meta)}")
            
            print(f"Tiene más hembras que machos: {'Sí' if especie.masHembras() else 'No'}")
            
            otra_especie = random.choice(self.especies)
            mayor_ritmo = especie.mayorRitmo(otra_especie)
            print(f"La especie con mayor ritmo entre {especie.nombre} y {otra_especie.nombre} es: {mayor_ritmo.nombre}")
            
            clon = especie.clonar()
            print(f"Especie clonada: {clon.toString()}")

# Ejemplo de ejecución:
tester = TesterEspecie()
tester.crearEspecie()  # Ingresar nombre y ritmo por el usuario, machos y hembras aleatorios
tester.crearEspecie()  # Crear una segunda especie
tester.mostrarEspecies()
tester.realizarPruebas()