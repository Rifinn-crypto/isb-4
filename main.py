import time
import argparse
from system_functions import load_settings, load_text, write_text, add_statistics, load_statistics
from enumeration import enumerate_card_number
from ploting import visualize_statistics
from correction import algorithm_luhn
import multiprocessing as mp
import logging


SETTINGS_FILE = "settings.json"
CORES = mp.cpu_count()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-set", "--settings", default=SETTINGS_FILE, type=str, help="Использование собственного файла с настройками")
    parser.add_argument("-sts", "--statistics", action="store_true", help="Сохраняет статистические данные в файл")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-enu", "--enumeration", nargs="?", const=CORES, type=int, help="Подбирает номер карты по её хэшу (Введите количество порождаемых процессов)")
    group.add_argument("-cor", "--correction", action="store_true", help="Проверяет корректность полученного номера карты")
    group.add_argument("-vis", "--visualization", action="store_true", help="Визуализирует данные из файла")
    args = parser.parse_args()
    settings = load_settings(args.settings)
    if settings:
        if args.enumeration:
            hash = settings["hash"]
            bins = settings["bins"]
            last_numbers = settings["last_numbers"]
            t0 = time.perf_counter()
            card_number = enumerate_card_number(hash, bins, last_numbers, args.enumeration)
            t1 = time.perf_counter()
            if args.statistics:
                add_statistics(args.enumeration, t1 - t0, settings["statistics_file"])
            if card_number:
                logging.info(f"Номер карты был найден: {card_number} ({t1 - t0} секунд потребовалось)")
                write_text(card_number, settings["card_number_file"])
            else:
                logging.info("Номер карты не был найден")
        elif args.visualization:
            statistics = load_statistics(settings["statistics_file"])
            visualize_statistics(statistics, settings["visual_directory"])
        else:
            card_number = load_text(settings["card_number_file"])
            if algorithm_luhn(card_number):
                logging.info(f"Номер карты {card_number} корректен")
            else:
                logging.info(f"Номер карты {card_number} не корректен")