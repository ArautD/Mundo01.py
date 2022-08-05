"""Crie um algoritmo que leia um valor e a partir disso faça: (1) se o valor for 1, 2 ou 3, mostre o valor elevado
ao quadrado; (2) se o valor for o número 4 ou 9, mostre a raiz quadrada do número; (3) se for os valores 
6, 7 e 8, mostre o valor dividido 9. PAULO"""

valor = float(input (" Digite um valor de 1 a 9: "))
print("=====================================")

if valor in range(1,3):
    result = (valor**2)
    print("\t(1)se o valor for 1, 2 ou 3, mostre o valor elevado ao quadrado;")
    print("\t Resultado: ",result)

elif valor == (4 or 9):
    result = ("\t Resultado: ",valor**0.5)
    print("\t(2)se o valor for o número 4 ou 9, mostre a raiz quadrada do número;")
    print(valor)
else:
    result = (valor/9)
    print("\t (3) se for os valores 6, 7 e 8, mostre o valor dividido 9.")
    print("\t Resultado: ", result)
