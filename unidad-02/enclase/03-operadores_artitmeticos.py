# ============================================================
# UNIDAD 02 - OPERADORES ARITMÉTICOS
# ============================================================
#
# Python ofrece los siguientes operadores aritméticos:
#
#   +    Suma
#   -    Resta
#   *    Multiplicación
#   /    División              (siempre devuelve un float)
#   //   División entera       (descarta los decimales)
#   %    Módulo / Resto        (devuelve el resto de la división)
#   **   Potencia              (exponente)
#
# También existen los operadores de asignación compuesta
# (+=, -=, *=, /=, //=, %=, **=) que combinan una operación
# aritmética con la asignación.
# ============================================================


# ------------------------------------------------------------
# 1) Operaciones básicas
# ------------------------------------------------------------
resultado = 10 + 5
print(resultado)   # 15

resultado = 10 - 5
print(resultado)   # 5

resultado = 10 * 5
print(resultado)   # 50

resultado = 10 / 4
print(resultado)   # 2.5  (división normal: devuelve float)

resultado = 10 // 4
print(resultado)   # 2    (división entera: descarta decimales)

resultado = 10 % 3
print(resultado)   # 1    (resto de dividir 10 entre 3)

resultado = 2 ** 3
print(resultado)   # 8    (2 elevado a la 3)


# ------------------------------------------------------------
# 2) Operadores de asignación compuesta
# ------------------------------------------------------------
# Permiten escribir operaciones como x = x + 2 de forma más corta.

x = 10
x = x + 2
print(x)   # 12

# La línea anterior puede simplificarse así:
x += 2     # equivalente a x = x + 2
print(x)   # 14

# Lo mismo aplica para -=, *=, /=, //=, %=, **=


# ------------------------------------------------------------
# 3) Ejemplo aplicado: cálculo de subtotal y total
# ------------------------------------------------------------
numero_uno    = 5
numero_dos    = 50
numero_tres   = 2
numero_cuatro = 30

# Suma de los primeros dos valores
subtotal = numero_uno + numero_dos

# Sumamos al subtotal los demás valores para obtener el total
total = subtotal + numero_tres + numero_cuatro

print("Subtotal:", subtotal)   # Subtotal: 55
print("Total:",    total)      # Total: 87


# ------------------------------------------------------------
# 4) Palabras reservadas del lenguaje
# ------------------------------------------------------------
# Python tiene palabras que no se pueden usar como nombres
# de variables porque están reservadas para el lenguaje.
# Podemos verlas con el módulo keyword.

import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break',
#  'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
#  'finally', 'for', 'from', 'global', 'if', 'import', 'in',
#  'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
#  'return', 'try', 'while', 'with', 'yield']
