

#Ingreso
print("Ingrese los datos correspondientes:")

# Ingreso y almasenaje de los datos correspondientes

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

#validacion de entero en la edad
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("el dato ingresado no es un numero.")

email = input("Ingrese su correo electrónico: ")

#mostrar los datos en forma de tarjeta
#print("hola mundo", nombre, apellido, edad, email)
print("\n----------------------------------------")
print("             TARJETA DE CONTACTO             ")
print("----------------------------------------")
print(f"    Nombre Completo: {nombre} {apellido}")
print(f"        Edad: {edad} años")
print(f"    Correo electrónico: {email}")
print("----------------------------------------")