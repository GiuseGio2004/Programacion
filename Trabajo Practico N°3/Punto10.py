# 10. Dada una lista de diccionarios que contienen información de estudiantes de una
# materia (nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final) ,
# utilizando list comprehensions:

def ingresar_estudiantes():
    estudiantes = []
    num_estudiantes = int(input("¿Cuántos estudiantes deseas ingresar? "))
    for _ in range(num_estudiantes):
        nombre_apellido = input("Ingresa el nombre y apellido del estudiante: ")
        legajo = input("Ingresa el número de legajo del estudiante: ")
        nota_parcial1 = int(input(f"Ingrese la nota del primer parcial de {nombre_apellido}: "))
        nota_parcial2 = int(input(f"Ingrese la nota del segundo parcial de {nombre_apellido}: "))
        nota_final = int(input(f"Ingrese la nota final de {nombre_apellido}: "))
        estudiante = {
            "nombre_apellido": nombre_apellido,
            "legajo": legajo,
            "nota_parcial1": nota_parcial1,
            "nota_parcial2": nota_parcial2,
            "nota_final": nota_final
        }
        estudiantes.append(estudiante)
    return estudiantes

# a. Crea una lista que contenga los nombres de todos los estudiantes. Salida
# ejemplo: nombres: ['Pepe', 'María', 'Pedro', 'Ana']
def obtener_nombres_estudiantes(estudiantes):
    return [estudiante["nombre_apellido"] for estudiante in estudiantes]

# b. Crea una lista que contenga los nombres de todos los estudiantes que han
# obtenido una calificación superior a 70 en todos los exámenes
def estudiantes_con_notas_superiores(estudiantes, umbral=70):
    return [estudiante["nombre_apellido"] for estudiante in estudiantes if estudiante["nota_parcial1"] > umbral and estudiante["nota_parcial2"] > umbral and estudiante["nota_final"] > umbral]

# c. Crea una lista que contenga los nombres de todos los estudiantes que han
# obtenido una calificación inferior a 60 en al menos un examen
def estudiantes_con_notas_inferiores(estudiantes, umbral=60):
    return [estudiante["nombre_apellido"] for estudiante in estudiantes if estudiante["nota_parcial1"] < umbral or estudiante["nota_parcial2"] < umbral or estudiante["nota_final"] < umbral]

estudiantes = ingresar_estudiantes()

# a. Lista con los nombres de todos los estudiantes
nombres_estudiantes = obtener_nombres_estudiantes(estudiantes)
print("Nombres de todos los estudiantes:", nombres_estudiantes)

# b. Lista con los estudiantes que obtuvieron más de 70 en todos los exámenes
estudiantes_destacados = estudiantes_con_notas_superiores(estudiantes)
print("Estudiantes con notas superiores a 70 en todos los exámenes:", estudiantes_destacados)

# c. Lista con los estudiantes que obtuvieron menos de 60 en al menos un examen
estudiantes_a_mejorar = estudiantes_con_notas_inferiores(estudiantes)
print("Estudiantes con notas inferiores a 60 en al menos un examen:", estudiantes_a_mejorar)