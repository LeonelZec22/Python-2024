
#Creando una lista 

from audioop import reverse
import copy


equipos = list()
equipos.append("Real Madrid")
equipos.append("Milán")
equipos.append("Liverpool")

#print(equipos)
#print(len(equipos))

clubes = ["Manchester United", "Arsenal", "Borussia Dortmund"]
#print(clubes)

usuario = ['Leonel', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types

primer_equipo = equipos[0] #extraemos el dato que está en la posición cero de la lista

print(primer_equipo)

print(clubes[-1])
print(clubes[-3])

print(clubes[1])
print(clubes[2])

mi_lista = [10, 20, 30, 40, 50]

# Contando de izquierda a derecha (números positivos)
print(mi_lista[0])  # 10 (primer elemento)
print(mi_lista[1])  # 20 (segundo elemento)

# Contando de derecha a izquierda (números negativos)
print(mi_lista[-1])  # 50 (último elemento)
print(mi_lista[-2])  # 40 (penúltimo elemento)

print(clubes.count('Arsenal'))

primer_equipo, segundo_equipo,tercer_equipo = equipos

print(primer_equipo)
print(segundo_equipo)
print(tercer_equipo)

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

#Creamos una tercera lista a partir de la unión de dos listas ya existentes
champions = clubes+equipos

print (champions)

Paises = countries[0:3]

print(Paises) # ['Germany', 'France','Belgium']
print(countries[3:]) #si no fijamos el final se lleva todos los elementos que faltan 

Paises = countries[-4:-1]
print(Paises) # ['Finland', 'Norway', 'Iceland']

#Paises = countries[-1:-4]
#print(Paises)  # Error de lógica el paso está en positivo después de -1 se ira a la posición 0

Paises = countries[-1:-4:-1]
print(Paises)  # ['Estonia', 'Iceland', 'Norway']

Paises = countries[0:10:2]
print(Paises)  #['Germany', 'Belgium', 'Denmark', 'Norway', 'Estonia']

Paises = countries[-1:-10:-2]
print(Paises)  #['Estonia', 'Norway', 'Denmark', 'Belgium', 'Germany']

countries[8]= 'Spain'

print(countries)

countries[-2] = 'England'

print(countries)

print("¿Este país se encuentra dentro de está lista?")

no_existe = 'Portugal' in countries

print(no_existe)

print("¿Este país se encuentra dentro de está lista?")

si_existe = 'Spain' in countries

print(si_existe)

print('¿Existe USA dentro de está lista?', 'USA' in countries)

print('¿Cuantos elementos forman parte de está lista?', len(countries)) #9

countries.append('USA')

print(countries)

print('¿Cuantos elementos forman parte de está lista?', len(countries)) #10

countries.insert(2,'Japan') #se inserta en la posición 3 desplazando los demás valores un posición a la derecha

print(countries)

print('¿Cuantos elementos forman parte de está lista?', len(countries)) #10

print('********************************************')

mi_lista = [1, 2, 3, 1,2]
print('¿Cuantos elementos forman parte de está lista?', len(mi_lista)) #10
print(mi_lista)
mi_lista.remove(2)
print('¿Cuantos elementos forman parte de está lista?', len(mi_lista)) #10
print(mi_lista)  # [1, 3, 2]

print('********************************************')

mi_lista = [1, 2, 3,4,5,6]
print('¿Cuantos elementos forman parte de está lista?', len(mi_lista)) #6
valor = mi_lista.pop()  # eliminar el último elemento
print('El elemento que se elimino es el siguiente:',valor)   #conoces que dato se elimino 
print('¿Cuantos elementos forman parte de está lista?', len(mi_lista)) #5
print(mi_lista)  # [1, 2,3,4,5,6]

print('********************************************')

print('¿Cuantos elementos forman parte de está lista?', len(mi_lista)) #5
valor = mi_lista.pop(2)
print('El elemento que se elimino es el siguiente:',valor)   #conoces que dato se elimino 
print('¿Cuantos elementos forman parte de está lista?', len(mi_lista)) #5
print(mi_lista)  # 

print('********************************************')

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']

#esto borra los elementos entre los índices dados, ¡por lo que no borra el elemento con índice 3!
del fruits[1:3]     
print(fruits)       # ['orange', 'lime']
#del fruits #Elimina toda la lista 
print(fruits)       # La lista ya no existe

print('********************************************')
mi_lista = [1, 2, 3]
print('¿Cuantos elementos forman parte de está lista?', len(mi_lista)) #3
mi_lista.clear()
print(mi_lista)  # []
print('¿Cuantos elementos forman parte de está lista?', len(mi_lista)) #0

print('********************************************')
list1 = [1, 2, 3]
list2 = list1.copy()
list2.append(4)
print(list1)  # [1, 2, 3]
print(list2)  # [1, 2, 3, 4]

print('********************************************')

print(countries)

countries.reverse()

#copy_countries = countries.copy().reverse()
print(countries)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']

fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']