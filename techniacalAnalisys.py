import pandas as pd 
import ta

#load data
df = pd.read_csv('BTCSUMMARY.csv', sep=',')

#clean NaN Values
df = ta.utils.dropna(df)

#Testando os dados de Bollinger
indicador_bb = ta.volatility.BollingerBands(close=df["closing"], n=20, ndev=2)

df['bb_bbm'] = indicador_bb.bollinger_mavg()


print(df.columns)