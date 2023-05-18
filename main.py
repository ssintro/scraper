import logging
import json
from bs4 import BeautifulSoup
import requests
import lxml

# URL = 'https://dou.ua/'

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42'
}

logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log",
                    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
                    datefmt='%H:%M:%S')


def getInfo(url, headers=headers):

    logging.info("Started")

    try:
        logging.debug("Processing")

        req = requests.get(url=url, headers=headers)

        print(f"[+] {url} {req.status_code}")

        soup = BeautifulSoup(req.text, 'lxml')

        first_job = soup.find('div', class_='col70 m-cola').find(
            'ul', class_='b-index-links').find('li').find('a', href='https://jobs.dou.ua/first-job/?from=doufp')

        print(f"{first_job.text}: {first_job.get('href')}")

        logging.info("Success")

        logging.info("Ended")

    except Exception as e:
        logging.error('Error: %s', str(e))

        logging.info("Ended")


def main():
    getInfo(url='https://dou.ua/')


if __name__ == '__main__':
    main()
