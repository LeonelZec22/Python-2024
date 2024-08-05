
#Creando una tupla
paises = ('Japan', 'USA', 'Germany', 'Spain', 'England', 'Portugal', 'Norway')

print(paises)

#paises[1] = 'Mexico' # Esto daría un error porque las tuplas son inmutables

print('¿Cuanto es el tamaño de está tupla?', len(paises))

#*****************************************************************+
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
ultimo_elemento =fruits[-1]

print(first_fruit)
print(second_fruit)
print(ultimo_elemento)

#*****************************************************************+

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3

print(orange_mango)

"""*****************************************************************
"""

print('¿Existe los USA dentro de está tupla?', 'USA' in paises)

print('¿Existe Mexico dentro de está tupla?', 'Mexico' in paises)

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits

#print(fruits) da error porque la tupla ya no existe al ser borrada

"""*****************************************************************
"""

#Creamos la tupla
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
print(type(fruits))
print(fruits)

#fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']

fruits = tuple(fruits)
print(type(fruits))
print(fruits)