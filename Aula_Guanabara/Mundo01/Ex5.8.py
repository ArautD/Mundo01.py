#Operadores Aritméticos
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salaário com aumento de 15%
print("Programa de salário")
print("-===========================-")
def reajusteSalario():
    reS = (salario * (aumento/100))
    newS = (salario + reS)
    print(f"Salario selecionado: R$ {salario}\nAumento de {aumento}%")
    print("-===========================-")
    print(f"Salario final: R$ {newS:.2f}")
salario = float(input("Digite o valor de Salário: "))
aumento = float (input("Digite a porcentagem de aumento: "))

reajusteSalario()
