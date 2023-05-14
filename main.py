import logging
import json
import requests
from bs4 import BeautifulSoup
import lxml


# Настройка объекта logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создание обработчика для вывода логов в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.ERROR)

# Создание форматтера для вывода логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Добавление обработчиков в logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


logging.basicConfig(
    level=logging.DEBUG,
    filename = "requests.log",
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )


try:
    URL = 'https://dpnmdefi.com/app/'
    URL_PRICE = 'https://dashboard.pnmtoken.com/api/dpnm/price'
    response = requests.get(URL)
    response_price = requests.get(URL_PRICE)
    rt = response_price.text

    soup = BeautifulSoup(response.content, "lxml")

    pool = soup.find("p", {"class": "header-icon2 fw-medium text-white-50"})

    pool_text = pool.get_text()

    print(pool_text)

    rt_list = json.loads(rt)
    result = [f"Date {x['date']}: Price {x['price']:.2f}\n" for x in rt_list]

    with open('data.txt', 'w') as file:
        file.writelines(result)

except requests.exceptions.RequestException as e:
    logger.error(f"Error: {e}")

except json.JSONDecodeError as e:
    logger.error(f"Error: Unable to parse JSON data: {e}")