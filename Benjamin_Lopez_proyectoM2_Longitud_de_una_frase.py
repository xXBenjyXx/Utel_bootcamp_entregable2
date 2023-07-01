### Programa para identificar la longitud de una frase ###

print("\t\n Bienvenido usuario... \n ") # Bienvenida al programa

while True: #iniciamos con un ciclo que nos pedira el ingreso de una palabra o frase
    try: # manejamos errores con el "try", "except"
        word = input(("Por favor, ingresa una palabra o frase: "))
        while not word: # mientras el input este vacio mostraremos un error
            print("\t Error!: Debes ingresar por lo menos una palabra. ")
            word = input(str("Por favor ingresa una palabra o frase: ")) # y volveremos a pedir un input.

        if word.isdigit(): # si el usuario ingresa un numero(s) en lugar de letras, mostraremos otro error
            print("\t Error!: no puedes ingresar numeros")

        #el siguiente fragmento de codigo es poco ortodoxo pero no encontraba forma de hacer que el "input" no admitiera un "float"
        elif "." in word: # si el usuario ingresa un punto el programa validara si es un float
            no_num = float(word) # esto lo hara convirtiendo el input en float
            if isinstance(no_num, float): # este if anidado funciona si el usuario ingresa un valor de punto flotante. tambien mostraremos otro error.
                print("\t Error!: no puedes ingresar numeros de punto flotante") # lamentablemente esto hara que la palabra no pueda contener punto final. 
                #si se da el caso esto pasa provocara un error y caeremos en el "except"
        else:
            break # este else rompera el ciclo y continuara con el codigo fuera del while principal

    except (ValueError, TypeError, IndexError): #esta parte del codigo funciona si el usuario provoca algun error de tipo, se le pedira ingresar una palabra de nuevo regresandolo al primer while
        print ("\t ¡Advertencia! La palabra no puede contener puntos ni terminar con punto.\n") # por ejemplo "Juan.Perez" o "Arriba el Atlas. " no se admiten

n = len(word) #validaremos la cantidad de caracteres que tenga el input

option = "palabra" if " " not in word else "frase" # con este if definiremos si se trata de una palabra o si es una frase

if len(word) < 4: # si contiene menos de 4 letras mostraremos una salida que diga si es palabra o frase y cuantas letras faltan
    print(f"\nTe faltan letras. La {option} tiene {n} letras. Debe tener minimo 4 letras ")
elif len(word) >8: # si contiene mas de 8 letras mostraremos una salida que diga si es palabra o frase y cuantas letras sobran
    print(f"\nTe sobran letras. La {option} tiene {n} letras. debe tener maximo 8 letras")
else:
    print(f"\nLa {option} contiene {n} letras, es correcta") # solo se admiten palabras o frases entre 4 y 8 letras. ejemplo: "si claro", "wow no" etc

if " " in word: #si es frase o la palabra contiene espacios se le da a conocer al usuario que el programa reconoce los espacios en blanco como un caracter
    print("(incluyendo espacios)")

print("\n \tfin del programa...") #finalizacion del programa
