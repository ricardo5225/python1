"""
numero = 0
while numero < 30:
    numero += 1

    if numero == 15:
        continue

    print("El valor es: " + str(numero)) 


nombre = len("Ricardo")
print("al palabra Ricardo tiene: " + str(nombre) + " Craacteres") a



print("hola {nombre} tienes {edad} años de edad".format(nombre = "Ricardo", edad = 55))


nombre = "Ricardo"
edad = 66
estatura = 1.58

print(f"Su nombre es {nombre}, tienes {edad} y mides {estatura} de estatura")
"""

nombre = "Piero"
apeliidio = "Piña"

nombre = input("Ingrese su nombre: ").lower()
apellido = input("Ingrese su Apellido: ").lower()

if nombre == "Piero" and apellido == "Piña":
    print("Acceso permitido")
elif nombre != "Piero" and apellido != "Piña":
    print(input("nombre para registrarce: "))
    nombre += " "
    print(input("Ingrese su apellido: "))
    apeliidio += " "
    print("Se registro correctamente")
else:
    print("Aceeso denegado")
