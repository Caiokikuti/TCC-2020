import pandas_datareader as web
import carteira
import simulador
import techniacalAnalisys
import hibrido

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
    print("Quantidade de venda por mes: ", carteira.contaVendaMes)
    print("Quantidade total comprada: ", carteira.quantidadeTotalComprada)

def main():

    portifolioTA = carteira.Carteira(100000) 
    portifolio = carteira.Carteira(100000)
    portifolioHibrido = carteira.Carteira(100000)
    
    # teste do hibrido
    hibrido.simulador(portifolioHibrido, 'OUTPUT_LSTM_reshape2.csv')
    print("======================Hibrido=====================\n\n")
    print("Carteira HIBRIDA\n")
    printCarteira(portifolioHibrido)

    # teste da TA
    techniacalAnalisys.simulador(portifolioTA, 'OUTPUT_LSTM_reshape2.csv')
    print("======================TA=====================\n\n")
    print("Carteira TA\n")
    printCarteira(portifolioTA)

    # teste da LSTM
    simulador.simulador(portifolio, 'OUTPUT_LSTM_reshape2.csv')
    print("======================LSTM=====================\n\n")
    print("Carteira LSTM\n")
    printCarteira(portifolio)


if __name__ == "__main__":
    main()
