# 4. Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo 
# las palabras que comienzan con una letra específica (por ejemplo, "a") indicada por 
# el usuario, utilizando list comprehensions.

def filtrar_palabras_por_letra(diccionario, palabras_usuario, letra):
    return [palabra for palabra in palabras_usuario if palabra in diccionario and palabra.startswith(letra)]

# Ejemplo de uso:
diccionario = {
    "amor": "Sentimiento de afecto hacia una persona, animal o cosa.",
    "amistad": "Relación de afecto, simpatía y confianza entre personas.",
    "animal": "Ser vivo que se puede mover por sí mismo.",
    "arbol": "Planta perenne con un tronco leñoso.",
    "casa": "Edificio destinado a ser habitado."
}

palabras_usuario = input("Ingresa una lista de palabras separadas por espacios: ").split()
letra = input("Ingresa la letra con la que deben comenzar las palabras: ").lower()

palabras_filtradas = filtrar_palabras_por_letra(diccionario, palabras_usuario, letra)
print("Las palabras que comienzan con", letra, "y están en el diccionario son:", palabras_filtradas)