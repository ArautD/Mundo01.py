# Operações aritméticas

"""Desenvolver um programa que leia as duas notas de um aluno
Calcule e mostre a sua média"""

print("Programa de notas escolar")
print("-==========================-")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1,nota2)
print(f"As notas digitadas foram {nota1}  {nota2}\n-==========================-")
print(f"A média de suas notas é {sum(media)/len(media)}")
