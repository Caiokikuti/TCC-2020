import pandas as pd
import main


def simulador(carteira, dataName):
    inputData = pd.read_csv(dataName)
    lucroMensal = {}
    for i in range (0, len(inputData)):
        mesCorrente = inputData.values[i][0][5:7]
        decisaoDoDia = inputData.values[i][9]
        fechamento = float(inputData.values[i][4])
        if(i == 361):
            if(carteira.verificaVenda()):
                lucroMensal[mesCorrente] += carteira.quantidadeDeBitcoin*fechamento             
                carteira.vender(fechamento, mesCorrente)
                print("venda ultimo dia: ", carteira.quantidadeDeBitcoin*fechamento)
        else:
            if(decisaoDoDia == 1):  
                if(carteira.podeComprar(fechamento)):
                    if(mesCorrente in lucroMensal):
                        lucroMensal[mesCorrente] -= carteira.valorDisponivel
                    else:
                        lucroMensal[mesCorrente] = -1*(carteira.valorDisponivel) 
                    carteira.comprar(fechamento, mesCorrente)
            elif(decisaoDoDia == 0):   
                if(carteira.verificaVenda()):
                    if(mesCorrente in lucroMensal):
                        lucroMensal[mesCorrente] += carteira.quantidadeDeBitcoin*fechamento
                    else:
                        lucroMensal[mesCorrente] = carteira.quantidadeDeBitcoin*fechamento
                    carteira.vender(fechamento, mesCorrente)
    
    carteira.lucroMensal = lucroMensal

    