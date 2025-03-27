# 8. El mismo almacén del punto anterior almacena los datos del stock de productos en
# el archivo stock.txt separados por punto y coma ( ; ) con el formato “codigo de
# producto; stock mínimo; stock real”. Escriba un programa, que a partir de
# información contenida en los archivos, genere otro archivo de texto, Compras.txt,
# conteniendo todos los productos cuyo stock se encuentra por debajo del mínimo.
# Utilizar el archivo productos.txt del punto anterior, y crear un archivo stock.txt y
# cargarle datos utilizando los códigos de los productos del archivo anterior. Ej:
# 100;50;60
# 102;50;20
# 135;20;15
# 138;20;20
# 140;10;8
# 201;20;30 ( etc… )

# Función para leer los productos desde el archivo Productos.txt
def leer_productos(archivo_productos):
    productos = {}
    with open(archivo_productos, 'r') as file:
        for linea in file:
            codigo, nombre, precio = linea.strip().split(';')
            productos[codigo] = nombre
    return productos

# Función para leer el stock desde el archivo stock.txt
def leer_stock(archivo_stock):
    stock = []
    with open(archivo_stock, 'r') as file:
        for linea in file:
            codigo, stock_minimo, stock_real = linea.strip().split(';')
            stock.append({
                "codigo": codigo,
                "stock_minimo": int(stock_minimo),
                "stock_real": int(stock_real)
            })
    return stock

# Función para generar el archivo Compras.txt
def generar_archivo_compras(productos, stock, archivo_compras):
    with open(archivo_compras, 'w') as file:
        for item in stock:
            if item["stock_real"] < item["stock_minimo"]:
                nombre_producto = productos.get(item["codigo"], "Desconocido")
                file.write(f"{item['codigo']};{nombre_producto};{item['stock_real']}\n")

# Función principal
def main():
    archivo_productos = "Productos.txt"
    archivo_stock = "Stock.txt"
    archivo_compras = "Compras.txt"

    # Leer los productos y el stock desde los archivos correspondientes
    productos = leer_productos(archivo_productos)
    stock = leer_stock(archivo_stock)

    # Generar el archivo Compras.txt
    generar_archivo_compras(productos, stock, archivo_compras)

    print(f"El archivo {archivo_compras} ha sido generado con éxito.")

# Llamar a la función principal
if __name__ == "__main__":
    main()