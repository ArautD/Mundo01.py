def inteiros_Test():
    n1 = int (input("Digite um valor ai: "))
    n2 = int (input ("Digite mais um ai tongo"))
    s = n1 + n2
    print (f"A soma dos números {n1} e {n2} é {s}")
    print(">>>>>>>>>>==<<<<<<<<<<<<<<<<<")

def teste_Tipagem():
    n = input("digite um número ai namoral: ")
    print(f"Upper? {n.isupper()}")
    print(f"Numeric? {n.isnumeric()}")
    print(f"AlphaNum? {n.isalnum()}")
    print(n.isalpha())
    print(n.isdecimal())
    print(n.isprintable())
    
inteiros_Test()
teste_Tipagem()