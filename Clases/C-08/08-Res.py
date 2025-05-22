#aunque no lo vimos aun, voy a declarar unas funciones para no repetir codigo
#el strip se usa para eliminar espacios en los extremos de un string

# funcionaers esteticas para darle una forma de tarjeta

VARX = 44

def centrar_text(texto):
    return texto.center(VARX - 2)

# funcion para limpiar y formatear strings con minusculas pero la primera mayuscula
def form_string(var_string):
    var_string = var_string.strip()
    if var_string == "" or " " in var_string:
        return "ERROR!"
    return var_string.capitalize()


#Ingreso
print("Ingrese los datos correspondientes o ingrese fin para salir")

# declaracion de array, Ingreso y validación de datos
name_list = []

while True:
    dato_list = []
    nombre = form_string(input("Ingrese su nombre: "))
    if nombre == "Fin":
        break
    while True:
        try:
            precio = int(input("Ingrese el valor del producto: "))
            break
        except ValueError:
            print("el valor es incorrecto!.")
    dato_list = [nombre, precio]
    name_list.append(dato_list)

name_list.sort()
print(name_list)

# mostrar la tarjeta con estilo y ancho de 44asda
print("\n" + "┌" + "─" * (VARX - 2) + "┐")
print(f"|{centrar_text('Lista de Productos')}|")
print("├" + "─" * (VARX - 2) + "┤")
for i in range(0,len(name_list),1):
    nombre = name_list[i][0]
    precio = name_list[i][1]
    texto = f"{i} : {nombre} - ${precio}"
    print(f"|{centrar_text(texto)}|")
print("└" + "─" * (VARX - 2) + "┘")