from datetime import date, timedelta

class Socio:
    def __init__(self, nombre: str, nacimiento: date):
        self.nombre = nombre
        self.fechaNacimiento = nacimiento
        self.fechaPenalizacion = None  # Inicialmente sin penalización
    
    def establecerNombre(self, nombre: str):
        self.nombre = nombre
    
    def establecerFechaPenalizacion(self, fechaHasta: date):
        self.fechaPenalizacion = fechaHasta
    
    def estaHabilitado(self, fecha: date) -> bool:
        if self.fechaPenalizacion is None or self.fechaPenalizacion < fecha:
            return True
        return False
    
    def obtenerNombre(self) -> str:
        return self.nombre
    
    def obtenerFechaNacimiento(self) -> date:
        return self.fechaNacimiento
    
    def obtenerFechaPenalizacion(self) -> date:
        return self.fechaPenalizacion
    
    def __str__(self):
        return f"Socio: {self.nombre}, Nacimiento: {self.fechaNacimiento}, Penalización: {self.fechaPenalizacion}"

class Libro:
    def __init__(self, nombre: str, autor: str, editorial: str, categoria: str):
        self.nombre = nombre
        self.autor = autor
        self.editorial = editorial
        self.categoria = categoria
    
    def obtenerNombre(self) -> str:
        return self.nombre
    
    def obtenerAutor(self) -> str:
        return self.autor
    
    def obtenerEditorial(self) -> str:
        return self.editorial
    
    def obtenerCategoria(self) -> str:
        return self.categoria
    
    def __str__(self):
        return f"Libro: {self.nombre}, Autor: {self.autor}, Editorial: {self.editorial}, Categoría: {self.categoria}"

class Prestamo:
    def __init__(self, libro: Libro, socio: Socio, fechaPrestamo: date, cantDias: int):
        self.libro = libro
        self.socio = socio
        self.fechaPrestamo = fechaPrestamo
        self.cantDias = cantDias
        self.fechaDevolucion = None
    
    def establecerFechaDevolucion(self, fechaDev: date):
        self.fechaDevolucion = fechaDev
        # Verificar penalizaciones
        if self.fechaDevolucion > self.fechaPrestamo + timedelta(days=self.cantDias):
            self.socio.establecerFechaPenalizacion(self.calcularPenalizacion())
    
    def obtenerLibro(self) -> Libro:
        return self.libro
    
    def obtenerFechaPrestamo(self) -> date:
        return self.fechaPrestamo
    
    def obtenerFechaDevolucion(self) -> date:
        return self.fechaDevolucion
    
    def estaAtrasado(self, fechaActual: date) -> bool:
        if self.fechaDevolucion is None and fechaActual > self.fechaPrestamo + timedelta(days=self.cantDias):
            return True
        return False
    
    def calcularPenalizacion(self) -> date:
        # Calcular el atraso en días
        atraso = (self.fechaDevolucion - (self.fechaPrestamo + timedelta(days=self.cantDias))).days
        penalizacion = 0
        
        # Determinar la duración de la penalización según el atraso
        if atraso < 7:
            penalizacion = 3
        elif atraso < 21:
            penalizacion = 5
        else:
            penalizacion = 10
        
        # Duplicar penalización si la categoría del libro es 'A'
        if self.libro.obtenerCategoria() == 'A':
            penalizacion *= 2
        
        return self.fechaDevolucion + timedelta(days=penalizacion)
    
    def __str__(self):
        return f"Préstamo del libro '{self.libro.obtenerNombre()}' por {self.socio.obtenerNombre()} el {self.fechaPrestamo}. Fecha de devolución: {self.fechaDevolucion}"

def test_prestamo():
    # Valores fijos
    socio1 = Socio("Carlos", date(1990, 5, 24))
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Editorial XYZ", 'A')
    
    # Crear un préstamo (prestamo)
    prestamo1 = Prestamo(libro1, socio1, date(2024, 9, 1), 7)
    
    # Entrada del usuario para prueba
    nombre_socio = input("Ingrese el nombre del socio: ")
    nacimiento_socio = date.fromisoformat(input("Ingrese la fecha de nacimiento (YYYY-MM-DD): "))
    socio2 = Socio(nombre_socio, nacimiento_socio)
    
    nombre_libro = input("Ingrese el nombre del libro: ")
    autor_libro = input("Ingrese el autor del libro: ")
    editorial_libro = input("Ingrese la editorial: ")
    categoria_libro = input("Ingrese la categoría del libro (A, B, C): ")
    libro2 = Libro(nombre_libro, autor_libro, editorial_libro, categoria_libro)
    
    fecha_prestamo = date.fromisoformat(input("Ingrese la fecha del préstamo (YYYY-MM-DD): "))
    cantDias = int(input("Ingrese la cantidad de días autorizados para el préstamo: "))
    
    prestamo2 = Prestamo(libro2, socio2, fecha_prestamo, cantDias)
    
    # Simular la devolución del libro después de un retraso
    fecha_devolucion = date.fromisoformat(input("Ingrese la fecha de devolución (YYYY-MM-DD): "))
    prestamo2.establecerFechaDevolucion(fecha_devolucion)
    
    # Resultados
    print(f"El socio {socio2.obtenerNombre()} está habilitado: {socio2.estaHabilitado(fecha_devolucion)}")
    print(f"Detalles del préstamo: {prestamo2}")
    print(f"Fecha de penalización: {socio2.obtenerFechaPenalizacion()}")

# Ejecutar el tester
test_prestamo()