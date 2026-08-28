edad = int(input("Ingrese edad: "))

cedula = input("S/N")

if edad >= 18:
    if cedula.upper() == "S":
        print ("Puede casarse")
    else:
        print ("No trae cedula")
else:
    print ("Es menor de edad, no puede casarse")
