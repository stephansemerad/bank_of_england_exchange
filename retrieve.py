
import requests, os
from bs4 import BeautifulSoup
from helpers import months_dictionary, currency_dictionary
from datetime import date, datetime, timedelta
from db import * 

end_date = datetime.now()
start_date = end_date - timedelta(days=365*2)
print(start_date.date(), end_date.date())

delta = int((end_date.date() - start_date.date()).days)


for i in range(delta):
    x = start_date + timedelta(days=i)

    url = f'https://www.bankofengland.co.uk/boeapps/database/Rates.asp?TD={x.day}&TM={months_dictionary[str(x.month)]}&TY={x.year}&into=GBP&rateview=D'    
    print('url: ', url)
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    
    filename = f"{x.year}_{x.month}_{x.day}.html"
    file_path = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), "files"), filename)
    
    with open(file_path,  "w", encoding="utf-8")  as file:
        file.write(str(soup))

    table = soup.find_all("table")[0]
    trs =  table.findAll('tr')

    for tr in trs:
        tds = tr.findAll('td')
        if len(tds) == 0:
            continue
        else:
            symbol = currency_dictionary[tds[0].text.strip()]
            
            rate = float( tds[1].text.replace('\t', '').replace('\r', '').replace(' ', '').strip().split('\n')[0])

            print('date: ', x.date())
            print('symbol: ', symbol )
            print('rate: ', rate )

            with Session() as session:
                fx = session.query(FX).filter(FX.date == x.date(), FX.symbol == symbol).first()
                fx = FX() if fx == None else fx

                fx.rate = rate
                fx.symbol = symbol
                fx.date = x.date()

                
                session.add(fx)
                session.commit()

    print('----------------------------------------------------------------')
