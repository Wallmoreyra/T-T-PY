#aunque no lo vimos aun, voy a declarar unas funciones para no repetir codigo
#el strip se usa para eliminar espacios en los extremos de un string

# funcionaers esteticas para darle una forma de tarjeta

VARX = 44

def centrar_text(texto):
    return texto.center(VARX - 2)


# funcion para limpiar y formatear strings con minusculas pero la primera mayuscula
def form_string(var_string):
    var_string = var_string.strip()
    if var_string == "":
        return "ERROR!"
    return var_string.capitalize()


#Ingreso
print("Ingrese los datos correspondientes:")

# Ingreso y validación
cant_mes = 0
nombre = form_string(input("Ingrese nombre del cliente: "))
cant_mes = int(input("Ingrese cantidad de meses: "))

#validacion de ingresos mensualisado del cliente

ingre_total = 0

for i in range(0,cant_mes,1):
    while True:
        try:
            val_mensual = int(input('ingreso mes ' + str(i + 1) + " : "))
            break
        except ValueError:
            print("el dato ingresado no es valido!")
    ingre_total = ingre_total + val_mensual


# mostrar la tarjeta con estilo y ancho de 44asda
print("\n" + "┌" + "─" * (VARX - 2) + "┐")
print(f"|{centrar_text('Acumulado mensual')}|")
print(f"|{centrar_text('Cliente: ' + nombre)}|")
print("├" + "─" * (VARX - 2) + "┤")
#print(formater_linea(f"Nombre Completo: {nombre} {apellido}"))
print(f"|{centrar_text('Ingreso total:')}|")
print(f"|{centrar_text('$' + str(ingre_total))}|")
print("└" + "─" * (VARX - 2) + "┘")