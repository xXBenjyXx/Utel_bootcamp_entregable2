# Utel_bootcamp_entregable2
Proyecto 1: longitud de una frase funciona para saber la longitud de caracteres de una frase corta o una palabra ingresada.

Mostramos un mensaje de bienvenida e iniciamos con un ciclo que nos pedira el ingreso de una palabra o frase
manejamos errores con el "try", "except"
pedimos el ingreso de la palabra o frase mediante un input y lo guardamos en la variable "word"
"while not word" no permitira que el usuario ingrese solo un enter vacio, mientras el input este vacio mostraremos un error
y volveremos a pedir que el usuario ingrese un valor, con esto el input nunca quedara vacio.

si el usuario llegar a teclear un numero entero usaremos un "if word.isdigit()" 
para saber si hay numeros en el input y mostraremos un error
y si el usuario ingresa un valor de punto flotante usaremos un metodo que se me ocurrio durante la marcha:
"elif "." in word" esto validara si hay un punto dentro del input, si es asi el programa intentara 
convertir la variable "word" a tipo "float" para detectar si se ingreso por ejemplo un "2.2"
y mostraremos un error. 

Pero si el usuario llegara a introducir por ejemplo:
"Benjamin.lopez" como hay un punto dentro el input, el programa intentara convertir la variable a tipo float 
y esto provocara un error que le dice al usuario que no puede haber un punto en medio de la palabra 
(lamentablemente tampoco admite que la palabra termine con punto)
la ventaja es que sin punto final la cantidad de letras sera mas precisa.

Si el usuario ingreso un palabra de forma correcta utilizaremos un else para romper el ciclo del "while" principal
y continuaremos con el resto del código. Con "len(word)" contaremos la cantidad de caracteres ingresados 
y lo guardamos en la variable "n". utilizaremos un if para saber si se trata de una palabra 
o frase si es que el usuario presiono la tecla "espacio" y lo guardaremos en la variable "option"

Después validaremos la cantidad de caracteres ingresados si son menos de 4 mostraremos un mensaje que dice:
"te faltan letras la palabra/frase tiene "n" cantidad de letras".
Si por otro lado excede los 8 caracteres mostraremos un mensaje que dice 
"te sobran letras, la palabra/frase tiene n cantidad de letras".
Si lo que se ingreso tiene entre 4 y 8 caracteres mostraremos "La palabra/frase tiene n cantidad de letras, es correcta.

Si cuando el usuario ingreso el input presiono la tecla espacio en el teclado después del mensaje anterior se imprimirá
uno que diga "incluyendo espacios" asi el usuario comprenderá que los espacios también se cuentan como carácter
y por último finalizaremos el programa

 ###################################################################################################################

Proyecto 2: Encuentra el cuadrante. Con este programa ayudaremos al usuario a saber en qué parte del plano cartesiano se encuentran
los valores ingresados.

Primero mostraremos un mensaje de bienvenida explicativo de lo que puede realizar el programa.
Utilizaremos un while con try y except anidados para evitar que el usuario pueda ingresar letras en lugar de números.

Una vez que el usuario ingrese un valor numérico para la variable X romperemos el ciclo
y continuaremos con un segundo While que funciona exactamente igual que el primero pero para el valor de Y. 

Después definimos 3 variables de tipo String para mostrarlas en el mensaje final.
Como se especifica en los requerimientos del proyecto no se admite el valor de "0" para ninguna 
de las entradas X o Y, para eso utilizamos un "if" y con un "or" en conjunto.
Asi si se introduce un 0 el programa mostrara que no es un valor admitido y finalizara. mediante el la función "exit()"
Si el usuario ingresa números enteros o de punto flotante, procederemos a validar mediante if y elif en que parte
del plano cartesiano se encuentra la intersección de los valores ingresados.

Para finalizar, mostramos un print con los valores ingresados, precisaremos la dirección en la que nos movimos en espacios
y mostramos el cuadrante en el que nos encontramos, esto con ayuda de las variables de tipo string previamente declaradas.
y gracias a aplicar formato a la cadena de texto de salida. y mostraremos que el programa ha finalizado.
