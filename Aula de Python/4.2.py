"""2 – Escreva um programa que receba o salário de um funcionário (float), e retorne o resultado do
novo salário com reajuste de 35%."""

salario = float(input("Digite seu salario: R$ "))
porcent = (1.35) #0.35 é o percentual, o 1 equivale ao proprio valor de salário sendo assim 1.35 = salario + os 35%
calc = (salario*porcent)
print(calc)
