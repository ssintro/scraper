import logging
import json
from bs4 import BeautifulSoup
import requests
import lxml

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
}

URL_PRICE = 'https://dashboard.pnmtoken.com/api/dpnm/price'
URL = 'https://dpnmdefi.com/app/'

def logs():
    logging.basicConfig(
    level=logging.DEBUG,
    filename = "requests.log",
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )

def getUserInfo():
    responseInfo = requests.get(URL, headers=headers)
    soup = BeautifulSoup(responseInfo.content, 'lxml')
    data_balance = soup.find("div", class_="flex-grow-1 ms-3")
    print(data_balance)

def getPrice():

    responsePrice = requests.get(URL_PRICE, headers=headers)
    responsePrice.raise_for_status()  # Raise an exception if the status code is an error code
    rt = responsePrice.text

    rt_list = json.loads(rt)
    result = [f"Date: {x['date']}, Price: {x['price']:.4f}\n" for x in rt_list]

    with open('data.txt', 'w') as file:
        file.writelines(result)

def main():
    logs()
    getPrice()
    getUserInfo()

if __name__ == '__main__':
    main()
