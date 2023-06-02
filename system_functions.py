import logging
import json


logger = logging.getLogger()
logger.setLevel("INFO")


def load_settings(settings_file: str) -> dict:
    settings = None
    try:
        with open(settings_file) as json_file:
            settings = json.load(json_file)
        logging.info(f'Настройки считаны из файла "{settings_file}"')
    except OSError as err:
        logging.warning(f'Ошибка при чтении настроек из файла "{settings_file}"\n{err}')
    return settings


def load_text(file_name: str) -> str:
    try:
        with open(file_name, mode="r") as text_file:
            text = text_file.read()
        logging.info(f'Файл "{file_name}" прочитан')
    except OSError as err:
        logging.warning(f'Ошибка при чтении файла "{file_name}"\n"{err}"')
    return text


def write_text(text: str, file_name: str) -> None:
    try:
        with open(file_name, mode="w") as text_file:
            text_file.write(text)
        logging.info(f'Текст записан в файл "{file_name}"')
    except OSError as err:
        logging.warning(f'Ошибка при записи в файл "{file_name}"\n"{err}"')


def load_statistics(file_name: str) -> dict:
    statistics = {}
    try:
        with open(file_name, mode="r") as text_file:
            lines = text_file.readlines()
    except OSError as err:
        logging.warning(f'Данные не были загружены из файла "{file_name}"\n{err}')
    for line in lines:
        line = list(map(float, line.split()))
        statistics[line[0]] = line[1]
    logging.info(f'Данные загрузились из файла "{file_name}"')
    return statistics


def add_statistics(pools: int, time: float, file_name: str) -> None:
    try:
        with open(file_name, mode="a") as text_file:
            text_file.write(f"{pools} {time}\n")
        logging.info(f'Данные добавлены в файл "{file_name}"')
    except OSError as err:
        logging.warning(f'Данные не добавлены в файл "{file_name}"\n{err}')