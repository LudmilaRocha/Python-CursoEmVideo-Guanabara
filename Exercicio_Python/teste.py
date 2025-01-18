print("Sistema de validacao")
cpf = int(input(("Informe o Cpf(apenas numeros):")))

if len(str(cpf)) == 11:
    print("1")
else:
    print("-1")
