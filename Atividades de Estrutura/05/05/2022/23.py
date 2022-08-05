"""Faça um programa que cadastre 5 produtos. Para cada produto, devem ser cadastrados o código do produto, preço 
e quantidade estocada. Os dados devem ser armazenados em uma lista simplesmente encadeada, não ordenada. 
Após o cadastro dos produtos, receber via teclado a taxa de desconto (ex.: digitar 10 pra desconto de 10%). 
Aplicar a taxa digitada ao preço de todos os produtos cadastrados e gerar um relatório final com o código e o novo
 preço do produto.

from typing import List
import random 
produto = []
cod_produto = []

for i in range(5):
    # Adciona a lista de produtos manualmente; - Porém ta com um none aparecendo e eu não sei pq
    produto.append(input(print(f"Digite o {i+1}º Produtos: ")))
    cod_produto.append(random.randint(100,110)) #geração dos cod;
    #Aqui to tentando fazer juntos o tal produto com o cod, mas não ta dando certo

"""

nome = []
codigo = []
quantidade = []
preco = []
desconto = 0

for i in range(5):
    print(f"\nProduto {i+1}:")
    nome.append(input("Digite o nome do produto: "))
    codigo.append(int(input("Digite o codigo: ")))
    quantidade.append(int(input("Digite a quanitdade em estoque: ")))
    preco.append(int(input("Digite o preço: ")))

desconto = int(input("\nDigite o desconto em %: "))

for i in range(5):
    preco[i] = preco[i] - desconto*preco[i]/100

for i in range(5):
    print(f"\n Produto {i+1}: ")
    print(f"Nome: {nome[i]}")
    print(f"Codigo: {codigo[i]}")
    print(f"Preço: {preco[i]}")
    print(f"Quantidade estocade: {quantidade[i]}")