#+------------------+          +---------------------+
#|     Mascota      |          |      Cuidador       |
#|------------------|          |---------------------|
#| - nombre: string |          | - nombre: string    |
#| - especie: string|          | - direccion: string |
#| - edad: int      |          | - telefono: string  |
#| - descripcion: string |     |---------------------|
#| - cuidador: Cuidador |      | + asignarMascota(m: Mascota) |
#|------------------|          | + obtenerMascotas(): list   |
#+------------------+          +---------------------+

class Mascota:
    def __init__(self, nombre, especie, edad, descripcion):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.descripcion = descripcion
        self.cuidador = None  # Inicialmente sin cuidador

    def asignarCuidador(self, cuidador):
        self.cuidador = cuidador

    def __str__(self):
        return f"Mascota: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}, Descripción: {self.descripcion}"

class Cuidador:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.mascotas = []  # Lista de mascotas asignadas al cuidador

    def asignarMascota(self, mascota):
        if mascota not in self.mascotas:
            self.mascotas.append(mascota)
            mascota.asignarCuidador(self)  # Asignar este cuidador a la mascota

    def obtenerMascotas(self):
        return self.mascotas

    def __str__(self):
        return f"Cuidador: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}"

# Clase Tester
def main():
    # Registrar cuidadores
    cuidadores = []
    num_cuidadores = int(input("¿Cuántos cuidadores deseas registrar? "))
    for _ in range(num_cuidadores):
        nombre = input("Nombre del cuidador: ")
        direccion = input("Dirección del cuidador: ")
        telefono = input("Teléfono del cuidador: ")
        cuidador = Cuidador(nombre, direccion, telefono)
        cuidadores.append(cuidador)

    # Registrar mascotas
    mascotas = []
    num_mascotas = int(input("¿Cuántas mascotas deseas registrar? "))
    for _ in range(num_mascotas):
        nombre = input("Nombre de la mascota: ")
        especie = input("Especie de la mascota: ")
        edad = int(input("Edad de la mascota: "))
        descripcion = input("Descripción de la mascota: ")
        mascota = Mascota(nombre, especie, edad, descripcion)
        mascotas.append(mascota)

        # Asignar cuidador a la mascota
        cuidador_nombre = input("Nombre del cuidador para la mascota: ")
        cuidador = next((c for c in cuidadores if c.nombre == cuidador_nombre), None)
        if cuidador:
            cuidador.asignarMascota(mascota)

    # Mostrar mascotas y sus cuidadores
    print("\nLista de mascotas y sus cuidadores:")
    for mascota in mascotas:
        print(mascota)
        if mascota.cuidador:
            print(f"  Cuidador: {mascota.cuidador.nombre}")
        else:
            print("  Sin cuidador asignado")

    # Mostrar cuidadores y sus mascotas
    print("\nLista de cuidadores y sus mascotas asignadas:")
    for cuidador in cuidadores:
        print(cuidador)
        if cuidador.obtenerMascotas():
            for mascota in cuidador.obtenerMascotas():
                print(f"  Mascota: {mascota.nombre}")
        else:
            print("  No tiene mascotas asignadas.")

if __name__ == "__main__":
    main()