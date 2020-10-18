def buscar_numero_en(numero, lista):
    indice = -1
    for i, item in enumerate(lista):
        if item == numero:
            indice = i
            break
    return indice

print(buscar_numero_en(1, [2,3,1,4,5]))
print(buscar_numero_en(1, [2,6,3,4,5]))