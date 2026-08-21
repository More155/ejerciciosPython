# ============================================================
# UNIDAD 02 - COMENTARIOS EN PYTHON
# ============================================================
#
# Los comentarios son líneas de texto dentro del código fuente
# que el intérprete de Python IGNORA por completo. No afectan
# el funcionamiento del programa.
#
# Sirven para:
#   - Explicar qué hace una porción de código.
#   - Documentar decisiones o aclaraciones.
#   - Desactivar temporalmente líneas de código durante pruebas.
# ============================================================


# ------------------------------------------------------------
# 1) Comentarios de UNA sola línea
# ------------------------------------------------------------
# Se escriben con el símbolo numeral (#).
# Todo lo que esté a la derecha del # en esa línea es ignorado
# por el intérprete.

# Esto es un comentario de una sola línea
# Puedo escribir varios comentarios uno debajo del otro
# para explicar lo que viene a continuación.

print("Hola Mundo")   # También se puede comentar al final de una línea de código


# ------------------------------------------------------------
# 2) Comentarios de VARIAS líneas (multilínea)
# ------------------------------------------------------------
# Se encierran entre triples comillas dobles (""" """) o triples
# comillas simples (''' '''). Sirven para:
#   - Escribir comentarios largos.
#   - Anular temporalmente un bloque de código.

"""
Este es un comentario de varias líneas.
Se usa cuando necesitamos explicar algo más extenso,
por ejemplo, la lógica de una función o de un módulo.
También sirve para deshabilitar un bloque de código sin borrarlo.
"""


# ------------------------------------------------------------
# 3) Cómo procesa Python los comentarios
# ------------------------------------------------------------
# Python NO ejecuta las líneas que son comentarios.
# Solo ejecuta las líneas con código real.

print("Esta línea SÍ se ejecuta")
# print("Esta línea NO se ejecuta porque está comentada")
print("Acá sigue el programa...")
