#+------------------+                       +---------------------+           +---------------------+
#|     Evento       |                       |    Participante     |           |    Organizador      |
#|------------------|                       |---------------------|           |---------------------|
#| - nombre: string |                       | - nombre: string    |           | - nombre: string    |
#| - fecha: string  |                       | - email: string     |           | - email: string     |
#| - descripcion: string |                  | - telefono: string  |           | - especialidad: string |
#| - organizador: Organizador|              |---------------------|           |---------------------|
#| - participantes: list |                  | + registrarEnEvento(e: Evento)  |  + asignarEvento(e: Evento) |
#|------------------|                       +---------------------+           +---------------------+
#| + asignarOrganizador(o: Organizador) | 
#| + agregarParticipante(p: Participante)|
#|------------------|

class Evento:
    def __init__(self, nombre, fecha, descripcion):
        self.nombre = nombre
        self.fecha = fecha
        self.descripcion = descripcion
        self.organizador = None  # Inicialmente sin organizador
        self.participantes = []  # Lista de participantes en el evento

    def asignarOrganizador(self, organizador):
        self.organizador = organizador

    def agregarParticipante(self, participante):
        if participante not in self.participantes:
            self.participantes.append(participante)

    def __str__(self):
        return f"Evento: {self.nombre}, Fecha: {self.fecha}, Descripción: {self.descripcion}"

class Participante:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def registrarEnEvento(self, evento):
        evento.agregarParticipante(self)

    def __str__(self):
        return f"Participante: {self.nombre}, Email: {self.email}, Teléfono: {self.telefono}"

class Organizador:
    def __init__(self, nombre, email, especialidad):
        self.nombre = nombre
        self.email = email
        self.especialidad = especialidad
        self.eventos = []  # Lista de eventos a cargo del organizador

    def asignarEvento(self, evento):
        self.eventos.append(evento)
        evento.asignarOrganizador(self)

    def __str__(self):
        return f"Organizador: {self.nombre}, Email: {self.email}, Especialidad: {self.especialidad}"

# Clase Tester
def main():
    # Registrar organizadores
    organizadores = []
    num_organizadores = int(input("¿Cuántos organizadores deseas registrar? "))
    for _ in range(num_organizadores):
        nombre = input("Nombre del organizador: ")
        email = input("Email del organizador: ")
        especialidad = input("Especialidad del organizador: ")
        organizador = Organizador(nombre, email, especialidad)
        organizadores.append(organizador)

    # Registrar eventos
    eventos = []
    num_eventos = int(input("¿Cuántos eventos deseas registrar? "))
    for _ in range(num_eventos):
        nombre = input("Nombre del evento: ")
        fecha = input("Fecha del evento: ")
        descripcion = input("Descripción del evento: ")
        evento = Evento(nombre, fecha, descripcion)
        eventos.append(evento)

        # Asignar organizador al evento
        organizador_nombre = input("Nombre del organizador para el evento: ")
        organizador = next((o for o in organizadores if o.nombre == organizador_nombre), None)
        if organizador:
            organizador.asignarEvento(evento)

    # Registrar participantes
    participantes = []
    num_participantes = int(input("¿Cuántos participantes deseas registrar? "))
    for _ in range(num_participantes):
        nombre = input("Nombre del participante: ")
        email = input("Email del participante: ")
        telefono = input("Teléfono del participante: ")
        participante = Participante(nombre, email, telefono)
        participantes.append(participante)

        # Asignar participante a un evento
        evento_nombre = input("Nombre del evento en el que desea participar: ")
        evento = next((e for e in eventos if e.nombre == evento_nombre), None)
        if evento:
            participante.registrarEnEvento(evento)

    # Mostrar eventos, organizadores y participantes
    print("\nLista de eventos, sus organizadores y participantes:")
    for evento in eventos:
        print(evento)
        if evento.organizador:
            print(f"  Organizador: {evento.organizador.nombre}")
        else:
            print("  Sin organizador asignado")
        if evento.participantes:
            for participante in evento.participantes:
                print(f"  Participante: {participante.nombre}")
        else:
            print("  No hay participantes registrados")

    # Mostrar organizadores y eventos a su cargo
    print("\nLista de organizadores y sus eventos:")
    for organizador in organizadores:
        print(organizador)
        if organizador.eventos:
            for evento in organizador.eventos:
                print(f"  Evento: {evento.nombre}")
        else:
            print("  No tiene eventos asignados.")

if __name__ == "__main__":
    main()