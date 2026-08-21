# ============================================================
# UNIDAD 02 - VARIABLES
# ============================================================
#
# Una variable es un NOMBRE que asociamos a un VALOR para
# poder reutilizarlo a lo largo del programa.
#
# Sintaxis:
#   nombre_variable = valor
#
# Reglas para nombrar variables en Python:
#   - Pueden contener letras, números y guion bajo (_).
#   - NO pueden comenzar con un número.
#   - NO pueden ser palabras reservadas del lenguaje
#     (if, for, while, def, class, etc.).
#   - Son SENSIBLES a mayúsculas/minúsculas (edad ≠ Edad).
#   - Por convención se usa snake_case (palabras_separadas_asi).
#
# Para ver la lista completa de palabras reservadas:
#   import keyword
#   print(keyword.kwlist)
# ============================================================


# ------------------------------------------------------------
# 1) Declarar y usar una variable
# ------------------------------------------------------------
nombre = "Juan"
print(nombre)   # Juan


# ------------------------------------------------------------
# 2) Reasignar el valor de una variable
# ------------------------------------------------------------
# El valor de una variable PUEDE CAMBIAR a lo largo del programa.
numero = 20
print(numero)            # 20

numero = numero + 30     # tomamos el valor actual y le sumamos 30
print(numero)            # 50


# ------------------------------------------------------------
# 3) Operar con variables
# ------------------------------------------------------------
numero_uno = 20
numero_dos = 10

# Suma
total = numero_uno + numero_dos
print(total)   # 30

# Resta
total = numero_uno - numero_dos
print(total)   # 10

# Multiplicación
total = numero_uno * numero_dos
print(total)   # 200

# División
total = numero_uno / numero_dos
print(total)   # 2.0

# Potencia (exponente)
total = 2 ** 3
print(total)   # 8

# Módulo (resto de la división)
total = 10 % 3
print(total)   # 1

# División entera
total = 10 // 3
print(total)   # 3


# ------------------------------------------------------------
# 4) Nombres de variables válidos
# ------------------------------------------------------------
# Pueden combinar letras y números, pero NO pueden empezar
# con un número. Sí pueden empezar con guion bajo (_).

ejemplo01 = 10
print(ejemplo01)         # 10

_01_ejemplo = 10         # comenzar con _ es válido
print(_01_ejemplo)       # 10


# ------------------------------------------------------------
# 5) Combinar varias variables en un cálculo
# ------------------------------------------------------------
numero_uno  = 25
numero_dos  = 10
numero_tres = 5.25       # esto es un float

total = numero_uno + numero_dos + numero_tres
print(total)             # 40.25
