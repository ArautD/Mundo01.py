"""1 – Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z:
z =
(𝑥
2+ 𝑦
2
)
(𝑥−𝑦)
2
"""

x= int(input("Digite o primeiro valor para X:  ")) 
y= int(input("Digite o segundo valor para Y:  "))
z= ((x**2 + y**2) / (x - y)**2) 
print(z)