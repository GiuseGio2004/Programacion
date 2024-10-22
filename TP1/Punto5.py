#5. Dada una cadena de texto ingresada por consola, 
# decir cuántos “espacios” contiene.

texto = input("ingrese una cadena de texto: ")

cantidad_espacios = texto.count("")

print(f"La cadena contiene {cantidad_espacios} espacios.")