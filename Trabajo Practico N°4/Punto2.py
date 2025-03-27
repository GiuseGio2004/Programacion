# Una organización desea mantener información básica sobre sus empleados para 
# calcular los sueldos, para ello diseñó la siguiente clase:

# A)
class Empleado:
    def __init__(self, legajo: int, horasTrabajadasMes: int=0, valorHora: float=0.0):
        self.__legajo = legajo
        self.__horasTrabajadasMes = horasTrabajadasMes
        self.__valorHora = valorHora

    def establecerHorasTrabajadas(self, cantHoras: int):
        self.__horasTrabajadasMes = cantHoras

    def establecerValorHora(self, valorHora: float):
        self.__valorHora = valorHora

    # Consultas (Getters)
    def obtenerLegajo(self) -> int:
        return self.__legajo

    def obtenerHorasTrabajadas(self) -> int:
        return self.__horasTrabajadasMes

    def obtenerValorHora(self) -> float:
        return self.__valorHora

    def obtenerSueldo(self) -> float:
        return self.__horasTrabajadasMes * self.__valorHora
# B)    
class Tester:
    @staticmethod
    def test():
    # Solicitar datos del empleado
        legajo = int(input("Ingrese el número de legajo: "))
        horasTrabajadas = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
        valorHora = float(input("Ingrese el valor de la hora trabajada: "))

    # Crear objeto Empleado
        empleado = Empleado(legajo, horasTrabajadas, valorHora)
        
    # Mostrar resultados
        print(f"Legajo del empleado: {empleado.obtenerLegajo()}")
        print(f"Sueldo calculado: {empleado.obtenerSueldo():.2f}")

if __name__=="__main__":
    Tester.test()
    
# C)
class TesterModificado:
    @staticmethod
    def test():
        # Solicitar datos del empleado
        legajo = int(input("Ingrese el número de legajo: "))
        
        # Crear objeto Empleado usando solo el legajo
        empleado2 = Empleado(legajo)
        
        # Modificar los demás atributos utilizando los métodos
        horasTrabajadas = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
        empleado2.establecerHorasTrabajadas(horasTrabajadas)
        
        valorHora = float(input("Ingrese el valor de la hora trabajada: "))
        empleado2.establecerValorHora(valorHora)
        
        # Mostrar resultados
        print(f"Legajo del empleado: {empleado2.obtenerLegajo()}")
        print(f"Sueldo calculado: {empleado2.obtenerSueldo():.2f}")

if __name__ == "__main__":
    TesterModificado.test()