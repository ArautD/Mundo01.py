#Operadores Aritméticos

#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considerando US$ 1.00 = R$ 3.27
def converteUS():
    br_us = (n*3.27)
    print(f'Você possui R$ {n:.2f} o mesmo que US$ {br_us:.2f}')

print('Programa de conversão R$ para US$')
print('-====================================-')
n = float(input('Quantidade de Reais na carteira: '))
converteUS()