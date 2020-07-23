import requests
import trade
from datetime import date
import json
import csv


hj = date.today()
## Pegar o primero dia de 2019
dia = date(2019, 1, 1)




def getFormatedData(periodo, dataPrimaria):
    counterDays = 0
    flagForCSV = 0

    nextDate = None
    while(counterDays != periodo):
    
        if (counterDays == 0):
            strGet = "https://www.mercadobitcoin.net/api/BTC/day-summary/"+str(dataPrimaria.year)+'/'+str(dataPrimaria.month)+'/'+str(dataPrimaria.day)+'/'
        else:
            strGet =  "https://www.mercadobitcoin.net/api/BTC/day-summary/"+str(nextDate.year)+'/'+str(nextDate.month)+'/'+str(nextDate.day)+'/'

        nextDate = dataPrimaria.fromordinal(dataPrimaria.toordinal()+1)

    
        r  = requests.get(strGet)

        print(r.json())
        
        data = r.json()['date']
        abertura = r.json()['opening']
        fechamento = r.json()['closing']
        baixa =  r.json()['lowest']
        maxima = r.json()['highest']
        volume = r.json()['volume']
        quantidade = r.json()['quantity']
        amount = r.json()['amount']
        media = r.json()['avg_price']

        with open('BTCSUMMARY.csv', 'a+', newline='\n') as file:
            writer = csv.writer(file)
            if(flagForCSV == 0):
                writer.writerow(["date", "opening", "closing", "lowest", "highest", "volume", "quantity", "amount", "avg_price"])
                writer.writerow([data, abertura, fechamento, baixa, maxima, volume, quantidade, amount, media])
                flagForCSV = 1
            else:
                writer.writerow([data, abertura, fechamento, baixa, maxima, volume, quantidade, amount, media])
        
        dataPrimaria = nextDate
        counterDays +=1 



getFormatedData(365, dia)