"""Crie um programa que leia 2 números e faça a soma entre eles"""

print("\t >> Programa para fazer a soma de dois números <<\n")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
somar = n1,n2

print(somar)
somar_tudo = sum(somar)
print(f"A soma entre os números de {n1} e {n2} é igual a {somar_tudo}")

