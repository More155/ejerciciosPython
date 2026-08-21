"""
PRÁCTICA - UNIDAD 03
Temas: Variables, tipos de datos, entrada/salida, operadores y estructuras condicionales
=========================================================================================

--------------------------------------------------------------
EJERCICIO 1 - Entrada de datos y salida formateada
--------------------------------------------------------------
Escribí un programa que le pida al usuario su nombre y su edad.
Luego mostrá en pantalla el siguiente mensaje:

    ¡Hola, [nombre]! Tienes [edad] años.

Ejemplo:
    Ingresá tu nombre: Ana
    Ingresá tu edad: 22
    ¡Hola, Ana! Tienes 22 años.


--------------------------------------------------------------
EJERCICIO 2 - Figuras geométricas con strings
--------------------------------------------------------------
Imprimí en pantalla las siguientes tres figuras geométricas.
Usá ÚNICAMENTE concatenación (+) y replicación (*) de strings.
No está permitido escribir los caracteres uno por uno a mano.

Figura 1:
+***************+
*               *
*               *
*               *
+***************+

Figura 2:
+---+
|   |
|   |
|   |
+---+

Figura 3:
###################################
###################################
##                               ##
##                               ##
##                               ##
###################################
###################################

Pista: Por ejemplo, para la primera línea de la Figura 1 podés hacer:
    "+" + "*" * 15 + "+"


--------------------------------------------------------------
EJERCICIO 3 - Conversión de tipos y división
--------------------------------------------------------------
Escribí un programa que le pida al usuario dos números enteros.
Convertí ambos números a tipo float y realizá la división entre ellos.
Mostrá el resultado en pantalla.

Ejemplo:
    Ingresá el primer número: 10
    Ingresá el segundo número: 4
    Resultado: 2.5

Nota: ¿Por qué es importante convertir a float antes de dividir?
Investigá qué pasa si dividís dos enteros en Python.


--------------------------------------------------------------
EJERCICIO 4 - Conversión de string a entero
--------------------------------------------------------------
Escribí un programa que le pida al usuario que ingrese un número entero
(que va a llegar como texto desde input()).
Convertí ese texto a entero usando int() y sumale 10.
Mostrá el resultado en pantalla.

Ejemplo:
    Ingresá un número: 25
    El resultado es: 35

Nota: Recordá que input() SIEMPRE devuelve un string, por eso es necesario
convertirlo antes de operar con él.


--------------------------------------------------------------
EJERCICIO 5 - Comparación con un número
--------------------------------------------------------------
Escribí un programa que le pida al usuario un número.
Luego, según el valor ingresado, mostrá uno de estos mensajes:

    - Si es mayor que 10  → "El número es mayor que 10"
    - Si es igual a 10    → "El número es igual a 10"
    - Si es menor que 10  → "El número es menor que 10"

Ejemplo:
    Ingresá un número: 7
    El número es menor que 10


--------------------------------------------------------------
EJERCICIO 6 - Comparación entre dos números
--------------------------------------------------------------
Escribí un programa que le pida al usuario dos números.
Comparalos y mostrá el resultado:

    - Si son iguales     → "Los números son iguales"
    - Si son diferentes  → "Los números son diferentes"

Ejemplo:
    Ingresá el primer número: 5
    Ingresá el segundo número: 8
    Los números son diferentes


--------------------------------------------------------------
EJERCICIO 7 - Mayoría de edad
--------------------------------------------------------------
Escribí un programa que le pida al usuario su edad.
Según el valor ingresado, mostrá:

    - Si tiene 18 años o más → "Eres mayor de edad"
    - Si tiene menos de 18   → "Eres menor de edad"

Ejemplo:
    Ingresá tu edad: 16
    Eres menor de edad


--------------------------------------------------------------
EJERCICIO 8 - Estado del agua
--------------------------------------------------------------
Escribí un programa que le pida al usuario una temperatura en grados Celsius.
Según el valor, mostrá el estado en que se encuentra el agua:

    - Temperatura >= 100  → "El agua está hirviendo"
    - Temperatura <= 0    → "El agua está congelada"
    - En cualquier otro caso → "El agua está en estado líquido"

Ejemplo:
    Ingresá la temperatura en Celsius: 45
    El agua está en estado líquido


--------------------------------------------------------------
EJERCICIO 9 - Positivo, negativo o cero
--------------------------------------------------------------
Escribí un programa que le pida al usuario un número.
Determiná si el número es positivo, negativo o cero y mostrá el mensaje correspondiente:

    - Si es mayor que 0  → "El número es positivo"
    - Si es menor que 0  → "El número es negativo"
    - Si es igual a 0    → "El número es cero"

Ejemplo:
    Ingresá un número: -3
    El número es negativo


--------------------------------------------------------------
EJERCICIO 10 - Día de la semana
--------------------------------------------------------------
Escribí un programa que le pida al usuario un número del 1 al 7.
Mostrá el día de la semana que corresponde a ese número:

    1 → Lunes
    2 → Martes
    3 → Miércoles
    4 → Jueves
    5 → Viernes
    6 → Sábado
    7 → Domingo

Si el usuario ingresa un número fuera del rango 1-7, mostrá:
    "Número de día no válido"

Ejemplo:
    Ingresá un número del 1 al 7: 3
    Miércoles


--------------------------------------------------------------
EJERCICIO 11 - Calculadora básica
--------------------------------------------------------------
Escribí un programa que le pida al usuario dos números.
Luego mostrá los resultados de las cuatro operaciones aritméticas básicas:
suma, resta, multiplicación y división.

Tené en cuenta el siguiente caso especial:
    - Si el segundo número es 0, NO se puede dividir.
      En ese caso, mostrá el mensaje: "No se puede dividir por cero"

Ejemplo:
    Ingresá el primer número: 10
    Ingresá el segundo número: 2
    Suma: 12
    Resta: 8
    Multiplicación: 20
    División: 5.0


--------------------------------------------------------------
EJERCICIO 12 - Calculadora de IMC (Índice de Masa Corporal)
--------------------------------------------------------------
El IMC es un valor que indica si una persona tiene un peso saludable
en relación a su altura. Se calcula con la siguiente fórmula:

    IMC = peso / altura²

Escribí un programa que le pida al usuario:
    - Su peso en kilogramos
    - Su altura en metros

Calculá el IMC y mostrá el resultado junto con su categoría:

    IMC < 18.5              → "Bajo peso"
    18.5 <= IMC < 25        → "Peso normal"
    25 <= IMC < 30          → "Sobrepeso"
    IMC >= 30               → "Obesidad"

Ejemplo:
    Ingresá tu peso (kg): 70
    Ingresá tu altura (m): 1.75
    Tu IMC es: 22.86
    Categoría: Peso normal


--------------------------------------------------------------
EJERCICIO 13 - Conversión de temperatura
--------------------------------------------------------------
Escribí un programa que convierta una temperatura de Celsius a Fahrenheit.
La fórmula de conversión es:

    F = C * 9/5 + 32

Pedile al usuario que ingrese una temperatura en Celsius y mostrá
el resultado en Fahrenheit.

Ejemplo:
    Ingresá la temperatura en Celsius: 100
    La temperatura en Fahrenheit es: 212.0


--------------------------------------------------------------
EJERCICIO 14 - Juego de adivinanza
--------------------------------------------------------------
Escribí un programa que le pida al usuario que adivine un número secreto
que vos (el programador) habrás definido previamente en el código (por ejemplo, el 7).

El número a adivinar debe estar entre 1 y 10.

Según la respuesta del usuario, mostrá:
    - Si adivinó correctamente → "¡Correcto! Adivinaste el número."
    - Si el número ingresado es mayor → "El número secreto es menor. ¡Intentá de nuevo!"
    - Si el número ingresado es menor → "El número secreto es mayor. ¡Intentá de nuevo!"

Ejemplo:
    Adivina el número (entre 1 y 10): 4
    El número secreto es mayor. ¡Intentá de nuevo!


--------------------------------------------------------------
EJERCICIO 15 - Identificación del tipo de dato
--------------------------------------------------------------
Cuando usamos input(), Python siempre nos devuelve un string (texto).
Sin embargo, el usuario pudo haber ingresado algo que representa un número.

Escribí un programa que analice lo que ingresó el usuario y determine
qué tipo de dato representa esa cadena. Seguí estas reglas en orden:

    1. Si todos los caracteres son dígitos (usá isdigit()):
       → "El dato representa un número entero"

    2. Si empieza con "-" y el resto son todos dígitos:
       → "El dato representa un número entero negativo"

    3. Si contiene exactamente un punto "." y, al quitarlo,
       el resto son todos dígitos:
       → "El dato representa un número flotante"

    4. En cualquier otro caso:
       → "El dato representa una cadena de texto"

Ejemplos:
    Entrada: "123"   → El dato representa un número entero
    Entrada: "-45"   → El dato representa un número entero negativo
    Entrada: "3.14"  → El dato representa un número flotante
    Entrada: "hola"  → El dato representa una cadena de texto

Pistas:
    - Usá isdigit() para verificar si una cadena contiene solo dígitos
    - Usá indexación (cadena[0]) para ver el primer carácter
    - Usá el método count(".") para contar cuántos puntos tiene la cadena
    - Usá replace(".", "", 1) para quitar el punto y verificar el resto


--------------------------------------------------------------
EJERCICIO 16 - Calculadora de calificaciones
--------------------------------------------------------------
Escribí un programa que le pida al usuario sus calificaciones en tres materias.
Calculá el promedio de las tres notas y mostrá:

    - El promedio obtenido
    - Si aprobó (promedio >= 6) → "Aprobaste"
    - Si no aprobó (promedio < 6) → "No aprobaste"

Ejemplo:
    Calificación materia 1: 7
    Calificación materia 2: 5
    Calificación materia 3: 8
    Promedio: 6.67
    Aprobaste


--------------------------------------------------------------
EJERCICIO 17 - Concatenación de strings
--------------------------------------------------------------
Escribí un programa que le pida al usuario:
    - Su nombre
    - Su color favorito

Luego, concatená esos datos para formar y mostrar la siguiente oración:

    "Hola [nombre], tu color favorito es [color]."

Ejemplo:
    Ingresá tu nombre: Lucas
    Ingresá tu color favorito: azul
    Hola Lucas, tu color favorito es azul.

"""
