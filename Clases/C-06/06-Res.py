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
print("Ingrese los datos correspondientes o ingrese 1 para salir")

# declaracion de array, Ingreso y validación de datos
name_list = []

while True:
    nombre = form_string(input("Ingrese su nombre: "))
    if nombre == "1":
        break

    name_list.append(nombre)


# print(name_list)

# mostrar la tarjeta con estilo y ancho de 44asda
print("\n" + "┌" + "─" * (VARX - 2) + "┐")
print(f"|{centrar_text('Lista de Nombres')}|")
print("├" + "─" * (VARX - 2) + "┤")
for i in range(0,len(name_list),1):
    print(f"|{centrar_text('Cliente '+ str(i) + ' : ' + name_list[i])}|")
print("└" + "─" * (VARX - 2) + "┘")