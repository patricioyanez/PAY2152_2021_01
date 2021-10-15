if 1 == 1:
    print("uno es igual a uno")


if 2 != 10:
    print("linea 1")
    print("linea 2")
    print("linea 3")
    print("linea 4")
    print("linea 5")
    print("linea 6")

if 12 != 12:
    print("Es verdadero")
else:
    print("Es falso")


edad = input("Ingrese su edad:")
edad = int(edad) # convierte el texto(string) en un numero

if edad <= 12:
    print("es un nin@")
elif edad < 18:
    print("e29s un adolescente")
elif edad <= 29:
    print("es un adulto Joven")
elif edad < 65:
    print("es un adulto")
else:
    print("Ud es mayor de edad")






