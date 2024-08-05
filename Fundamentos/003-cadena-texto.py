
from traceback import print_tb


texto =""
print (len(texto)) #imprime 0
texto = "Buenos días"
print (len(texto)) #imprime 11

texto = '''Soy profesor y disfruto enseñando. 
No encontré nada tan gratificante como capacitar a la gente. 
Por eso creé 30 días de python.'''

print(texto)
#**************************************

"""Si insertamos una comilla sin pleca invertida la cadena de texto se cierra antes"""
print("Hola, soy un \"string\" con unas comillas doble.")

"""Si no insertamos la n con pleca python ignora el salto y lo muestra en una sola línea"""
print("Esta es la primera línea.\nEsta es la segunda línea.")

print("Hola,\\ soy un string con una barra invertida.")
print("Hola,\t soy un string con un tabulador.")


#Formateo antiguo utilizando %
"""
nombre = "Ana"
edad = 30
mensaje = "Hola, %s. Tienes %d años." % (nombre, edad)
print(mensaje)
"""

"""No es lo mismo que concatenación porque ahí estás uniendo dos o más cadenas mientras 
que con el formateo antiguo es una sola cadena que estás haciendo más grande al insertar valores"""

"""
nombre = "Ana"
edad = 30
mensaje = "Hola, " + nombre + ". Tienes " + str(edad) + " años."
print(mensaje)

nombre = "Ana"
edad = 30
mensaje = "Hola, %s. Tienes %d años." % (nombre, edad)
print(mensaje)

"""

nombre = "Ana"
edad = 30
mensaje = "Hola, {}. Tienes {} años.".format(nombre,edad)
#print(mensaje)

num1 = 4
num2 = 3

"""
#sustituye la llave por el valor de la variable
print('{} + {} = {}'.format(a, b, a + b)) #7
print('{} - {} = {}'.format(a, b, a - b)) #1
print('{} * {} = {}'.format(a, b, a * b)) #12

"""

"""
print(f"Hola, mi nombre es {nombre}. Tengo {edad} años")

print(f'{num1} + {num2} = {num1 + num2}') #7
print(f'{num1} - {num2} = {num1 - num2}') #1
print(f'{num1} * {num2} = {num1 * num2}') #12
"""

#Desempaquetado de caracteres 

#pais = "España"

#e,s,p,a,ñ,a = pais

#print(e)

#letra = pais[2]

#print (letra) 

pais = "El Salvador"

subcadena = pais[3:6]

#print(subcadena)

subcadena = pais[::-1]

#print(subcadena)

lenguaje = 'python'

print(lenguaje.capitalize()) #convierte a mayuscula la primera letra


challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(6)) # 'thirty    days      of        python'

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0


challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 8)) # error

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8
print(challenge.rindex(sub_string, 9)) # error

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True

num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'