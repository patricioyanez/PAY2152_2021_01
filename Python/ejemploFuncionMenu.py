def sumar(numero1, numero2):
    resultado = numero1 + numero2
    print("El resultado de la suma es: ", resultado)
def restar(numero1, numero2):
    resultado = numero1 - numero2
    print("El resultado de la suma es: ", resultado)
def dividir(numero1, numero2):
    if numero2 == 0:
        print("***************** NO SE PUEDE DIVIDIR POR CERO")
        return
    resultado = numero1 + numero2
    print("El resultado de la suma es: ", resultado)
def multiplicar(numero1, numero2):
    resultado = numero1 * numero2
    print("El resultado de la suma es: ", resultado)
# crear 1 funcion para cada operacion del menú, luego llamarlas si el usuario lo solicita :)
opcion = ""
while opcion != "5":
    print("| ****** SUPER CALCULADORA ****** |")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- División")
    print("5.- Salir")
    opcion = input("¿Qué operación desea realizar?:")

    if opcion == "5":
        break

    numero1 = input("Ingrese el primer nro:")
    numero2 = input("Ingrese el segundo nro:")

    numero1 = int(numero1)
    numero2 = int(numero2)
    # opcion  = int(opcion)
    if opcion == "1":
        sumar(numero1, numero2)
    if opcion == "2":
        restar(numero1, numero2)
    if opcion == "3":
        multiplicar(numero1, numero2)
    if opcion == "4":
        dividir(numero1, numero2)
        
    input("....... presione enter para continuar")



