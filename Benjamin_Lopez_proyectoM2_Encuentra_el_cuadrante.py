### Programa para encontrar el cuadrante ###
# print explicativo del programa y una bienvenida
print("\tBienvenido, este programa funciona para localizar el cuadrante en el que se encuentran\n\tun par de numeros en el plano cartesiano...\n")
#ciclo que itera hasta que se introduzca un valor flotante o entero para el valor de X
while True:
    try:
        x = float(input("Por favor ingresa un valor para x (Valores negativos y positivos aceptados): "))
        print("\n")
        break
    except (ValueError, TypeError): #no se admiten letras 
        print("\n\t¡Error!: Debes ingresar un numero\n")
#ciclo que itera hasta que se introduzca un valor flotante o entero para el valor de Y
while True:
    try:
        y = float(input("Por favor ingresa el valor para Y: "))
        print("\n")
        break
    except (ValueError, TypeError): # no se admiten letras
        print("\n\t¡Error!: Debes ingresar un numero\n")
#definimos 3 variables "caud" funciona para guardar el valor del cuadrante en el que se encuentran los valores ingresados
cuad = "a"
#dx se reserva para saber en que direccion nos movemos en el eje de X y lo igualamos a una cadena de texto caulquiera en este caso una "a"
dx = "a"
#dy se reserva para saber en que direccion nos movemos en el eje Y y lo igualamos a una cadena de texto caulquiera en este caso una "a"
dy = "a"
#como se especifica en los requerimientos del proyecto no se admite el valos de "0" para ninguna de las entradas X o Y, para eso utilizamos un "if" y con un "or" en conjunto
if x == 0 or y == 0:
    print("\n\tLo sentimos, pero no se admiten ceros, por favor intenta con otro valor (Negativo o positivo)")
    exit()
#para los demas casos en que la entrada no es "0" utilizamos los "elif" y "else" para igualar lso valores de "cuad" "dx" y "dy" segun el caso que aplique
elif x > 0 and y > 0:
    cuad = "Cuadrante I"
    dx = "derecha"
    dy = "arriba"
elif x < 0 and y > 0:
    cuad = "Cuadrante II"
    dx = "izquierda"
    dy = "arriba"
elif x < 0  and y < 0:
    cuad = "Cuadrante III"
    dx = "izquierda"
    dy = "abajo"
else:
    cuad = "Cuadrante IIII"
    dx = "derecha"
    dy = "abajo"

#mostramos un print con los valores ingresados, presisamos la direccion en la que nos movimos en espacios y mostramos el cuadrante en el que nos encontramos
print(f"""Estos son los resultados de tu consulta: El punto en eje X se encuenta a {x} espacios hacia la {dx}
y el punto en el eje Y se encuentra a {y} espacios hacia {dy}
por lo tanto tus coordenadas estan en el {cuad}""")

print("\t\nFin del programa")
