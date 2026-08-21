# ============================================================
# UNIDAD 02 - LA FUNCIÓN print()
# ============================================================
#
# print() es la función que usamos para mostrar información
# por pantalla (en la consola).
#
# Sintaxis general:
#   print(valor1, valor2, ..., sep=" ", end="\n")
#
# Argumentos importantes:
#   - Podemos pasar uno o varios valores separados por comas.
#   - sep: define el SEPARADOR entre los valores (por defecto " ").
#   - end: define qué se imprime al FINAL (por defecto "\n",
#          que es un salto de línea).
# ============================================================


# ------------------------------------------------------------
# 1) Uso básico
# ------------------------------------------------------------
# Vamos a probar la función print (recordá que esta línea es un comentario)
print("Hola, Python")


# ------------------------------------------------------------
# 2) Caracteres especiales: \n (salto de línea)
# ------------------------------------------------------------
print("Hola mundo!\nHola Python\n")
# Salida en consola:
# Hola mundo!
# Hola Python


# ------------------------------------------------------------
# 3) Múltiples argumentos
# ------------------------------------------------------------
# Se pueden pasar varios valores separados por coma.
# Por defecto, se imprimen separados por un espacio.
print("Hola", "Python")
# Salida en consola:
# Hola Python


# ------------------------------------------------------------
# 4) Argumento end
# ------------------------------------------------------------
# Cambia lo que imprime al final (por defecto es "\n").
print("Hola", end="-")
print("Mundo")
# Salida en consola:
# Hola-Mundo


# ------------------------------------------------------------
# 5) Argumento sep
# ------------------------------------------------------------
# Cambia el separador entre los valores (por defecto es " ").
print("Python", "es", "genial", sep="-")
# Salida en consola:
# Python-es-genial


# ------------------------------------------------------------
# 6) Combinando sep y end
# ------------------------------------------------------------
print("Aprender", "Python", sep="->", end="!!!\n")
# Salida en consola:
# Aprender->Python!!!


# ------------------------------------------------------------
# 7) Ejemplo con varios saludos
# ------------------------------------------------------------
print("Hola mundo", "hola brasil", "hola colombia", "hola venezuela", sep="--", end="\n")
# Salida en consola:
# Hola mundo--hola brasil--hola colombia--hola venezuela


# ------------------------------------------------------------
# 8) Imprimir variables de distintos tipos
# ------------------------------------------------------------
# Valores numéricos
numero_entero  = 10
numero_decimal = 3.1416

# Valores de tipo string (str)
saludo = "Hola, mundo"
letra  = 'A'

print(numero_entero)
print(numero_decimal)
print(saludo)
print(letra)
