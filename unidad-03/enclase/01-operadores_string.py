# =============================================================================
# OPERADORES DE STRINGS EN PYTHON
# =============================================================================
# En Python, los strings (cadenas de texto) tienen dos operadores especiales:
#   +  →  Concatenación: une dos strings en uno solo
#   *  →  Replicación: repite un string una cantidad de veces
# =============================================================================


# -----------------------------------------------------------------------------
# 1. CONCATENACIÓN DE STRINGS (operador +)
# -----------------------------------------------------------------------------
# El operador + une dos o más strings uno detrás del otro.

saludo    = "Hola"
nombre    = "Mundo"
resultado = saludo + " " + nombre   # agregamos un espacio en el medio

print("Concatenación:", resultado)
# Salida: Hola Mundo

# IMPORTANTE: No se puede concatenar un string con un número directamente.
# Esto daría error:
#   print("Resultado: " + 42)       # ← TypeError
#
# Para solucionarlo, convertimos el número a string con str():
numero = 42
print("El número es: " + str(numero))   # ← Correcto
# Salida: El número es: 42


# -----------------------------------------------------------------------------
# 2. REPLICACIÓN DE STRINGS (operador *)
# -----------------------------------------------------------------------------
# El operador * repite un string la cantidad de veces que indiquemos.
# El número DEBE ser un entero (int). Con decimales daría error.

mensaje     = "Python "
repeticion  = mensaje * 3

print("Replicación:", repeticion)
# Salida: Python Python Python

# Otro ejemplo: construir una línea separadora
linea = "-" * 40
print(linea)
# Salida: ----------------------------------------

# Ejemplo combinado: concatenación + replicación
borde     = "+" + "*" * 15 + "+"
print(borde)
# Salida: +***************+


# -----------------------------------------------------------------------------
# 3. ENTRADA DE DATOS Y CONVERSIÓN DE TIPOS
# -----------------------------------------------------------------------------
# La función input() siempre devuelve un STRING, aunque el usuario escriba números.
# Si necesitamos operar matemáticamente, debemos convertir ese string al tipo
# de dato correcto usando int(), float() o str().

edad = input("Ingresá tu edad: ")
print("Tipo antes de convertir:", type(edad))   # <class 'str'>

# Convertimos el string a entero
edad = int(edad)
print("Tipo después de int():", type(edad))     # <class 'int'>

# También podemos convertir a otros tipos
edad_como_float  = float(edad)   # entero  → flotante
edad_como_string = str(edad)     # entero  → string

print("Como float :", edad_como_float,  type(edad_como_float))
print("Como string:", edad_como_string, type(edad_como_string))
