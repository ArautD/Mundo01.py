""" Implemente uma classe Stack em python de forma a ter o método min() que retorna o menor valor da pilha em 
tempo constante. 8. Assinale alternativa correta sobre listas simplesmente encadeadas.
from typing import List

stack: List[str] = []
stack.append('A')
stack.append('B')

menor_stack= min(stack)

print(stack, menor_stack)"""

import random 
produto = []
cod_produto = []

for i in range(5):
    # Adciona a lista de produtos manualmente; - Porém ta com um none aparecendo e eu não sei pq
    produto.append(input(f"Digite o {i+1}º Produtos: "))
    cod_produto.append(random.randint(100,110)) #geração dos cod;
    #Aqui to tentando fazer juntos o tal produto com o cod, mas não ta dando certo