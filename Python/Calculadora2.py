opcion = ""
while opcion != "7":
    print("| ****** SUPER CALCULADORA ****** |")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- División")
    print("5.- Potencia")
    print("6.- Raiz")
    print("7.- Salir")
    opcion = input("¿Qué operación desea realizar?:")

    if int(opcion) == 7:
        print("Sistema cerrado")
        break # termina el ciclo while, independiente de la condicion

    numero1 = input("Ingrese el primer nro:")
    numero2 = input("Ingrese el segundo nro:")
    # solo ejecutar la operacion que el usuario solicite

    # conviente el numero que esta como string
    # en tipo de dato numerico
    numero1 = int(numero1)
    numero2 = int(numero2)
    opcion  = int(opcion)
    if opcion == 1:
        resultado = numero1 + numero2
        print("El total de la suma :" , resultado)
    if opcion == 2:
        resultado = numero1 - numero2
        print("El total de la resta:" , resultado)
    if opcion == 3:
        resultado = numero1 * numero2
        print("El total de la multiplicación:" , resultado)
    if opcion == 4:
        if numero2 > 0:
            resultado = numero1 / numero2
            print("El total de la división:" , resultado)
        else:
            print("No se puede dividir por cero")
    if opcion == 5:
        resultado = numero1 ** numero2
        print("El total de la Potencia:" , resultado)
    if opcion == 6:
        resultado = numero1 ** .5
        print("La raíz de numero 1:" , resultado)
        resultado = numero2 ** .5
        print("La raíz de numero 2:" , resultado)

    #print("El total es:" , numero1 + numero2)
    # print("El nro es:", numero1)
