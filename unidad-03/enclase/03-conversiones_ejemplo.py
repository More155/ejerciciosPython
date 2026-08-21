# =============================================================================
# EJEMPLO PRÁCTICO — CONVERSIÓN DE TIPOS: CÁLCULO DE HIPOTENUSA
# =============================================================================
# Este programa aplica lo visto sobre conversión de tipos en un problema real.
#
# CONTEXTO:
#   El Teorema de Pitágoras dice que en un triángulo rectángulo:
#       hipotenusa² = cateto_a² + cateto_b²
#   Despejando:
#       hipotenusa = √(cateto_a² + cateto_b²)
#   En Python la raíz cuadrada se escribe como: numero ** 0.5
#
# CONCEPTOS QUE SE APLICAN:
#   - input()  → siempre devuelve string
#   - float()  → convierte el string a número decimal para poder calcular
#   - **       → operador de potencia (2 ** 3 = 8)
#   - str()    → convierte el resultado a string para concatenar con texto
# =============================================================================

# Pedimos los dos catetos al usuario
# Como input() devuelve string, convertimos inmediatamente a float
lado_a = float(input("Ingresá el valor del lado A (cateto): "))
lado_b = float(input("Ingresá el valor del lado B (cateto): "))

# Paso 1: elevamos cada cateto al cuadrado y los sumamos
sub_total = lado_a ** 2 + lado_b ** 2

# Paso 2: calculamos la raíz cuadrada del resultado
# Elevar a la 0.5 es equivalente a calcular la raíz cuadrada
hipotenusa = sub_total ** 0.5

# Mostramos el resultado
print("La hipotenusa del triángulo es:", hipotenusa)

# Ejemplo:
#   lado_a = 3, lado_b = 4
#   sub_total  = 3² + 4² = 9 + 16 = 25
#   hipotenusa = 25 ** 0.5 = 5.0
