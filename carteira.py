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
        self.contaVendaMes = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0}
        self.contaCompraMes = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0}

    def podeComprar(self, fechamento):
        satoshi = fechamento/(10**8)
        # print("satoshi: ",satoshi)
        if(self.valorDisponivel >= satoshi):
            return True
        return False

    def comprar(self, fechamento, mes):
        quantidadeComprada = self.valorDisponivel/fechamento
        self.quantidadeTotalComprada += quantidadeComprada
        self.valorDisponivel = self.valorDisponivel - (quantidadeComprada*fechamento)
        self.quantidadeDeBitcoin = self.quantidadeDeBitcoin + quantidadeComprada
        self.numeroDeCompras += 1
        self.montanteDeCompra += quantidadeComprada*fechamento
        self.contaCompraMes[mes] +=1

    def verificaVenda(self):
        if(self.quantidadeDeBitcoin > 0):
            return True
        return False
    
    def vender(self, fechamento, mes):
        self.valorDisponivel = self.valorDisponivel + self.quantidadeDeBitcoin*fechamento
        self.montanteDeVenda += self.quantidadeDeBitcoin*fechamento
        self.quantidadeDeBitcoin = 0
        self.numeroDeVendas += 1
        self.contaVendaMes[mes] +=1  
        # print("venda realizada: ", self.valorDisponivel )
        # print("quantidade de bitcoin", self.quantidadeDeBitcoin)














 