from datetime import date, timedelta

class Fecha:
    # Constructor que inicializa día, mes y año
    def __init__(self, dia: int, mes: int, anio: int):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio

    # Comandos para establecer valores de día, mes y año
    def establecerDia(self, dia: int):
        self.__dia = dia

    def establecerMes(self, mes: int):
        self.__mes = mes

    def establecerAnio(self, anio: int):
        self.__anio = anio

    # Consultas para obtener los valores de día, mes y año
    def obtenerDia(self) -> int:
        return self.__dia

    def obtenerMes(self) -> int:
        return self.__mes

    def obtenerAnio(self) -> int:
        return self.__anio

    # Consulta para comparar si la fecha actual es anterior a otra fecha
    def esAnterior(self, otraFecha: 'Fecha') -> bool:
        fecha_actual = date(self.__anio, self.__mes, self.__dia)
        otra_fecha = date(otraFecha.obtenerAnio(), otraFecha.obtenerMes(), otraFecha.obtenerDia())
        return fecha_actual < otra_fecha

    # Consulta para sumar días a la fecha actual
    def sumaDias(self, cantDias: int) -> 'Fecha':
        fecha_actual = date(self.__anio, self.__mes, self.__dia)
        nueva_fecha = fecha_actual + timedelta(days=cantDias)
        return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)

    # Consulta para obtener el día siguiente
    def diaSiguiente(self) -> 'Fecha':
        return self.sumaDias(1)

    # Consulta para comparar si la fecha actual es igual a otra fecha
    def esIgualQue(self, otraFecha: 'Fecha') -> bool:
        return (self.__dia == otraFecha.obtenerDia() and
                self.__mes == otraFecha.obtenerMes() and
                self.__anio == otraFecha.obtenerAnio())

# Clase Tester para verificar el comportamiento de Fecha
class TesterFecha:
    def __init__(self):
        # Crear dos fechas para pruebas
        self.fecha1 = Fecha(16, 9, 2024)
        self.fecha2 = Fecha(15, 9, 2023)

    def probar_comparaciones(self):
        print("\n--- Pruebas de Comparación ---")
        if self.fecha1.esAnterior(self.fecha2):
            print(f"{self.fecha1.obtenerDia()}/{self.fecha1.obtenerMes()}/{self.fecha1.obtenerAnio()} es anterior a {self.fecha2.obtenerDia()}/{self.fecha2.obtenerMes()}/{self.fecha2.obtenerAnio()}")
        else:
            print(f"{self.fecha1.obtenerDia()}/{self.fecha1.obtenerMes()}/{self.fecha1.obtenerAnio()} no es anterior a {self.fecha2.obtenerDia()}/{self.fecha2.obtenerMes()}/{self.fecha2.obtenerAnio()}")

        if self.fecha1.esIgualQue(self.fecha2):
            print(f"Las fechas son iguales.")
        else:
            print(f"Las fechas no son iguales.")

    def probar_suma_dias(self):
        print("\n--- Prueba de Suma de Días ---")
        nueva_fecha = self.fecha1.sumaDias(10)
        print(f"Sumar 10 días a {self.fecha1.obtenerDia()}/{self.fecha1.obtenerMes()}/{self.fecha1.obtenerAnio()} da como resultado {nueva_fecha.obtenerDia()}/{nueva_fecha.obtenerMes()}/{nueva_fecha.obtenerAnio()}")

    def probar_dia_siguiente(self):
        print("\n--- Prueba de Día Siguiente ---")
        dia_siguiente = self.fecha1.diaSiguiente()
        print(f"El día siguiente a {self.fecha1.obtenerDia()}/{self.fecha1.obtenerMes()}/{self.fecha1.obtenerAnio()} es {dia_siguiente.obtenerDia()}/{dia_siguiente.obtenerMes()}/{dia_siguiente.obtenerAnio()}")

# Ejecución de pruebas
tester = TesterFecha()
tester.probar_comparaciones()
tester.probar_suma_dias()
tester.probar_dia_siguiente()