opcion = ""
opcionServicio = ""

rut = ""
nombre = ""
marca = ""
modelo = ""
tiempo = 0
contador = 0
servicios = ""
while opcion != "2":
    print("********************** MENÚ **********************")
    print("1.- Ingreso de automovil")
    print("2.- Salir del menú")
    opcion = input("ingrese la opción correcta: ")

    if opcion == "1":
        contador = 0
        cantidad = 0
        servicios = ""
        print("**** Ingreso de datos del dueño del auto ****")
        rut     = input("Ingrese su rut     : ")
        nombre  = input("Ingrese su nombre  : ")
        marca   = input("Ingrese su marca   : ")
        modelo  = input("Ingrese su modelo  : ")

        while opcionServicio != "7":
            print("1.- Revsión 1000km")
            print("2.- Cambio de aceite")
            print("3.- Revisión frenos")
            print("4.- Revisión correa")
            print("5.- Revisión luces")
            print("6.- Revisión dirección")
            print("7.- Salir ")
            opcionServicio = input ("Seleccione servicio a realizar")

            if opcionServicio == "1":
                print("revisión 1000km")
                tiempo = tiempo + 120 # 2hrs
                contador = contador + 1
                servicios = servicios + "revisión 1000km,"
            elif opcionServicio == "2":
                print("Cambio de aceite")
                tiempo = tiempo + 60 
                contador = contador + 1
                servicios = servicios + "Cambio de aceite,"
            elif opcionServicio == "3":
                print("Revisión frenos")
                tiempo = tiempo + 30
                contador = contador + 1
                servicios = servicios + "Revisión frenos,"
            elif opcionServicio == "4":
                print("Revisión correa")
                tiempo = tiempo + 30
                contador = contador + 1
                servicios = servicios + "Revisión correa,"
            elif opcionServicio == "5":
                print("Revisión luces")
                tiempo = tiempo + 10
                contador = contador + 1
                servicios = servicios + "Revisión luces,"
            elif opcionServicio == "6":
                print("Revisión dirección")
                tiempo = tiempo + 30
                contador = contador + 1
                servicios = servicios + "Revisión dirección,"
        
