
# =============================================================================
# PROGRAMACION 1 - UNIDAD 2: Variables, Tipos de Datos y Operaciones
# =============================================================================


# 1. Calcula el area de un rectangulo con base 5 y altura 3.
#    Guarda el resultado en una variable e imprimila.

base = 5
altura = 3

area_rectangulo = base * altura
print("El area del rectangulo es:", area_rectangulo)

# 2. Convierte una temperatura de Celsius a Fahrenheit.
#    Pide al usuario que ingrese la temperatura en Celsius,
#    aplica la formula (C * 9/5) + 32 e imprime el resultado.

input_celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = (input_celsius * 9/5) + 32
print(f"{input_celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

# 3. Pide al usuario su nombre y su edad. Concatenalos en un solo string
#    con un formato como "Me llamo Ana y tengo 20 anios."
#    Luego imprime el texto y su tipo de dato con type().

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
mensaje = print(f"Me llamo {nombre} y mi edad es {edad}.")

# 4. Calcula el area de un circulo con radio 4.
#    Usa 3.14159 como valor de PI. Guarda el resultado e imprimilo.

area_circulo = 3.14159 * (4 ** 2)
print("El area del circulo es:", area_circulo)

# 5. Pide al usuario que ingrese dos numeros enteros.
#    Muestra la suma, resta, multiplicacion y division de esos numeros,
#    cada operacion en una linea separada con una etiqueta clara.
numero1 = int(input("Ingrese el primer numero entero: "))
numero2 = int(input("Ingrese el segundo numero entero: "))

print("Suma:", numero1 + numero2)
print("Resta:", numero1 - numero2)
print("Multiplicacion:", numero1 * numero2)
if numero2 != 0:
    print("Division:", numero1 / numero2)
else:
    print("Division: No se puede dividir por cero")


# 6. Realiza la siguiente operacion: (15 + 5) * 3 - 10 / 2
#    Guarda el resultado en una variable e imprime tanto el resultado
#    como su tipo de dato usando type().
resultado = (15 + 5) * 3 - 10 / 2
print(f"El resultado es {resultado} y el tipo es {type(resultado).__name__}")

# 7. Crea una variable booleana llamada "aprobo" que represente si un alumno
#    aprobo un examen. Asignale el valor True o False segun tu criterio
#    e imprime un mensaje claro indicando el estado del alumno.
aprobo = type(bool)
if True:
    print(f"El alumno aprobo")  

# 8. Calcula el perimetro de un triangulo equilatero con lados de longitud 6.
#    Guarda el resultado en una variable e imprimila con una etiqueta descriptiva.
triangulo_equilatero = 3 * 6
print(f"El perimetro del triangulo es {triangulo_equilatero}")

# 9. Pide al usuario que ingrese su nombre, edad y ciudad de residencia.
#    Imprime cada dato en una linea separada junto con su tipo de dato usando type().
nombre = (str(input("Ingrese su nombre: ")))
edad = (int(input("Ingrese su edad: ")))
ciudad = (str(input("Ingrese su ciudad de residencia: ")))

print(f"Nombre: {nombre}\nEdad: {edad}\nCiudad de residencia: {ciudad}")

# 10. Realiza una operacion matematica que use parentesis, multiplicacion,
#     suma y resta. Guarda el resultado en una variable e imprimila
#     junto con su tipo de dato.

operacion = (2+4) * 36 - 27
print(f"Resultado operacion: {operacion}\nTipo: {type(operacion).__name__}")
# -----------------------------------------------------------------------------
# EJERCICIOS ADICIONALES - Nivel intermedio
# -----------------------------------------------------------------------------


# 11. Pide al usuario que ingrese el precio de un producto y la cantidad
#     que desea comprar. Calcula el total a pagar e imprime el resultado
#     con el mensaje: "El total a pagar es: $___"
precio = (float(input("Ingrese el precio del producto a comprar: ")))
cantidad = (int(input("Ingrese la cantidad del producto a comprar: ")))
if precio and cantidad != 0:
    total = precio * cantidad
    print(f"El total a pagar es: ${total}")
else: print("Debe ingresar un valor mayor a 0")


# 12. Calcula el area y el perimetro de un cuadrado cuyo lado pide al usuario.
#     Imprime ambos resultados con etiquetas claras.
lado = (int(input("Ingrese la longitud del lado del cuadrado: ")))
area = lado * 4
perimetro = lado * lado
if area and perimetro != 0:
    print(f"El area del cuadrado es: {area} y el perimetro: {perimetro}")

# 13. Pide al usuario su nombre y mostralo en pantalla de tres formas distintas:
#     - Todo en mayusculas (usa .upper())
#     - Todo en minusculas (usa .lower())
#     - Con la primera letra en mayuscula (usa .capitalize())
nombre = (str(input("Ingrese su nombre: ")))
print(f"Nombre en mayusculas: {nombre.upper()}")
print(f"Nombre en minusculas: {nombre.lower()}")
print(f"Nombre con la primera letra en mayuscula: {nombre.capitalize()}")

# 14. Pide al usuario que ingrese dos numeros decimales (float).
#     Calcula su promedio e imprime el resultado redondeado a 2 decimales
#     usando la funcion round().
num1 = (float(input("Ingrese un numero decimal: ")))
num2 = (float(input("Ingrese otro numero decimal: ")))
promedio = num1 + num2 /2
print(round(promedio))

# 15. Una pizzeria cobra $1500 por pizza y hace descuento del 10% si se compran
#     3 o mas. Pide al usuario la cantidad de pizzas, calcula el total
#     aplicando el descuento si corresponde, e imprime el precio final.

compra = (int(input("Cuantas pizzas desea comprar?: ")))
pizza = 1500
descuento = pizza - 150
total = (compra * pizza)
total_desc = (compra * descuento)
if compra < 3:
    print(f"El valor es de {total}$")
else:
    print(f"El valor es de {total_desc}$")

# 16. Convierte una cantidad de segundos ingresada por el usuario a horas,
#     minutos y segundos. Por ejemplo: 3750 segundos = 1 hora, 2 minutos, 30 segundos.
#     Imprime el resultado en formato legible.
#     Pista: usa el operador // para division entera y % para el resto.
segundos = (int(input("Ingrese una cantidad de segundos: ")))
horas = segundos // 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos_finales = segundos_restantes % 60
print(f"{segundos} segundos son {horas} horas, {minutos} minutos y {segundos_finales} segundos.")


# 17. Pide al usuario que ingrese la base y la altura de un triangulo.
#     Calcula su area (base * altura / 2) y su perimetro aproximado asumiendo
#     que es un triangulo isoceles (los dos lados iguales = altura * 1.2).
#     Imprime ambos resultados.
base = (int(input("Ingrese la base del triangulo: ")))
altura = (int(input("Ingrese la altura del triangulo: ")))
area = (int(base * altura / 2))
perimetro = (int(altura * 1.2))
print(f"El area del triangulo es {area} y el perimetro es de {perimetro} aproximadamente")

# 18. Pide al usuario su anio de nacimiento. Calcula cuantos anios tiene
#     asumiendo que estamos en 2026. Luego calcula en que anio cumplio o
#     cumplira 18 anios. Imprime ambos resultados con mensajes claros.
anio = (int(input("Ingrese su anio de nacimiento: ")))
edad = 2026 - anio
mayor_edad = anio + 18
if edad >= 18:
    print(f"Edad: {edad}, cumplio 18 anios en {mayor_edad}")
else:
    print(f"Edad: {edad}, cumplira 18 anios en {mayor_edad}")

# 19. Una empresa paga a sus empleados $2000 por hora. Los primeros 8 diarios
#     son normales, las horas extra se pagan al doble.
#     Pide al usuario las horas trabajadas en el dia y calcula el pago total.
#     Imprime el desglose: horas normales, horas extra y total.
horas_normales = 2000
horas_extra = horas_normales * 2
horas_trabajadas = (int(input("Ingrese la cantidad de horas trabajadas: ")))
if horas_trabajadas <= 8:
    pago_total = horas_trabajadas * horas_normales
    print(f"Horas normales: {horas_trabajadas}, horas extra: 0, total a pagar: ${pago_total}")
else:
    horas_extra_trabajadas = horas_trabajadas - 8
    pago_total = (8 * horas_normales) + (horas_extra_trabajadas * horas_extra)
    print(f"Horas normales: 8, horas extra: {horas_extra_trabajadas}, total a pagar: ${pago_total}")


# 20. Pide al usuario que ingrese tres notas de un alumno (pueden ser decimales).
#     Calcula el promedio y determina si aprobo (promedio >= 6).
#     Guarda el resultado en una variable booleana llamada "aprobo".
#     Imprime el promedio redondeado a 1 decimal y el estado del alumno.

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))     
promedio = (nota1 + nota2 + nota3) / 3
aprobo = (bool(promedio >= 6))
print(f"Promedio: {round(promedio, 1)}, Aprobo: {aprobo}")

# =============================================================================
