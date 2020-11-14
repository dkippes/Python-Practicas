import json

#serializar un objeto
json.dump([1,2,3])

#deserializar un objeto
json.loads('[1,2,3]')

#escribir como json directamente a un archivo
with open('home/aolmedo/coursera/python', 'w') as a_file:
    json.dump([1,2,3,4], a_file)

#leer un json directamente desde un archivo
with open('home/aolmedo/coursera/python', 'r') as a_file:
    a_list = json.load(a_file)