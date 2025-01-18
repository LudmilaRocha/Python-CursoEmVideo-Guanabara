#CaseTecnicoAlgar
#“A empresa Telecom S.A oferece três diferentes produtos: X, Y, Z com valores respectivos de R$150, R$100, R$80.
#funcao
def valida_venda(idCliente, Charproduto):
    if idCliente % 2 != 0:
        return 1
    return -1

def redireciona_Checkout(idCliente, Charproduto):
    print("Voce foi redirecionado para o Chekout")
    return 1

def redireciona_Negociacao(idCliente, Charproduto):
    print(f"Cliente {idCliente} redirecionado para Negociacao do {Charproduto}")
    return 1

def realizarVenda(idCliente, Charproduto):

    produtos = {'X': 150, 'Y': 100, 'Z': 80}


#verifica se o cliente pode adquirir o produto

if valida_venda(IdCliente, Charproduto) == 1:
    if redireciona_Checkout(idClient, Charproduto) == 1:
        print(f"Venda realizada com sucesso")
    else:
        produto_valor_menor = min(produtos, key = produtos.get)

            print(f"Cliente nao pode adquirir o produto.")

     if validaVenda(idCliente,  produto_valor_menor) == 1:
            if redireciona_Checkout(int idCliente, Charproduto):

                print(f"Venda realizada com sucesso.")
        else:

            if redireciona_Negociacao(int idCliente, Charproduto):
                print(f"Cliente  redirecionado para negociação.")

# Exemplo de uso da função
idCliente = 456
produto = 'X'

realizarVenda(idCliente, Charproduto)

