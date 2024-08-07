
from os import name


person = {
    'first_name':'Leonel',
    'last_name':'Moran',
    'age':25,
    'country':'El Salvador',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

print('****************************************************++')
print('¿Cuantos elementos hay en este diccionario?', len(person))

person['job_title'] = 'Instructor'
person['skills'].append('HTML')

print('Hola mi nombre es',person['first_name']) # Leonel
print('Soy del',person['country'])    # El Salvador
print('Me gradué de', person['job_title'])
print('He estudiado estos lenguajes',person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print('pero mi favorito es',person['skills'][4])  # Python
print('puedes enviarme regalos a está dirección:',person['address']['street']) # Space street

print('¿Cuál es mi ciudad de residencia?',person.get('city'))   # None

print('****************************************************++')

print(f'Hola soy {person["first_name"]}, tengo {person["age"]} años y soy {person["job_title"]}')

person['age']='20'
person['job_title'] = 'Ingeniero en sistemas'

print(f'Hola soy {person["first_name"]}, tengo {person["age"]} años y soy {person["job_title"]}')

print('****************************************************++')

print('¿Existe el color favorito dentro del diccionario?', 'color_favorito' in person)
print('¿Existe la carrera profesional dentro del diccionario?', 'job_title' in person)

print('****************************************************++')

print('El valor eliminando del diccionario es el siguiente:', person.pop('is_marred'))

print(person)

print('****************************************************++')

copy_person = person.copy()

copy_person['first_name'] = 'Ronaldo'

print(copy_person)

print('****************************************************++')

claves_person = person.keys();

print(claves_person)

print('****************************************************++')

valores_person = person.values()

print(valores_person)

print('****************************************************++')

#Crear un nuevo diccionario sin valores es decir hace una copia de un diccionario
print(person.fromkeys(('age', 'country')))