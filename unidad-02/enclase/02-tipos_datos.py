# ============================================================
# UNIDAD 02 - TIPOS DE DATOS BÁSICOS EN PYTHON
# ============================================================
#
# En Python, todo valor tiene un "tipo de dato" asociado.
# Los tipos básicos que vamos a usar en esta unidad son:
#
#   int   -> Números enteros          (ej: 1, 3, 42, 100, -5)
#   float -> Números decimales        (ej: 3.14, 2.5, -0.7)
#   str   -> Cadenas de texto         (ej: "hola", "Python")
#   bool  -> Valores booleanos        (True / False)
#
# Para conocer el tipo de un valor o variable usamos la
# función type().
# ============================================================


# ------------------------------------------------------------
# 1) Tipo entero (int)
# ------------------------------------------------------------
print(235)                                     # 235
print("El tipo de 235 es:", type(235))         # <class 'int'>


# ------------------------------------------------------------
# 2) Tipo flotante (float)
# ------------------------------------------------------------
print(3.14)                                    # 3.14
print("El tipo de 3.14 es:", type(3.14))       # <class 'float'>


# ------------------------------------------------------------
# 3) Tipo cadena de texto (str)
# ------------------------------------------------------------
print("Hola mundo")
print("El tipo de 'Hola mundo' es:", type("Hola mundo"))   # <class 'str'>


# ------------------------------------------------------------
# 4) Tipo booleano (bool)
# ------------------------------------------------------------
# Solo tiene dos valores posibles: True o False.
print(True)
print("El tipo de True es:", type(True))       # <class 'bool'>
print(False)
print("El tipo de False es:", type(False))     # <class 'bool'>


# ------------------------------------------------------------
# 5) Tipos de datos guardados en variables
# ------------------------------------------------------------
# Las variables toman el tipo del valor que se les asigna.

# Variable de tipo entero (int)
numero_entero = 42
print(numero_entero, type(numero_entero))      # 42 <class 'int'>

# Variable de tipo flotante (float)
numero_flotante = 3.14
print(numero_flotante, type(numero_flotante))  # 3.14 <class 'float'>

# Variable de tipo string (str)
mensaje = "Hola mundo"
print(mensaje, type(mensaje))                  # Hola mundo <class 'str'>

# Variables de tipo booleano (bool)
verdadero = True
falso = False
print(verdadero, type(verdadero))              # True <class 'bool'>
print(falso, type(falso))                      # False <class 'bool'>
