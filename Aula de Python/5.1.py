"""1 – Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
a) tamanho da lista.
b) maior valor da lista.
c) menor valor da lista.
d) soma de todos os elementos da lista.
e) lista em ordem crescente.
f) lista em ordem decrescente."""

L = [5, 7, 2, 9, 4, 1, 3]
print ("------------------------------------------------ ")
print("Lista")
print("Tamanho da Lista: ",len(L))
print("Maior valor: ", max(L))
print("Menor valor: ",min(L))
print("Soma dos valores: ", sum(L))
L.sort()
print("Ordem Crescente: ", L)
L.reverse()
print("Ordem Decrescente: ", L)
print ("------------------------------------------------ ")