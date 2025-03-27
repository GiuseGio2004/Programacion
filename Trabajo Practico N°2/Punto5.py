# 5. Escriba un programa que permita cargar una lista de alumnos junto con su nota del
# parcial. Seleccione la estructura de datos que mejor se adapte al problema. Luego
# de ingresados los datos debe generar una lista donde figure si aprobaron o no (se
# aprueba con 40 o más). El listado a mostrar por pantalla debe ser como el siguiente
# (el resultado no se almacena, se calcula):
#   ALUMNOS         PARCIAL     RESULTADO
#   Smith, Juan       70        Aprobado
#   Suárez, María     35        Desaprobado

# Inicializar la lista para almacenar los alumnos y sus notas
alumnos = []

cantidad_alumnos = int(input("Ingresa la cantidad de alumnos: "))

# Cargar los datos de los alumnos
for i in range(cantidad_alumnos):
    nombre = input(f"Ingresa el nombre del alumno {i + 1}: ")
    nota = float(input(f"Ingresa la nota del parcial para {nombre}: "))
    alumnos.append({"nombre": nombre, "nota": nota})

# Mostrar el encabezado de la tabla
print(f"\n{'ALUMNOS':<20}{'PARCIAL':<15}{'RESULTADO':<15}")

# Evaluar si cada alumno aprobó o no, y mostrar los resultados
for alumno in alumnos:
    resultado = "Aprobado" if alumno["nota"] >= 40 else "Desaprobado"
    print(f"{alumno['nombre']:<20}{alumno['nota']:<15}{resultado:<15}")