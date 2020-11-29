

a_list = [3, 1, 2, 9, 5, 4, 7, 7, 6]

# Ordena los elementos de la lista in situ
a_list.sort()
a_list.sort(reverse=True)

a_list = [(1, 9), (1, 3), (1, 4), (1, 2)]
a_list.sort(key=lambda x: x[1])

# Revierte los elementos de la lista in situ
a_list = [3, 1, 2, 9, 5, 4, 7, 7, 6]
a_list.reverse()

a_list = [3, 1, 2, 9, 5, 4, 7, 7, 6]

# Ordena los elementos y crea una lista nueva
sorted(a_list)
sorted(a_list, reverse=True)

a_list = [(1, 9), (1, 3), (1, 4), (1, 2)]
sorted(a_list, key=lambda x: x[1])
