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
        logging.debug("Processing def getInfo")

        req = requests.get(url=url, headers=headers)

        print(f"[+] {url} {req.status_code}")

        soup = BeautifulSoup(req.text, 'lxml')

        jobs_href = soup.find('header').find(
            'ul').find('a', href='https://jobs.dou.ua/')

        link_to_jobs = jobs_href.get('href')

        getJobs(link_to_jobs, headers)

        logging.info("Success")

    except Exception as err:
        logging.exception(err)

        logging.info("Ended on def getInfo")


def getJobs(url, headers):
    logging.debug("Processing def getInfo")

    try:
        req = requests.get(url=url, headers=headers)

        print(f"[+] {url} {req.status_code}")

        soup = BeautifulSoup(req.text, 'lxml')

        find_jobs = soup.find_all('a', {'class': 'cat-link'})

        jobs = []

        for cat in find_jobs:
            jobs.append(f"Job as {cat.text}: {cat.get('href')}")

        with open('data_jobs_dou.txt', 'w', encoding='utf-8') as file:
            file.writelines('\n'.join(jobs))

    except Exception as err:
        logging.exception(err)

        logging.info("Ended on def getJobs")


def main():
    getInfo(url='https://dou.ua/')


if __name__ == '__main__':
    main()
    