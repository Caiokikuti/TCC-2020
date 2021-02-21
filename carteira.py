class Carteira:
    def __init__(self, valorInicial):
        self.valorInicial = valorInicial
        self.valorDisponivel = valorInicial
        self.quantidadeDeBitcoin = 0
        self.quantidadeTotalComprada = 0
        self.numeroDeCompras = 0
        self.numeroDeVendas = 0
        self.montanteDeCompra = 0
        self.montanteDeVenda = 0
        self.lucroMensal = {}

    def podeComprar(self, fechamento):
        satoshi = fechamento/(10^8)
        if(self.valorDisponivel > satoshi):
            return True
        False

    def comprar(self, fechamento):
        quantidadeComprada = self.valorDisponivel/fechamento
        self.quantidadeTotalComprada += quantidadeComprada
        self.valorDisponivel = self.valorDisponivel - (quantidadeComprada*fechamento)
        self.quantidadeDeBitcoin = self.quantidadeDeBitcoin + quantidadeComprada
        self.numeroDeCompras += 1
        self.montanteDeCompra += quantidadeComprada*fechamento

    def verificaVenda(self):
        if(self.quantidadeDeBitcoin > 0):
            return True
        False
    
    def vender(self, fechamento):
        self.valorDisponivel = self.valorDisponivel + self.quantidadeDeBitcoin*fechamento
        self.montanteDeVenda += self.quantidadeDeBitcoin*fechamento
        self.quantidadeDeBitcoin = 0
        self.numeroDeVendas += 1  
        # print("venda realizada: ", self.valorDisponivel )
        # print("quantidade de bitcoin", self.quantidadeDeBitcoin)














 