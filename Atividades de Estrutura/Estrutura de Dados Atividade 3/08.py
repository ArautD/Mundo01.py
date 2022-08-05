"""Crie um algoritmo que leia um valor e a partir disso
faça: (1) se for um valor negativo, mostre o módulo 
(valor sem sinal) do valor; (2) se for um valor maior 
do que 10, solicite outro valor e mostre a diferença 
entre eles; (3) Caso o valor não seja de nenhuma 
condição anterior, mostre o valor dividido por 5."""
diferenca = ""
valor = float(input("Digite um valor: "))
print("=====================================")

if valor < 0:
    print("\t(1) se for um valor negativo, mostre o módulo (valor sem sinal) do valor;")
    print("\t Valor Sem Sinal!")
elif valor > 10:
    print("\t(2) se for um valor maior do que 10, solicite outro valor e mostre a diferença entre eles;")
    correc = float(input(" Digite outro Valor: "))
    diferenca = (valor - correc)
    print(f"\t A Diferença entre eles é de {diferenca}")
else:
    result = (valor/5)
    print("\t (3) Caso o valor não seja de nenhuma condição anterior, mostre o valor dividido por 5.")
    print("\t Resultado: ", result)