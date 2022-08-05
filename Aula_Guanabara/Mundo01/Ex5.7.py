#Operadores aritméticos
#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
def descont():
    valor_desconto = (produto * (porcentagem_desconto/100))
    valor_total = (produto - valor_desconto)
    print(f"O desconto soliciado foi de {porcentagem_desconto}%\nValor de produto foi de {produto}")
    print("-=====================-")
    print(f"\t\t\t\tValor final {valor_total:.2f}")

print("Programa de mercado")
print("-=====================-")
print(">>>EXEMPLO: 5 equivale a 5% <<<")
print("-=====================-")
porcentagem_desconto = float(input("Digite a quantidade de desconto: "))
print("-=====================-")
print(">>>EXEMPLO 5 equivale a R$5.00 <<<")
print("-=====================-")
produto = float(input("Valor do produto: "))
print("-=====================-")

descont()
