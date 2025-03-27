# A)
import random

class Automovil:
    def __init__(self, marca, modelo, año, velocidadMaxima):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidadMaxima = velocidadMaxima
        self.velocidadActual = 0

    # Comandos
    def establecerMarca(self, marca):
        self.marca = marca

    def establecerModelo(self, modelo):
        self.modelo = modelo

    def establecerAnio(self, anio):
        self.año = anio

    def establecerVelocidadMaxima(self, velocidadMax):
        self.velocidadMaxima = velocidadMax

    def establecerVelocidadActual(self, velocidad):
        self.velocidadActual = velocidad

    def acelerar(self, incrementoVelocidad: int):
        if self.velocidadActual + incrementoVelocidad > self.velocidadMaxima:
            self.velocidadActual = self.velocidadMaxima
            print(f"Has alcanzado la velocidad máxima de {self.velocidadMaxima} km/h.")
        else:
            self.velocidadActual += incrementoVelocidad
            print(f"Velocidad actual: {self.velocidadActual} km/h.")

    def desacelerar(self, decrementoVelocidad: int):
        if self.velocidadActual - decrementoVelocidad < 0:
            self.velocidadActual = 0
            print(f"El automóvil se ha detenido.")
        else:
            self.velocidadActual -= decrementoVelocidad
            print(f"Velocidad actual: {self.velocidadActual} km/h.")

    def frenarPorCompleto(self):
        self.velocidadActual = 0
        print("El automóvil se ha detenido por completo.")

    # Consultas
    def obtenerMarca(self):
        return self.marca

    def obtenerModelo(self):
        return self.modelo

    def obtenerAnio(self):
        return self.año

    def obtenerVelocidadMaxima(self):
        return self.velocidadMaxima

    def obtenerVelocidadActual(self):
        return self.velocidadActual

    def calcularMinutosParaLlegar(self, distanciaKM: float):
        if self.velocidadActual == 0:
            print("El auto está detenido y no se puede calcular el tiempo para llegar.")
            return None
        else:
            tiempo_horas = distanciaKM / self.velocidadActual
            tiempo_minutos = tiempo_horas * 60
            print(f"Tiempo estimado para recorrer {distanciaKM} km: {tiempo_minutos:.2f} minutos.")
            return tiempo_minutos
        
# B)
class TesterAutomovil:
    @staticmethod
    def test():
        # Crear una instancia de Automovil
        auto = Automovil("Toyota", "Corolla", 2020, 180)
        
        # Pedir cantidad de iteraciones al usuario
        iteraciones = int(input("Ingrese la cantidad de iteraciones: "))

        for i in range(iteraciones):
            accion = random.randint(0, 3)  # Genera un número entre 0 y 3

            if accion == 0:
                print(f"Iteración {i+1}: velocidad = {auto.obtenerVelocidadActual()}, acelerar(20)")
                auto.acelerar(20)
                print(f"Velocidad actual = {auto.obtenerVelocidadActual()}")

            elif accion == 1:
                print(f"Iteración {i+1}: velocidad = {auto.obtenerVelocidadActual()}, desacelerar(15)")
                auto.desacelerar(15)
                print(f"Velocidad actual = {auto.obtenerVelocidadActual()}")

            elif accion == 2:
                print(f"Iteración {i+1}: frenarPorCompleto()")
                auto.frenarPorCompleto()
                print(f"Velocidad actual = {auto.obtenerVelocidadActual()}")

            elif accion == 3:
                print(f"Iteración {i+1}: calcularMinutosParaLlegar(50)")
                auto.calcularMinutosParaLlegar(50)


if __name__ == "__main__":
    TesterAutomovil.test()

# C)
class TesterAutomovilAleatorio:
    @staticmethod
    def test():
        # Crear una instancia de Automovil
        auto = Automovil("Honda", "Civic", 2021, 200)

        # Pedir cantidad de iteraciones al usuario
        iteraciones = int(input("Ingrese la cantidad de iteraciones: "))

        for i in range(iteraciones):
            accion = random.randint(0, 3)  # Genera un número entre 0 y 3

            if accion == 0:
                incremento = random.randint(5, 50)  # Incremento aleatorio entre 5 y 50
                print(f"Iteración {i+1}: velocidad = {auto.obtenerVelocidadActual()}, acelerar({incremento})")
                auto.acelerar(incremento)
                print(f"Velocidad actual = {auto.obtenerVelocidadActual()}")

            elif accion == 1:
                decremento = random.randint(5, 30)  # Decremento aleatorio entre 5 y 30
                print(f"Iteración {i+1}: velocidad = {auto.obtenerVelocidadActual()}, desacelerar({decremento})")
                auto.desacelerar(decremento)
                print(f"Velocidad actual = {auto.obtenerVelocidadActual()}")

            elif accion == 2:
                print(f"Iteración {i+1}: frenarPorCompleto()")
                auto.frenarPorCompleto()
                print(f"Velocidad actual = {auto.obtenerVelocidadActual()}")

            elif accion == 3:
                distancia = random.randint(10, 100)  # Distancia aleatoria entre 10 y 100 km
                print(f"Iteración {i+1}: calcularMinutosParaLlegar({distancia})")
                auto.calcularMinutosParaLlegar(distancia)
                
if __name__ == "__main__":
    TesterAutomovilAleatorio.test()