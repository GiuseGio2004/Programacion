# 8. Dada una lista con elementos duplicados, crea una nueva lista que contenga solo los
# elementos únicos utilizando list comprehensions

def eliminar_duplicados(lista):
    return list({elemento for elemento in lista})

lista = input("Ingresa una lista de elementos separados por espacios: ").split()
lista_unicos = eliminar_duplicados(lista)
print("La lista con elementos únicos es:", lista_unicos)