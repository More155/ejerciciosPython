# =============================================================================
# EJEMPLOS PRÁCTICOS — SENTENCIA if / elif / else
# =============================================================================
# Este archivo muestra distintos casos de uso de las estructuras condicionales.
# Está pensado para ejecutar de a un ejemplo por vez.
# =============================================================================


# -----------------------------------------------------------------------------
# EJEMPLO 1 — if / else simple: mayoría de edad
# -----------------------------------------------------------------------------
# El bloque que está indentado (con sangría) dentro del if se ejecuta
# SOLO si la condición es verdadera. El else se ejecuta si es falsa.

alumno_nombre = "Juan"
alumno_edad   = 17

if alumno_edad >= 18:
    print("El alumno", alumno_nombre, "es mayor de edad.")
else:
    print("El alumno", alumno_nombre, "es menor de edad.")


# -----------------------------------------------------------------------------
# EJEMPLO 2 — if / else con entrada del usuario
# -----------------------------------------------------------------------------
# Combinamos input(), conversión de tipo y estructura condicional.

edad = int(input("\nEscribí tu edad: "))

if edad >= 18:
    print("Sos mayor de edad.")
    print("Podés votar.")
    print("Podés manejar.")
else:
    print("Sos menor de edad.")


# -----------------------------------------------------------------------------
# EJEMPLO 3 — Operador and: verificar un rango
# -----------------------------------------------------------------------------
# El operador 'and' permite combinar dos condiciones.
# El bloque se ejecuta SOLO si AMBAS condiciones son verdaderas.
#
# Sintaxis:
#   if condicion_1 and condicion_2:

alumno_edad = int(input("\nIngresá la edad del alumno: "))

if alumno_edad > 40 and alumno_edad < 50:
    print("El alumno tiene entre 40 y 50 años.")
elif alumno_edad >= 30:
    print("El alumno tiene 30 años o más.")
elif alumno_edad >= 20:
    print("El alumno tiene 20 años o más.")
elif alumno_edad >= 10:
    print("El alumno tiene 10 años o más.")
else:
    print("El alumno tiene menos de 10 años.")

print("Fin del programa.")


# -----------------------------------------------------------------------------
# EJEMPLO 4 — División exacta usando el operador módulo (%)
# -----------------------------------------------------------------------------
# El operador % devuelve el RESTO de una división.
# Si el resto es 0, la división es exacta.
#
# Ejemplo:
#   10 % 2 = 0  → exacta
#   10 % 3 = 1  → no exacta (sobra 1)

numero_uno = int(input("\nIngresá el primer número: "))
numero_dos = int(input("Ingresá el segundo número: "))

resto = numero_uno % numero_dos

if resto == 0:
    print("La división es exacta.")
else:
    print("La división NO es exacta. El resto es:", resto)
