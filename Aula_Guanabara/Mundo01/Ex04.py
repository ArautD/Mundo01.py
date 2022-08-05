"""Dissecando uma variável"""
inicio = input("Digite algo para análise: ")
print("=========================================")
print("O tipo primitivo desse valor é ", type(inicio))
print("Só tem espaços digitados? ", " -- ",inicio.isspace())
print("É um número? ", " -- ", inicio.isnumeric())
print("É alfabético? ", " -- ",inicio.isalpha())
print("Está em maiúsculo? ", " -- ", inicio.isupper())
print("Está em minúsculo? ", " -- ", inicio.islower())
