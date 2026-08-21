# =============================================================================
# SENTENCIA elif EN PYTHON
# =============================================================================
# 'elif' es una contracción de "else if" (si no, entonces si...).
# Se usa cuando necesitamos evaluar más de dos condiciones posibles.
#
# REGLAS IMPORTANTES:
#   - Siempre empieza con un 'if'
#   - Puede haber VARIOS 'elif' encadenados
#   - El 'else' es opcional y va siempre al final
#   - En cuanto una condición es True, el resto se omite
#
# ESTRUCTURA:
#
#   if condicion_1:
#       bloque 1          ← se ejecuta si condicion_1 es True
#   elif condicion_2:
#       bloque 2          ← se ejecuta si condicion_1 es False Y condicion_2 es True
#   elif condicion_3:
#       bloque 3          ← se ejecuta si las anteriores son False Y condicion_3 es True
#   else:
#       bloque final      ← se ejecuta si NINGUNA condición anterior fue True
# =============================================================================

alumno_nombre = "Federico"
alumno_edad   = int(input("Ingresá la edad del alumno: "))

if alumno_edad > 40:
    print("El alumno", alumno_nombre, "es mayor de 40 años.")
elif alumno_edad > 30:
    print("El alumno", alumno_nombre, "tiene entre 31 y 40 años.")
elif alumno_edad > 20:
    print("El alumno", alumno_nombre, "tiene entre 21 y 30 años.")
else:
    print("El alumno", alumno_nombre, "tiene 20 años o menos.")

# Esta línea siempre se ejecuta porque está fuera de todos los bloques
print("Fin del programa.")

# -----------------------------------------------------------------------------
# ¿QUÉ PASA INTERNAMENTE?
# -----------------------------------------------------------------------------
# Supongamos que alumno_edad = 35:
#
#   ¿35 > 40?  No  → saltamos al primer elif
#   ¿35 > 30?  Sí  → ejecutamos este bloque y salimos del if/elif/else
#
# Los elif que siguen (> 20) y el else NO se evalúan.
# Esto hace que el código sea eficiente y evita evaluar condiciones innecesarias.
