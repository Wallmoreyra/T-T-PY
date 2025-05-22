
# Variables auxiliares, centrado de texto y funcion de menu
menu_opciones = [
    "1. Agregar producto",
    "2. Mostrar productos",
    "3. Buscar producto",
    "4. Eliminar producto",
    "5. Salir"
]

titulo = "Sistema de Gestión Básica De productos "

# Auxiliar de productos para hacer las verificaciones!!
# productos = [
#     ["7UP","Gaseosa",1100],
#     ["Agila","Alfajor",900],
#     ["Coca","Gaseosa",1400],
#     ["Fanta","Gaseosa",1200],
#     ["Fantoche","Alfajor",500],
#     ["Pepsi","Gaseosa",1000],
#     ["Pepsico","Gaseosa sin gas",1400]
# ]

productos = []

def centrar_text(texto, ancho):
    return texto.center(ancho)

# funcion para limpiar y formatear strings con minusculas pero la primera mayuscula
def form_string(var_string):
    var_string = var_string.strip()
    if var_string == "":
        return "ERROR!"
    return var_string.title()

def menu_principal():

    ancho_contenido = max(len(titulo), max(len(op) for op in menu_opciones))
    VARX = ancho_contenido + 10

    print("\n" + "┌" + "─" * (VARX - 2) + "┐")
    print(f"|{centrar_text(titulo, VARX - 2)}|")
    print("├" + "─" * (VARX - 2) + "┤")
    print("|" + " " * (VARX - 2) + "|")

    print("|" + " " * 2 + "┌" + "─" * (VARX - 8) + "┐" + " " * 2 + "|")
    print("|" + " " * 2 + "│" + " " * (VARX - 8) + "│" + " " * 2 + "|")

    for opcion in menu_opciones:
        espacio = (VARX - 6) - len(opcion)
        print("|" + " " * 2 + f"│  {opcion}" + " " * (espacio - 4) + "|" + " " * 2 + "|")

    print("|" + " " * 2 + "│" + " " * (VARX - 8) + "│" + " " * 2 + "|")
    print("|" + " " * 2 + "└" + "─" * (VARX - 8) + "┘" + " " * 2 + "|")

    print("|" + " " * (VARX - 2) + "|")
    print("└" + "─" * (VARX - 2) + "┘")
    return

#-------------------FUNCIOES----------------------------#

def mostrar_tabla(array):
    if not array:
        print("\n" + "┌" + "─" * 40 + "┐")
        print(f"|{centrar_text('No hay productos!', 40)}|")
        print("└" + "─" * 40 + "┘")
        return
    
    # ver
    array_filtrado = isinstance(array[0], tuple)

    if array_filtrado:
        array_productos = [p for _, p in array]
        indices = [i for i, _ in array]
    else:
        array_productos = array
        indices = list(range(len(array)))

    # calculamos los anchos para simular una tabla
    ancho_idx = max(5, len(str(len(indices) - 1)))
    ancho_nombre = max(12, max(len(p[0]) for p in array_productos))
    ancho_categ = max(10, max(len(p[1]) for p in array_productos))
    ancho_precio = max(12, max(len(f"${p[2]:.2f}") for p in array_productos))

    ancho_tot = ancho_idx + ancho_nombre + ancho_categ + ancho_precio + 9

    print("\n" + "┌" + "─" * (ancho_tot + 2) + "┐")
    print(f"|{centrar_text('Lista de Productos', ancho_tot + 2)}|")
    print("├" + "─" * (ancho_tot + 2) + "┤")

    print(f"| {'ÍND':^{ancho_idx}} | {'NOMBRE':^{ancho_nombre}} | {'CATEGORÍA':^{ancho_categ}} | {'PRECIO':^{ancho_precio}} |")
    print("├" + "─" * (ancho_idx + 2) + "┬" + "─" * (ancho_nombre + 2) + "┬" + "─" * (ancho_categ + 2) + "┬" + "─" * (ancho_precio + 2) + "┤")

    for idx, p in zip(indices, array_productos):
        nombre, categoria, precio = p
        print(f"| {idx:^{ancho_idx}} | {nombre:<{ancho_nombre}} | {categoria:<{ancho_categ}} | ${precio:>{ancho_precio - 1}} |")
    print("└" + "─" * (ancho_tot + 2) + "┘")

