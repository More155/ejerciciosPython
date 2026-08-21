# =============================================================================
# SENTENCIA if / else EN PYTHON
# =============================================================================
# La sentencia 'if' permite que el programa tome decisiones.
# Si la condición es True, se ejecuta el bloque del if.
# Si es False, se ejecuta el bloque del else (si existe).
#
# ESTRUCTURA BÁSICA:
#
#   if condicion:
#       # bloque que se ejecuta si la condición es True
#   else:
#       # bloque que se ejecuta si la condición es False
#
# MUY IMPORTANTE: la indentación (sangría de 4 espacios) es obligatoria
# en Python. Define qué líneas pertenecen a cada bloque.
# =============================================================================


# -----------------------------------------------------------------------------
# Ejemplo con if / elif / else encadenados
# -----------------------------------------------------------------------------
# Cuando hay más de dos posibilidades, usamos 'elif' (else if).
# Python evalúa cada condición en orden y ejecuta el PRIMER bloque
# cuya condición sea verdadera. Las demás condiciones son ignoradas.
#
# ESTRUCTURA:
#
#   if condicion_1:
#       bloque 1
#   elif condicion_2:
#       bloque 2
#   elif condicion_3:
#       bloque 3
#   else:
#       bloque final (si ninguna condición anterior fue True)

alumno_nombre = "Federico"
alumno_edad   = int(input("Ingresá la edad del alumno: "))

# Evaluamos en qué rango de edad está el alumno
if alumno_edad > 40:
    mens_salida = "El alumno es mayor de 40 años."
elif alumno_edad > 30:
    mens_salida = "El alumno es mayor de 30 años."
elif alumno_edad > 20:
    mens_salida = "El alumno es mayor de 20 años."
else:
    mens_salida = "El alumno tiene 20 años o menos."

# Este print se ejecuta SIEMPRE, ya que está fuera de todos los bloques
print(mens_salida)
print("Fin del programa.")
