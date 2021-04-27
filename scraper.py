from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime
import json


def main(): 
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://stockanalysis.com/stocks/")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    stocks ={}
    
    ulBox = soup.find('ul', class_="no-spacing")
    listings = ulBox.findAll('li')

    for li in listings:
        TickerAndName = li.a.text
        ticker = TickerAndName.split('-')[0].strip()
        stocks[ticker] = TickerAndName.split('-')[1].strip()
    
    driver.close()
    date = datetime.now().date()
    with open('Stocks '+ date.strftime('%d-%m-%y') +'.txt', 'w') as file:
        json.dump(stocks, file)


main()