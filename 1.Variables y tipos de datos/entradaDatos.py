"""
entrada de datos:
En Python, puedes solicitar entrada del usuario utilizando la función input(). Esta función lee una línea de texto
 desde la entrada estándar (generalmente el teclado) y devuelve una cadena
"""
#solicitar al usuario que ingrese su nombre
nombre =input("Introduce tu nombre: ")
#mostrar un saludo utilizando el nombre proporcionado.
print ("hola " + nombre)
# solicicitar al usuario que ingrese un numero y realice la operacion.
numero = input("Ingrese un numero: ")
# La función input devuelve una cadena, así que convertimos la entrada a un número entero
numero_entero = int(numero)
# Realizar una operación con el número ingresado
resultado = numero_entero * 2
print ("El resultado es", resultado)

#_____________________________________________________
# Solicitar al usuario que ingrese un número decimal
decimal_str = float (input("ingrese un numero decimal: "))
print (decimal_str)