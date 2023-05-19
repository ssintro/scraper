import logging
import inspect
import json
from bs4 import BeautifulSoup
import requests
import lxml

logging.info("Started")

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
    function_name = inspect.currentframe().f_code.co_name

    try:
        logging.debug(f"Processing: {function_name}")

        req = requests.get(url=url, headers=headers)

        print(f"[+] {url} {req.status_code}")

        soup = BeautifulSoup(req.text, 'lxml')

        jobs_href = soup.find('header').find(
            'ul').find('a', href='https://jobs.dou.ua/')

        link_to_jobs = jobs_href.get('href')

        getJobs(link_to_jobs, headers)

        logging.info(f"Success: {function_name}")

    except Exception as err:
        logging.exception(err)

        logging.info(f"Ended: {function_name}")


def getJobs(url, headers):
    function_name = inspect.currentframe().f_code.co_name

    logging.debug(f"Processing: {function_name}")

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

        logging.info(f"Success: {function_name}")

    except Exception as err:
        logging.exception(err)

        logging.info(f"Ended: {function_name}")


def main():
    getInfo(url='https://dou.ua/')


if __name__ == '__main__':
    main()
