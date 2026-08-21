# =============================================================================
# CONVERSIÓN DE TIPOS DE DATOS EN PYTHON
# =============================================================================
# Python tiene varios tipos de datos básicos:
#   int   → números enteros          (ej: 5, -10, 0)
#   float → números con decimales    (ej: 3.14, -2.5)
#   str   → cadenas de texto         (ej: "Hola", "42")
#   bool  → valores lógicos          (True o False)
#
# A veces necesitamos convertir un dato de un tipo a otro.
# Para eso usamos las funciones: int(), float() y str()
# =============================================================================


# -----------------------------------------------------------------------------
# 1. str() — Convertir a STRING (cadena de texto)
# -----------------------------------------------------------------------------
# Útil cuando queremos mostrar un número junto con texto usando concatenación.

numero = 20
print("Tipo original:", type(numero))       # <class 'int'>

numero_como_texto = str(numero)
print("Después de str():", type(numero_como_texto))  # <class 'str'>

# Caso de uso práctico: concatenar número con texto
print("El número es: " + str(numero))       # Correcto
# print("El número es: " + numero)          # ← Error: no se puede concatenar int con str


# -----------------------------------------------------------------------------
# 2. int() — Convertir a ENTERO
# -----------------------------------------------------------------------------
# Útil cuando recibimos un número como texto (por ejemplo, desde input())
# y necesitamos hacer operaciones matemáticas con él.

numero_texto = "654"
numero_entero = int(numero_texto)
print("\nDespués de int():", type(numero_entero))    # <class 'int'>
print("Valor:", numero_entero + 1)                  # Podemos operar: 655

# También podemos convertir un float a int (se pierde la parte decimal):
precio = 19.99
precio_entero = int(precio)
print("float → int:", precio_entero)                # 19  (no redondea, trunca)

# ADVERTENCIA: Si el texto no representa un número, int() dará error.
# int("Hola")   ← ValueError
# int("3.14")   ← ValueError (para decimales hay que usar float primero)


# -----------------------------------------------------------------------------
# 3. float() — Convertir a FLOTANTE (número con decimales)
# -----------------------------------------------------------------------------
# Útil cuando necesitamos precisión decimal en los cálculos.

numero_texto = "20.3"
numero_flotante = float(numero_texto)
print("\nDespués de float():", type(numero_flotante))  # <class 'float'>
print("Valor:", numero_flotante)                       # 20.3

# También podemos convertir un entero a float:
entero = 5
print("int → float:", float(entero))                  # 5.0


# -----------------------------------------------------------------------------
# 4. EJEMPLO PRÁCTICO — Calculadora de Hipotenusa (Teorema de Pitágoras)
# -----------------------------------------------------------------------------
# Fórmula: hipotenusa = √(cateto_a² + cateto_b²)
# En Python: (cateto_a**2 + cateto_b**2) ** 0.5

print("\n--- Calculadora de Hipotenusa ---")

# input() devuelve string → convertimos a float para poder calcular
cateto_a = float(input("Ingresá la longitud del cateto A: "))
cateto_b = float(input("Ingresá la longitud del cateto B: "))

hipotenusa = (cateto_a**2 + cateto_b**2) ** 0.5

# str() para poder concatenar el resultado con el texto
print("La hipotenusa es: " + str(hipotenusa))

# Ejemplo con cateto_a=3 y cateto_b=4:
# La hipotenusa es: 5.0
