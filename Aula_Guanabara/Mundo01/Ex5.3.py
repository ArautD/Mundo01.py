#Operadores Aritméticos
"""Escreva um programa que leia um valor em metros e o exiba 
em centimetros e milimetros"""
def meter_cm():
    mcm = (n * 100)
    print(f"{n} m convertidos em {mcm} cm - Centimetros")
def cm_mm():
    cmmm = (n * 1000)
    print(f"{n} m convertidos em {cmmm} mm - Milimetros")
print("Programa para transformar Metro em Centimentros e Milimetros")
print("-============================================================-")
n = float(input("Digite a quantidade de metros para conversão: "))
meter_cm()
cm_mm()
