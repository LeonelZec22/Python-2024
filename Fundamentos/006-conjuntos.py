
from os import remove


mi_conjunto = {1, 2, 3, 4}
print(mi_conjunto)  # {1, 2, 3, 4}

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)

mi_conjunto.add(5)
print(mi_conjunto)  # {1, 2, 3, 4, 5}

mi_conjunto.remove(3)
print(mi_conjunto)  # {1, 2, 4, 5}

print('¿Cuantos elementos hay en este conjunto?', len(fruits))

print('*******************************************************')
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)

vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

print(fruits)

print('*******************************************************')
mi_conjunto = {1, 2, 3}
mi_conjunto.remove(2)
print(mi_conjunto)  # {1, 3}
#mi_conjunto.remove(4)  # Esto lanzará un KeyError porque 4 no está en el conjunto

mi_conjunto = {1, 2, 3}
mi_conjunto.discard(2)
print(mi_conjunto)  # {1, 3}
mi_conjunto.discard(4)  # No hace nada, no lanza error
print(mi_conjunto)  # {1, 3}

tareas_completadas = {"tarea1", "tarea2", "tarea3"}

#tareas_completadas.remove("tarea4");

#print("La tarea4 no está completada aún")

elementos = {"elemento1", "elemento2", "elemento3"}

elementos.discard("elemento2")  # Funciona bien, elimina el elemento si está presente
elementos.discard("elemento4")  # No hace nada, no lanza error

print('****************************************************************')
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruit_delete = fruits.pop()  
print("La fruta eliminada del conjunto fue", fruit_delete)
print(fruits)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits