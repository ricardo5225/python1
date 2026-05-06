print("========================")
print("SISTEMA DE CALCULADORA")
print("======================== \n")

print("-Se muestran las siguientes opciones: \n")

print("(opcion 1)-SUMA")
print("(opcion 2)-RESTA")
print("(opcion 3)-MULTIPLICACION")
print("(opcion 4)-DIVISION")
print("(opcion 5)-POTENCIA")

respuesta = int(input("\n-Introduce una Opcion: "))

if respuesta == 1:
    print("\n-SUMA...\n")
    suma1 = int(input("-Ingrese el Primer numero: "))
    suma1 += int(input("-Ingrese el segundo numero: "))
    print("\n -EL RESULTADO DE SUMA ES: " + str(suma1))
elif respuesta == 2: 
    print("\n-RESTA...\n")
    resta1 = int(input("-Ingrese el Primer numero: "))
    resta1 -= int(input("-Ingrese el segundo numero: "))
    print("\n -EL RESULTADO DE RESTA ES: " + str(resta1))
elif respuesta == 3: 
    print("\n-MULPLICACION...\n")
    multi1 = int(input("-Ingrese el Primer numero: "))
    multi1 *= int(input("-Ingrese el segundo numero: "))
    print("\n -EL RESULTADO DE SUMA ES: " + str(multi1))
elif respuesta == 4:
    print("\n-DIVISION...\n")
    divi1 = float(input("-Ingrese el Primer numero: "))
    divi1 /= float(input("-Ingrese el segundo numero: "))
    print("\n -EL RESULTADO DE SUMA ES: " + str(divi1))
elif respuesta == 5:
    print("\n-POTENCIA...")
    pote1 = float(input("-Ingrese el primer numero: "))
    pote1 **= float(input("-Ingrese el segundo numero: "))
    print("\n- EL RESULTADO DE LA POTENCIA ES: " + str(pote1))
else:
    print("Opcion no válida")

