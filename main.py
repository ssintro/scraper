import logging
import json
from bs4 import BeautifulSoup
import requests
import lxml

URL = 'https://dou.ua/'

logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log",
                    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
                    datefmt='%H:%M:%S')


def getInfo():

    logging.info("Started")

    try:
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'lxml')
        info = soup.find('div', class_='sc-9d68cce4-0.sc-9d68cce4-3.gPdXCK').find(
            'tr')

        logging.debug("Processing")

        logging.info("Success")

        logging.info("Ended")

    except Exception as e:
        logging.error('Error: %s', str(e))

        logging.info("Ended")


def main():
    getInfo()


if __name__ == '__main__':
    main()
