#aunque no lo vimos aun, voy a declarar unas funciones para no repetir codigo
#el strip se usa para eliminar espacios en los extremos de un string

# funcionaers esteticas para darle una forma de tarjeta

VARX = 44

def centrar_text(texto):
    return texto.center(VARX - 2)

def formater_linea(conten):
    conten = conten.ljust(VARX - 4)
    return f"| {conten} |"


# funcion para limpiar y formatear strings con minusculas pero la primera mayuscula
def form_string(var_string):
    var_string = var_string.strip()
    if var_string == "":
        return "ERROR!"
    return var_string.capitalize()

# funcion para verificar el mail
def form_email(mail):
    mail = mail.strip()
    if mail == "" or " " in mail or mail.count("@") != 1:
        return "ERROR!"
    return mail

# funcion para clasificar por rango etario
def clas_edad(val):
    val = int(val)
    if val == 0:
        return "ERROR!"
    elif 0 < val < 15:
        return  "Niño/a"
    elif 15 <= val <= 18:
        return "Adolecente"
    else:
        return "Adulto"
    

#Ingreso
print("Ingrese los datos correspondientes:")

# Ingreso y validación

nombre = form_string(input("Ingrese su nombre: "))
apellido = input("Ingrese su apellido: ")

#validacion de entero en la edad
while True:
    try:
        edad = clas_edad(int(input("Ingrese su edad: ")))
        break
    except ValueError:
        print("el dato ingresado no es un numero.")

email = form_email(input("Ingrese su correo electrónico: "))


#mostrar los datos en forma de tarjeta original

# print("\n ----------------------------------------")
# print("|            TARJETA DE CONTACTO           |")
# print("|----------------------------------------|")
# print(f"    Nombre Completo: {nombre} {apellido}")
# print(f"        Clas: {edad} ")
# print(f"    Correo electrónico: {email}")
# print("----------------------------------------")

# mostrar la tarjeta con estilo y ancho de 44asda
print("\n" + "-" * VARX)
print(f"|{centrar_text('TARJETA DE CONTACTO')}|")
print("|" + "-" * (VARX - 2) + "|")
print(formater_linea(f"Nombre Completo: {nombre} {apellido}"))
print(formater_linea(f"Clas: {edad}"))
print(formater_linea(f"Correo electrónico: {email}"))
print("-" * VARX)