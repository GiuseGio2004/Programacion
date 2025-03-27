class Atleta:
    # Atributos de clase (valores máximos y mínimos predeterminados)
    max_valor = 100
    min_valor = 0

    # Constructor: inicializa el nombre, energía y destreza
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__energia = Atleta.max_valor  # Energía empieza en el valor máximo
        self.__destreza = Atleta.min_valor  # Destreza empieza en el valor mínimo
        self.__entrenamientos_realizados = 0  # Contador de entrenamientos

    # Comando: Entrenar
    def Entrenar(self):
        if self.__energia >= 5:  # Verifica si tiene suficiente energía para entrenar
            self.__energia -= 5  # Reduce la energía en 5 unidades
            self.__entrenamientos_realizados += 1

            # Mejora la destreza cada 5 entrenamientos
            if self.__entrenamientos_realizados % 5 == 0:
                self.__destreza += 1
                print(f"{self.__nombre} ha mejorado su destreza. Nueva destreza: {self.__destreza}")
        else:
            print(f"{self.__nombre} no tiene suficiente energía para entrenar.")

    # Comando: Descansar
    def Descansar(self):
        self.__energia += 20
        if self.__energia > Atleta.max_valor:
            self.__energia = Atleta.max_valor
        print(f"{self.__nombre} ha descansado. Energía actual: {self.__energia}")

    # Consulta: Mismo nivel de destreza que otro atleta
    def mismaDestrezaQue(self, otroAtleta: 'Atleta') -> bool:
        return self.__destreza == otroAtleta.__destreza

    # Consulta: Comparar destreza con otro atleta
    def mayorDestrezaQue(self, otroAtleta: 'Atleta') -> bool:
        return self.__destreza > otroAtleta.__destreza

    # Métodos adicionales (para obtener información del atleta)
    def get_nombre(self):
        return self.__nombre

    def get_energia(self):
        return self.__energia

    def get_destreza(self):
        return self.__destreza
    
class Tester:
    def __init__(self):
        # Crea dos atletas de prueba
        self.atleta1 = Atleta("Juan")
        self.atleta2 = Atleta("Pedro")

    def probar_entrenar_y_descansar(self):
        print("\n--- Iniciando pruebas de Entrenar y Descansar ---")
        # Realiza varios entrenamientos con el atleta1
        for i in range(6):
            print(f"Entrenamiento {i + 1}:")
            self.atleta1.Entrenar()

        # Descanso del atleta1
        self.atleta1.Descansar()

    def probar_comparacion(self):
        print("\n--- Iniciando pruebas de Comparación de Destreza ---")
        # Compara destreza entre atleta1 y atleta2
        if self.atleta1.mismaDestrezaQue(self.atleta2):
            print(f"{self.atleta1.get_nombre()} tiene la misma destreza que {self.atleta2.get_nombre()}.")
        else:
            print(f"{self.atleta1.get_nombre()} no tiene la misma destreza que {self.atleta2.get_nombre()}.")

        # Compara si atleta1 es mejor que atleta2
        if self.atleta1.mayorDestrezaQue(self.atleta2):
            print(f"{self.atleta1.get_nombre()} es mejor que {self.atleta2.get_nombre()}.")
        else:
            print(f"{self.atleta1.get_nombre()} no es mejor que {self.atleta2.get_nombre()}.")

# Ejecución de pruebas
tester = Tester()
tester.probar_entrenar_y_descansar()
tester.probar_comparacion()