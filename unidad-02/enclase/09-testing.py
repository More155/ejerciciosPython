# ============================================================
# UNIDAD 02 - EJERCICIO DE PRUEBA: FIZZBUZZ
# ============================================================
#
# FizzBuzz es un ejercicio clásico para practicar lo aprendido.
# Para los números del 1 al 100:
#   - Si el número es divisible por 3 Y por 5  -> imprimir "FizzBuzz"
#   - Si es divisible solo por 3               -> imprimir "Fizz"
#   - Si es divisible solo por 5               -> imprimir "Buzz"
#   - En cualquier otro caso                   -> imprimir el número
#
# Conceptos que combinamos en este ejercicio:
#   - Bucle for con range()
#   - Operador módulo (%) para saber si un número es divisible
#   - Estructuras condicionales (if / elif / else)
#   - Operador lógico and
# ============================================================


for i in range(1, 101):
    marca = "FORD"

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

    print(marca, "\n")


print("Hola Mundo")
print(marca)
