# ============================================================
# UNIDAD 02 - LA FUNCIÓN input()
# ============================================================
#
# input() permite que el programa pida datos al usuario por
# TECLADO. Cuando se ejecuta, el programa se detiene y espera
# que el usuario escriba algo y presione ENTER.
#
# Sintaxis:
#   variable = input("Mensaje a mostrar: ")
#
# IMPORTANTE:
#   input() SIEMPRE devuelve un string (str), aun cuando el
#   usuario escriba un número. Si necesitamos trabajar con un
#   número, hay que convertirlo con int() o float():
#
#       edad = int(input("Tu edad: "))
#       precio = float(input("Precio: "))
# ============================================================


# ------------------------------------------------------------
# 1) Pedir un dato simple
# ------------------------------------------------------------
edad = input("Decime tu edad: ")

print("Edad:", edad, "nombre:", "Juan")
print(type(edad))   # <class 'str'>  -> input siempre devuelve str


# ------------------------------------------------------------
# 2) Pedir varios datos al usuario
# ------------------------------------------------------------
nombre   = input("Ingrese un nombre: ")
apellido = input("Ingrese apellido: ")

print("Tu nombre es", nombre)
print("Tu apellido es", apellido)
print("Tu nombre completo es", nombre, apellido)


# ------------------------------------------------------------
# 3) Ejemplo combinando varios input()
# ------------------------------------------------------------
nombre = input("Ingrese su nombre: ")
edad   = input("Ingrese su edad: ")
lugar  = input("Ingrese su lugar de nacimiento: ")

print("Hola", nombre)
print("Su edad es", edad)
print("Usted nació en", lugar)