def mostrar_producto(indice, producto):
    nombre, categoria, precio = producto
    print("\n" + "┌" + "─" * 40 + "┐")
    print(f"| {'Índice: ':<10}{indice:<28} |")
    print(f"| {'Nombre: ':<10}{nombre:<28} |")
    print(f"| {'Categoría: ':<10}{categoria:<27} |")
    print(f"| {'Precio: ':<10}${precio:<27.2f} |")
    print("└" + "─" * 40 + "┘")

def agregar_productos():
    #print("Función: agregar productos")
    global productos
    print("\n Agregar un nuevo producto")
    nombre = form_string(input("Nombre: ").strip())
    categoria = form_string(input("Categoria: ").strip())

    while True:
        precio_str = input("Precio: ").strip()
        if precio_str.replace('.', '', 1).isdigit():
            precio = int(precio_str)
            break
        else:
            print("El ingreso de precio no es válido.")

    nuevo = [nombre, categoria, precio]
    print("\n Producto a agregar: ")
    mostrar_producto(len(productos), nuevo)
    confirmar = input("¿Desea agregar este producto? (s/n): ").strip().lower()
    if confirmar == "s":
        productos.append(nuevo)
        productos.sort(key=lambda x: x[0].lower())
        print("Producto agregado correctamente.")
    else:
        print("Nuevo ingreso de producto cancelado.")

    mostrar_tabla(productos)
    input("Presione Enter para volver al menú...")

def ver_productos():
    #print("Función: ver productos")
    # como en los ejercicios anteriores volvemos a usar la variable global!!
    global productos
    mostrar_tabla(productos)
    input("Presione Enter para volver al menú...")

def buscar_producto():
    #print("Función: buscar producto")
    global productos
    nombre = input("Ingrese el nombre de la busqueda: ").strip().lower()
    resultado = [(i, p) for i, p in enumerate(productos) if nombre in p[0].lower()]
    mostrar_tabla(resultado)
    input("Presione Enter para volver al menú...")

def eliminar_producto():
    #print("Función: eliminar producto")
    global productos

    if not productos:
        print("\n No hay productos para eliminar!")
        input("Presione Enter para volver al menú...")
        return

    mostrar_tabla(productos)

    while True:
        ingreso = input("Ingrese el indice del producto o presione Enter para salir: ").strip()
        if ingreso == "":
            break

        if not ingreso.isdigit():
            print("Ingreso no valido!! ingrese otro numero.")
            continue

        indice = int(ingreso)

        if 0 <= indice < len(productos):
            print("\n Producto a eliminar: ")
            mostrar_producto(indice, productos[indice])
            confirmar = input("¿Seguro quiere borrar este producto? (s/n): ").strip().lower()
            if confirmar == "s":
                productos.pop(indice)
                print("Producto eliminado exitosamente.\n")
                mostrar_tabla(productos)
            else:
                print("Eliminacion cancelada!")
        else:
            print("indice invalido!!")

    input("Presione Enter para volver al menú...")

#-------------------------------------------------------#



#------Codigo del PI------#
while True:
    menu_principal()
    opcion = input("Seleccione una opción: ")
    match opcion:
        case "1":
            agregar_productos()
            #print("select 1")
        case "2":
            ver_productos()
            #print("select 2")
        case "3":
            buscar_producto()
            #print("select 3")
        case "4":
            eliminar_producto()
            #print("select 4")
        case "5":
            print("Saliendo bye bye =)")
            break
        case _:
            print("Opción no válida. Seleccione otra opción:")
