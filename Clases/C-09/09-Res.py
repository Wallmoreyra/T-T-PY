VARX = 44

def centrar_text(texto):
    return texto.center(VARX - 2)

# funcion para limpiar y formatear strings con minusculas pero la primera mayuscula
def form_string(var_string):
    var_string = var_string.strip()
    if var_string == "" or " " in var_string:
        return "ERROR!"
    return var_string.capitalize()

# declaracion de array, Ingreso y validación de datos
produc_list = [
    ["coca", 120],
    ["pepsi", 110],
    ["gancia", 90]
]

# Declaracion de funciones
# - FUNCION DE AGREGAR-
def add_produc():
    global produc_list
    # print("se ejecuta la funcion de agregar producto")
    while True:
        nombre = form_string(input("ingrese nombre del producto o ('volver' para cancelar:)"))
        if nombre.lower() == "volver":
            break
        try:
            precio = int(input("Ingrese el precio del producto: "))
            produc_list.append([nombre, precio])
            print("Producto agregado correctamente!\n")
        except ValueError:
            print("Precio inválido. Ingrese nuevamente:")


# - FUNCION DE BORRAR-
def del_produc():
    # print("se ejecuta la funcion de agregar producto")
    global produc_list
    see_producs()
    if not produc_list:
        return
    try:
        nombre = form_string(input("ingrese nombre del producto a eliminar o ('volver' para cancelar:)"))
        if nombre.lower() == "volver":
            return

# Busqueda del producto por nombre:
        for i, product in enumerate(produc_list):
            if product[0].lower() == nombre.lower():
                aux = produc_list.pop(i)
                print(f"Producto '{aux[0]}' borrado exitosamente!")
                return
        
    except ValueError:
        print("nombre no encontrado o ingreso no valido!")


# - FUNCION DE VER-
def see_producs():
    #usamos la variable de manera global
    global produc_list
    if not produc_list:
        print("\n" + "┌" + "─" * (VARX - 2) + "┐")
        print(f"|{centrar_text('No hay productos!')}|")
        print("└" + "─" * (VARX - 2) + "┘")
    else:
        print("\n" + "┌" + "─" * (VARX - 2) + "┐")
        print(f"|{centrar_text('Lista de Productos')}|")
        print("├" + "─" * (VARX - 2) + "┤")
        for i, producto in enumerate(produc_list):
            prod = f"{i}: {producto[0]} - ${producto[1]:.2f}"
            print(f"|{centrar_text(prod)}|")
        print("└" + "─" * (VARX - 2) + "┘")


# creacion del menu
while True:
    # dato_list = []
    # nombre = form_string(input("Ingrese su nombre: "))
    print("1. agregar productos")
    print("2. ver productos")
    print("3. eliminar producto")
    print("4. salir")
    menu = input("opcion: ")
    match menu:
        case "1":
            add_produc()
        case "2":
            see_producs()
        case "3":
            del_produc()
        case "4":
            print("select salir")
            break
        case _:
            print("Opción no válida. Seleccione otra opción:")