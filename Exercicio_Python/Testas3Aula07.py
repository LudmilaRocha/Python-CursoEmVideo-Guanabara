n1 = int(input("Um valor: "))
n2 = int(input("Informe outro valor: "))
print("A soma vale {}".format(n1 + n2))

# Cria uma variável, é aconselhável para demonstração
# Aplicando as operações
sm = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# As operações precisam estar alinhadas corretamente
print("A soma é {}, a subtração é {}, o produto é {} e a divisão {:.3f}".format(sm, sub, m, d), end = "")
print("Divisão inteira é {} e potência {}".format(di, e))

#o ende n realiza a quebra de linha ou barra invertida realiza um quebra de linha



