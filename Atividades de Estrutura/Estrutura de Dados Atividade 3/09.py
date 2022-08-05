"""Crie um algoritmo que leia um valor e a partir disso faça: (1) se o valor for 1 e 2, mostre o valor elevado 
ao cubo; (2) se o valor for múltiplo de 3 mostre o fatorial desse número; (3) se o valor for os valores 4, 5, 7
ou 8, mostre o valor dividido 9. Caso não seja nenhum dos valores, informe como “valor inválido”. PAULO"""

from math import factorial #biblioteca pra poder usar o fatorial MATH.

valor = int(input("Digite um valor: "))

if valor in range(1,3):
    print("\t >>\033[96m=====================================")
    result = valor ** 3
    print("\t(1) se o valor for 1 e 2, mostre o valor elevado ao cubo;")
    print(f"\t O Resultado é: {result}")
    
elif valor % 3 == 0:
    print("\t >>\033[92m=====================================")
    print("\t(2) se o valor for múltiplo de 3 mostre o fatorial desse número;")
    print (f"\t O Resultado de {valor}!: ", factorial(valor))

elif valor % 3 != 0: #Já que acima temos os múltiplos de 3, decidi por pra facilitar o entendimento
    print("\t >>\033[94m=====================================")
    result = (valor/9)
    print("\t (3) se o valor for os valores 4, 5, 7ou 8, mostre o valor dividido 9. Caso não seja nenhum dos valores, informe como “valor inválido”.")
    print(f"\t O Resultado é: {result:.2f}")
else:
    print("\t\033[91m VALOR INVALIDO!!!")   