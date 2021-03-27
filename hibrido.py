import pandas as pd 
import ta

#load data



def simulador(carteira, dataName):
    inputData = pd.read_csv(dataName)
    lucroMensal = {}
    



    for i in range (1, len(inputData)+1):

        if i == 362:
            mesCorrente = inputData.values[i-1][0][5:7]
            fechamento = float(inputData.values[i-1][4])
            decisaoDoDia = inputData.values[i-1][9]
        else:
            mesCorrente = inputData.values[i][0][5:7]
            fechamento = float(inputData.values[i][4])
            decisaoDoDia = inputData.values[i][9]
        

        rsi = ta.momentum.RSIIndicator(close=inputData['Close'], n=9, fillna=False)
        inputData['rsi'] = rsi.rsi()

        stochasticOscilator = ta.momentum.StochasticOscillator(high=inputData['High'], low=inputData['Low'], close=inputData['Close'], n=14, d_n=3, fillna=True)
        inputData['stochastic'] = stochasticOscilator.stoch_signal()

        MACD = ta.trend.MACD(close=inputData['Close'], n_slow= 26, n_fast=12, n_sign=9, fillna=True)
        inputData['MACD_diff'] = MACD.macd_diff()

        if(i == 362):
            if(carteira.verificaVenda()):
                # lucroMensal[mesCorrente] += carteira.quantidadeDeBitcoin*fechamento             
                # print("venda ultimo dia: ", carteira.quantidadeDeBitcoin*fechamento)
                if(mesCorrente in lucroMensal):
                    lucroMensal[mesCorrente] += carteira.quantidadeDeBitcoin*fechamento
                else:
                    lucroMensal[mesCorrente] = carteira.quantidadeDeBitcoin*fechamento
                carteira.vender(fechamento, mesCorrente)
        else:
            if(decisaoDoDia == 1):  
                if(carteira.podeComprar(fechamento)):
                    if(mesCorrente in lucroMensal):
                        lucroMensal[mesCorrente] -= carteira.valorDisponivel
                    else:
                        lucroMensal[mesCorrente] = -1*(carteira.valorDisponivel)
                    carteira.comprar(fechamento, mesCorrente)
            elif((inputData['stochastic'][i-1] >= 80) and (decisaoDoDia == 0) and (inputData['rsi'][i-1] >= 70) and (inputData['MACD_diff'][i-1] <= 0)):   
                if(carteira.verificaVenda()):
                    if(mesCorrente in lucroMensal):
                        lucroMensal[mesCorrente] += carteira.quantidadeDeBitcoin*fechamento
                    else:
                        lucroMensal[mesCorrente] = carteira.quantidadeDeBitcoin*fechamento
                    carteira.vender(fechamento, mesCorrente)
    carteira.lucroMensal = lucroMensal