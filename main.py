import carteira
import simulador
def printCarteira(carteira):
    print("quantidade de bitcoin: ", carteira.quantidadeDeBitcoin)
    print("valor inicial: ", carteira.valorInicial)
    print("valor disponivel: ", carteira.valorDisponivel)
    print("numero de compras", carteira.numeroDeCompras)
    print("numero de vendas", carteira.numeroDeVendas)
    print("porcentagem de lucro: ", (carteira.valorDisponivel/carteira.valorInicial)*100)
    print("dinheiro movimentado em compras: ", carteira.montanteDeCompra)
    print("dinheiro movimentado em vendas: ", carteira.montanteDeVenda)
    print("Lucro arrecadoado no mes: ", carteira.lucroMensal)
    print("Quantidade de compra por mes: ", carteira.contaCompraMes)
    print("Quantidade de compra por mes: ", carteira.contaVendaMes)
    print("Quantidade total comprada: ", carteira.quantidadeTotalComprada)

def main():
    portifolio = carteira.Carteira(100000)
    simulador.simulador(portifolio, 'OUTPUT_LSTM_reshape2')
    printCarteira(portifolio)


if __name__ == "__main__":
    main()
