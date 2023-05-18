import logging
import json
import requests
from bs4 import BeautifulSoup
import lxml

URL_PRICE = 'https://dashboard.pnmtoken.com/api/dpnm/price'

logging.basicConfig(
    level=logging.DEBUG,
    filename="requests.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)


def getPrice():
    responsePrice = requests.get(URL_PRICE)
    rt = responsePrice.text

    rt_list = json.loads(rt)
    result = [f"Date {x['date']}: Price {x['price']:.2f}\n" for x in rt_list]
    result = [f"Date: {x['date']}, Price: {x['price']:.4f}\n" for x in rt_list]

    with open('data_dpnm_price.txt', 'w') as file:
        file.writelines(result)


def main():
    getPrice()


if __name__ == '__main__':
    main()
