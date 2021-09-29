## condicionales
numero1 = 100
numero2 = 1000

## el numero1 es igual a 100 o es verdadera la afirmación
if numero1 == 100:  # ==  >=  <=  !=  >  <
    print("numero1 es igual a 100")

if numero1 == 101:
    print("numero1 es igual a 100")
    print("numero1 es igual a 100 _ 2")

if numero1 == 100:
    print("numero1 es igual a 100")
    print("numero1 es igual a 100")
else:
    print("numero1 no es igual a 100")
    print("numero1 no es igual a 100")


## ejercicio:
## preguntar al usuario si su edad y señalar si es
## mayor de edad o no

edad = 0
edad = input("¿Cual es su edad?") # input devuelve string
edad = int(edad)

if edad >= 18:
    print("Ud es mayor de edad")
else:
    print("Ud es menor de edad")
