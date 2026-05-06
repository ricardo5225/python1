print("SISTEMA DE DIA DE VACACIONES")

print("Areas de la empresa: ")

area1 = print("-(Clave 1) Departamento de Atencion al Cliente")
area2 = print("-(Clave 2) Departamento de Logistica")
area3 = print("-(Clave 3) Departamneto de Gerencia")

ingreso = int(input("Ingrese numero de Clave: "))

if ingreso == 1:
    print("- Departamento de atencion al Cliente- \n")
    años1 = int(input("¿cuanto años de servicio tiene en la empresa?: "))
    if años1 == 1:
        print("Usted tiene 6 dias de vacaciones")
    elif años1 <= 6:
        print("Usted tiene 14 dias de vacaciones")
    elif años1 >= 7:
        print("Usted tiene 20 dias de vacaciones")
elif ingreso == 2: 
    print("Departamento de Logistica")
    años2 = int(input("¿Cuantos años de servicio tiene en la Empresa?: "))
    if años2 == 1:
        print("Usted tiene 15 dias de vacaciones")
    elif años2 <= 6:
        print("Usted tiene 15 dias de vacaciones")
    elif años2 >= 7:
        print("Usted tiene 22 dias de vacaciones")
elif ingreso == 3:
    print("Departamento de Gerencia")
    años3 = int(input("¿Cuantos años de servicio tiene en la Empresa? : "))         
    if años3 == 1:
        print("Usted tiene 10 de vacaciones")
    elif años3 <= 6:
        print("Usted tiene 20 de vacaciones")
    elif años3 >= 7:
        print("Usted tiene 30 dias de vcaciones")
else:
    print("CLAVE NO REGISTRADA")
