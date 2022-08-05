def verificarInteiroCrescente(lista):
    for i in range(len(lista)):
        if (isinstance(lista[i], int) == False):
            return False

    lista_cres = lista.copy()
    lista_cres.sort()

    if lista == lista_cres:
        return True
    else: 
        return False

l1 = [1 , 2, 3, 4, 5]

print(verificarInteiroCrescente(l1))