# menu
opcion = ""
while opcion != "4":
    print("********************** MENÚ **********************")
    print("1.- ingrese su edad")
    print("2.- ingrese su nombre")
    print("3.- ingrese dirección")
    print("4.- Salir del menú")
    opcion = input("ingrese la opción correcta: ")

    # si usuario presiona el 1
    if(opcion == "1"):
        edad = input("su edad es: ")
        if(int(edad)>=18):
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

    if(opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4"):
        print("Opcion no válida!!!")


# Ejercicios: Imprimir numeros del 1 al que señale el usuario


numero = input("Ingrese numero a mostrar: ")
numero = int(numero)
contador = 0
while(contador < numero):
    contador = contador + 1
    print(contador)