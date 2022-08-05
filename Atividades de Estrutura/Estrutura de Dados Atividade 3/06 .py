
#6 - Faça um Programa que peça dois números e imprima o maior deles.

print("=============================================")
print("\t Qual será o maior número?")
User1 = int(input("Digite um valor: "))
User2 = int(input("Digite um valor: "))
Maior = "O maior número é: "

if(User1 > User2):
    print(Maior, User1)
elif(User2 > User1):
    print(Maior, User2)
else:
    print("Algo deu errado, os números digitados são iguais!")