#+--------------------+                          +--------------------+                               +--------------------+            +--------------------+
#|     Atracción      |                          |      Visitante     |                               |      Entrada       |            |   Guía de Aventura |
#|--------------------|                          |--------------------|                               |--------------------|            |--------------------|
#| - nombre: string   |                          | - nombre: string   |                               | - numero: int      |            | - nombre: string   |
#| - tipo: string     |                          | - edad: int        |                               | - fecha: string    |            | - turno: string    |
#| - estaturaMinima: float |                     | - altura: float    |                               | - tipo: string     |            |--------------------|
#| - nivelEmocion: string |                      | - email: string    |                               | - visitante: Visitante |        | + autorizar(v: Visitante, a: Atracción) |
#| - turnos: list     |                          | - entradas: list   |                               |--------------------|            +--------------------+
#|--------------------|                          | - atraccionesAccedidas: list |                     +--------------------+
#| + autorizarIngreso(v: Visitante) |            |--------------------|
#+--------------------+                          | + comprarEntrada(e: Entrada) |
#                                                | + disfrutarAtraccion(a: Atracción) |
#                                                +--------------------+

class Atraccion:
    def __init__(self, nombre, tipo, nivel_de_emocion, estatura_minima, turnos_de_funcionamiento):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel_de_emocion = nivel_de_emocion
        self.estatura_minima = estatura_minima
        self.turnos_de_funcionamiento = turnos_de_funcionamiento

class Visitante:
    def __init__(self, nombre, edad, estatura, correo_electronico):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.correo_electronico = correo_electronico
        self.historial_atracciones = []
        
    def registrar_atraccion(self, atraccion):
        self.historial_atracciones.append(atraccion)
    
    def obtener_historial_atracciones(self):
        return [atr.nombre for atr in self.historial_atracciones]

class Entrada:
    def __init__(self, numero, fecha, tipo, visitante):
        self.numero = numero
        self.fecha = fecha
        self.tipo = tipo
        self.visitante = visitante

class GuiaAventura:
    def __init__(self, nombre, turno_de_trabajo):
        self.nombre = nombre
        self.turno_de_trabajo = turno_de_trabajo
        
    def autorizar_atraccion(self, visitante, atraccion):
        if visitante.estatura >= atraccion.estatura_minima:
            visitante.registrar_atraccion(atraccion)
            return True
        return False
    
def tester():
    # Crear algunas atracciones
    montana_rusa = Atraccion("Montaña Rusa", "Montaña Rusa", "Alto", 1.40, ["mañana", "tarde"])
    casa_embrujada = Atraccion("Casa Embrujada", "Casa Embrujada", "Medio", 1.20, ["noche"])
    
    # Crear un visitante
    visitante1 = Visitante("Juan Pérez", 25, 1.75, "juan.perez@example.com")
    
    # Crear entradas para el visitante
    entrada1 = Entrada(1, "2024-10-02", "General", visitante1)
    
    # Crear un guía de aventura
    guia1 = GuiaAventura("Carlos", "mañana")
    
    # Autorizar al visitante para una atracción
    if guia1.autorizar_atraccion(visitante1, montana_rusa):
        print(f"El visitante {visitante1.nombre} ha ingresado a la atracción {montana_rusa.nombre}.")
    else:
        print(f"El visitante {visitante1.nombre} no cumple con los requisitos para ingresar a {montana_rusa.nombre}.")
    
    # Verificar historial de atracciones del visitante
    print(f"Historial de atracciones de {visitante1.nombre}: {visitante1.obtener_historial_atracciones()}")

# Ejecutar tester
tester()