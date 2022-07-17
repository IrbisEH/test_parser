from bs4 import BeautifulSoup
import requests

from db_classes import ConnectDB




class GetInfo1:
    """Skillbox Здоровая самооценка"""
    AUTHOR_ID = '1'
    PROJECT_ID = '1'

    def __init__(self):
        db = ConnectDB()
        self.url = db.get_url(self.PROJECT_ID)
        self.response = requests.get(self.url)
        print(f'{self.__doc__}, response code {self.response.status_code}')
        self.soup = BeautifulSoup(self.response.text, 'lxml')

    def get_title(self):
        """Название курса"""
        return self.soup.title.string

    def get_price(self) -> int:
        """Цена без скидки"""
        price = self.soup.find_all('li', class_='price-info__subprice')
        result = price[1].text
        result = int(''.join(i for i in result if i.isdigit()))
        return result

    def get_discount_price(self) -> int:
        """Цена со скидкой"""
        price = self.soup.find_all('li', class_='price-info__subprice')
        result = price[0].text
        result = int(''.join(i for i in result if i.isdigit()))
        return result

    def get_installment_price(self) -> int:
        """Цена рассрочки которая отражена на сайте"""
        price = self.soup.find_all('li', class_='price-info__item')
        result = price[0].text
        result = int(''.join(i for i in result if i.isdigit()))
        return result