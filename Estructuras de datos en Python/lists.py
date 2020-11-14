a_list = [3, 7.5, 'Hola', 7j + 5, [1,2]];

# Acceso mediante indexacion
a_list[0] # 3
a_list[2] # 'Hola'
a_list[-1] # [1, 2]

# Slicing
a_list[1:] # [7.5, 'Hola', 7j + 5, [1,2]]
a_list[1:2] # [7.5]
a_list[1:3] # [7.5, 'Hola']
a_list[:2] # [3, 7.5, 'Hola', 7j + 5, [1,2]]
a_list[:] # [3, 7.5, 'Hola', 7j + 5, [1,2]]

# Algunas funciones

# Devuelve la cantidad de elementos de la lista
len(a_list) # 5
# Agrega un elemento al final de la lista
a_list.append(2)
# Extiende la lista con los elementos de otras lista
a_list.extend([3, 4])
# Insertar un elemento en una posicion determinada
a_list.insert(4, 'Intercalado')
a_list.insert(12, 'Fuera de rango')
a_list.insert(-1, 'Hacia atras')
# Cuenta cuantos elementos hay que coincidan con el argumento
a_list.count(3)
# Elimina el primer elemento que encuentra pasado por parametro
a_list.remove(3)
# Hace una copia superficial de la lista
a_list_copy = a_list.copy()
# Saca el ultimo elemento y lo  devuelve
a_list.pop(3)
# Borra todos los elementos de la lista
a_list.clear()