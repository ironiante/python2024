"""
solicita al usuario que ingrese su nombre y edad
realiza algunas operaciones y luego muestra un mensaje con la información recopilada:
"""
nombre = input("Ingrese su nombre: ")
edad =  int (input("Ingrese su edad : "))
edad_doble = edad*2
mensaje = " su nombre es " + nombre + " y su edad es : " + str(edad_doble)
print(mensaje)



