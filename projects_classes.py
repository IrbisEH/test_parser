from bs4 import BeautifulSoup
import requests
import numpy

from datetime import datetime

from db_classes import ConnectDB


class GetInfo:
    AUTHOR_ID = None
    PROJECT_ID = None

    def __init__(self):
        self.db = ConnectDB()
        self.url = self.db.get_url(self.PROJECT_ID)
        self.response = requests.get(self.url)
        print(f'для {self.__doc__} получен ответ, {self.response.status_code}')
        self.soup = BeautifulSoup(self.response.text, 'lxml')

    def get_title(self):
        pass

    def get_tariff_1(self):
        pass

    def get_tariff_2(self):
        pass

    def get_tariff_3(self):
        pass

    def get_tariff_4(self):
        pass

    def get_tariff_5(self):
        pass

    def get_average_price(self):
        prices = [
            self.get_tariff_1(),
            self.get_tariff_2(),
            self.get_tariff_3(),
            self.get_tariff_4(),
            self.get_tariff_5(),
        ]
        prices_lst = [i for i in prices if i is not None]
        avg_price = int(numpy.average(prices_lst))
        return avg_price

    def save_data(self):
        project_id = self.PROJECT_ID
        date = datetime.now().date()
        average_price = self.get_average_price()
        self.db.save_prices(
            project_id,
            date,
            average_price,
            self.get_tariff_1(),
            self.get_tariff_2(),
            self.get_tariff_3(),
            self.get_tariff_4(),
            self.get_tariff_5(),
        )


class GetInfo1(GetInfo):
    """Skillbox Здоровая самооценка"""
    AUTHOR_ID = '1'
    PROJECT_ID = '1'

    def get_title(self):
        """Название курса"""
        return self.soup.title.string

    def get_tariff_1(self) -> int:
        price = self.soup.find_all('li', class_='price-info__subprice')
        result = price[0].text
        result = int(''.join(i for i in result if i.isdigit()))
        return result

    # def get_discount_price(self) -> int:
    #     """Цена со скидкой"""
    #     price = self.soup.find_all('li', class_='price-info__subprice')
    #     result = price[0].text
    #     result = int(''.join(i for i in result if i.isdigit()))
    #     return result
    #
    # def get_installment_price(self) -> int:
    #     """Цена рассрочки которая отражена на сайте"""
    #     price = self.soup.find_all('li', class_='price-info__item')
    #     result = price[0].text
    #     result = int(''.join(i for i in result if i.isdigit()))
    #     return result
