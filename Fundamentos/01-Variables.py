
#Creando Variables

print('Hola mi nombre es:')
nombre = 'Leonel'

print(nombre)

#reutilizando la variable

#nombre = 'Ronaldo'

#print(nombre)

#variable entera

print('Tengo la de Edad de:')
edad = 25

print(edad)

print("Disculpa ¿Está encendida la luz del baño?")
respuesta = True

print(respuesta)

print('***************************************************')

#objects: Los valores que quieres imprimir, separados por comas. 
print('Hola mi nombre es', nombre, sep=":")

print('Tengo la de Edad de', edad, sep=":")

print("Disculpa ¿Está encendida la luz del baño?", respuesta, sep=" ")

print("Si sumamos 2.678 +3.899 eso es igual a:", 2.678 + 3.899 )

numero1 = 2

print("Si sumamos 2 + 2 es igual a: ", str(numero1) + str(2))

print(type(numero1))

#***************************

numero2 ='4'

print("Si sumamos 2 + 2 es igual a: ", int(numero2) + 2)

print(type(numero2))

print('Mi nombre tiene está cantidad de caracteres:', len(nombre))

#***************************************

primer_nombre, segundo_nombre, cumpleaños, edad, pais, carrera = "Leonel", "armando", "11/05/1997", 26, "El Salvador", "Ingeniería en Sistemas"

print("Hola soy", primer_nombre, segundo_nombre, "tengo", edad, "cumplo años el", cumpleaños, "soy de", pais, "y me de gradué de", carrera)

"""***************************************

primer_nombre= input('¿Cual es tú nombre? ')

edad = input('¿Cual es tú edad? ')

print("Mucho gusto", primer_nombre, "es un placer conocerte", 'no pareces que tengas', edad, 'años' ) """

direccion = 'El Salvador'
direccion = 5 
print(type(direccion))