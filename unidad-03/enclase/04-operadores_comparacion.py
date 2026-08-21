# =============================================================================
# OPERADORES DE COMPARACIÓN EN PYTHON
# =============================================================================
# Los operadores de comparación se usan para comparar dos valores.
# El resultado de una comparación SIEMPRE es un valor booleano: True o False.
#
# Operadores disponibles:
#   ==   igual a
#   !=   distinto de
#   >    mayor que
#   <    menor que
#   >=   mayor o igual que
#   <=   menor o igual que
#
# Se pueden comparar números Y strings.
# Al comparar strings, Python usa el orden del alfabeto (orden Unicode).
# =============================================================================


# -----------------------------------------------------------------------------
# 1. IGUAL A  (==)
# -----------------------------------------------------------------------------
# Devuelve True si ambos valores son exactamente iguales.

print("--- Igual a (==) ---")
print(5 == 5)           # True
print(5 == 3)           # False
print("abc" == "abc")   # True
print("ABC" == "abc")   # False  ← mayúsculas y minúsculas son distintas


# -----------------------------------------------------------------------------
# 2. DISTINTO DE  (!=)
# -----------------------------------------------------------------------------
# Devuelve True si los valores son diferentes.

print("\n--- Distinto de (!=) ---")
print(5 != 3)           # True
print(5 != 5)           # False
print("abc" != "ABC")   # True


# -----------------------------------------------------------------------------
# 3. MAYOR QUE  (>)
# -----------------------------------------------------------------------------
# Devuelve True si el valor de la izquierda es mayor que el de la derecha.

print("\n--- Mayor que (>) ---")
print(5 > 3)            # True
print(3 > 5)            # False
print("b" > "a")        # True  ← en el alfabeto, "b" va después de "a"


# -----------------------------------------------------------------------------
# 4. MENOR QUE  (<)
# -----------------------------------------------------------------------------
# Devuelve True si el valor de la izquierda es menor que el de la derecha.

print("\n--- Menor que (<) ---")
print(3 < 5)            # True
print(5 < 3)            # False
print("a" < "b")        # True


# -----------------------------------------------------------------------------
# 5. MAYOR O IGUAL QUE  (>=)
# -----------------------------------------------------------------------------
# Devuelve True si el valor de la izquierda es mayor O igual al de la derecha.

print("\n--- Mayor o igual que (>=) ---")
print(5 >= 5)           # True   ← son iguales, también cumple
print(5 >= 3)           # True
print(3 >= 5)           # False


# -----------------------------------------------------------------------------
# 6. MENOR O IGUAL QUE  (<=)
# -----------------------------------------------------------------------------
# Devuelve True si el valor de la izquierda es menor O igual al de la derecha.

print("\n--- Menor o igual que (<=) ---")
print(3 <= 5)           # True
print(5 <= 5)           # True   ← son iguales, también cumple
print(5 <= 3)           # False


# -----------------------------------------------------------------------------
# 7. GUARDAR EL RESULTADO EN UNA VARIABLE
# -----------------------------------------------------------------------------
# El resultado True/False se puede guardar en una variable booleana.

condicion = (10 == 10)
print("\n¿10 == 10?", condicion)        # True

condicion = (5 > 8)
print("¿5 > 8?", condicion)            # False


# -----------------------------------------------------------------------------
# 8. COMPARACIÓN COMBINADA CON OPERACIONES ARITMÉTICAS
# -----------------------------------------------------------------------------
# Primero se resuelve la operación aritmética, luego se compara.

resultado = (2 + 3) > 4     # Primero: 2+3=5, luego: ¿5 > 4? → True
print("\n¿(2 + 3) > 4?", resultado)     # True

resultado = (10 - 6) == 3   # Primero: 10-6=4, luego: ¿4 == 3? → False
print("¿(10 - 6) == 3?", resultado)    # False


# -----------------------------------------------------------------------------
# 9. COMPARACIÓN DE STRINGS Y EL ORDEN UNICODE
# -----------------------------------------------------------------------------
# Python compara strings letra por letra usando el código Unicode de cada carácter.
# Las letras mayúsculas tienen un código menor que las minúsculas.
# Podemos ver el código de un carácter con ord():

print("\nCódigo Unicode de 'A':", ord("A"))    # 65
print("Código Unicode de 'a':", ord("a"))      # 97
print("¿'A' < 'a'?", "A" < "a")               # True  ← 65 < 97
