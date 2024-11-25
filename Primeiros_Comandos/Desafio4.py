#Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas as
# informações possiveis sobre ela.

algo = input("Digite algo no seu teclado:")

print(type(algo))
#Verifica se todos os caracteres de uma string são letras do alfabeto (a-z, A-Z).
print(algo.isalpha())
# Verifica se todos os caracteres alfabéticos da string estão em maiúsculas.
print(algo.isupper())
#Verifica se a string contém apenas caracteres alfanuméricos (letras e números).
print(algo.isalnum())
# Verifica se a string é um identificador válido em Python.
print(algo.isidentifier())
