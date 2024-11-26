#Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas as
# informações possiveis sobre ela.

a = input("Informe algo:")
print("O tipo primitivo deste valor é:", type(a))
print("Tem espaços:", a.isspace())
print("É um número:", a.isnumeric())
print("É alfabetico:", a.isalpha())