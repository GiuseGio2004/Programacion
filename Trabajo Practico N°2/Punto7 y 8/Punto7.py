# 7. Un almacén guarda los códigos, los nombres de los productos y sus precios,
# respectivamente, separados por punto y coma ( ; ) en el archivo productos.txt. Hacer
# un algoritmo y luego los procedimientos necesarios que permitan tomar los datos del
# archivo y buscar el precio de un artículo ingresado por teclado. Para probar el
# algoritmo crear un archivo “productos.txt” y cargarle datos al estilo:
# 100;arroz;10
# 102;fideos;5
# 135;lentejas;8
# 138;porotos;6
# 140;sal gruesa;5
# 201;aceite;20 ( etc… )

# Función para leer los productos desde el archivo
def leer_productos(archivo):
    productos = {}
    with open(archivo, 'r') as file:
        for linea in file:
            codigo, nombre, precio = linea.strip().split(';')
            productos[nombre.lower()] = int(precio)
    return productos

# Función para buscar el precio de un producto
def buscar_precio(productos, nombre_producto):
    nombre_producto = nombre_producto.lower()
    return productos.get(nombre_producto, None)

# Función principal
def main():
    # Leer los productos desde el archivo
    archivo = "Productos.txt"
    productos = leer_productos(archivo)
    
    # Solicitar al usuario el nombre del producto
    nombre_producto = input("Ingresa el nombre del producto que deseas buscar: ")
    
    # Buscar el precio del producto
    precio = buscar_precio(productos, nombre_producto)
    
    # Mostrar el resultado
    if precio is not None:
        print(f"El precio de {nombre_producto} es {precio}.")
    else:
        print(f"El producto '{nombre_producto}' no se encuentra en la lista.")

# Llamar a la función principal
if __name__ == "__main__":
    main()