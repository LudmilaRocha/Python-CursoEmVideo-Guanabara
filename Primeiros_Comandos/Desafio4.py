#Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas as
# informações possiveis sobre ela.
#validando a entrada do valor
algo = input("Digite algo no seu teclado:")
#verificando o tipo
print("Qual é o tipo da palavra:")
print(type(algo))
#Verifica se todos os caracteres de uma string são letras do alfabeto (a-z, A-Z).
print("Todos os caracteres da palavra são das letras alfabetica:")
print(algo.isalpha())
# Verifica se todos os caracteres alfabéticos da string estão em maiúsculas.
print("Os caracteres estão em maiusculas:")
print(algo.isupper())
#Verifica se a string contém apenas caracteres alfanuméricos (letras e números).
print("Os caracteres tem letras/numeros:")
print(algo.isalnum())
# Verifica se a string é um identificador válido em Python.
print("Os caracteres são validos em python:")
print(algo.isidentifier())
