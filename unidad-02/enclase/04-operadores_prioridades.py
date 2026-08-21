# ============================================================
# UNIDAD 02 - PRIORIDAD DE LOS OPERADORES
# ============================================================
#
# Cuando una expresión combina varios operadores, Python los
# evalúa siguiendo un orden de prioridad (similar al de la
# matemática). De MAYOR a MENOR prioridad:
#
#   1. ()                Paréntesis (modifican el orden natural)
#   2. **                Potencia
#   3. *  /  //  %       Multiplicación, división, división entera, módulo
#   4. +  -              Suma y resta
#
# Los operadores con la misma prioridad se evalúan de
# IZQUIERDA A DERECHA.
# ============================================================


# ------------------------------------------------------------
# 1) Variable inicial
# ------------------------------------------------------------
resultado = 20
print(resultado)   # 20


# ------------------------------------------------------------
# 2) El valor None
# ------------------------------------------------------------
# None representa la "ausencia de valor". Es útil cuando
# queremos declarar una variable sin un valor inicial concreto.
nombre = None
print(nombre)      # None


# ------------------------------------------------------------
# 3) Ejemplo SIN paréntesis
# ------------------------------------------------------------
# Pasos de evaluación:
#   2 ** 4      = 16
#   3 * 5       = 15
#   9 / 3       = 3
# Quedando:
#   2 + 15 - 3 + 16 = 30
print(2 + 3 * 5 - 9 / 3 + 2**4)   # 30.0


# ------------------------------------------------------------
# 4) Ejemplo CON paréntesis
# ------------------------------------------------------------
# Los paréntesis fuerzan el orden de evaluación.
# Lo que está dentro de () se calcula primero.
print(2 + 3 * (5 - 9) / 3 + (2**4 / 10))
