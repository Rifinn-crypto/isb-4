import hashlib
from typing import Union, Optional
import multiprocessing as mp
from tqdm import tqdm


def check_card_number(main_card_number_part: int, original_hash: str, bins: list, last_numbers: str) -> Union[str, bool]:
    """
    Функция подбирает номер карты и проверяет истинное значение хэша и хэша номера карты
    :param main_card_number_part: неизвестная часть карты
    :param original_hash: хэш функции желаемой карты
    :param bins: список BINs
    :param last_numbers: 4 последние цифры карты
    :return: номер карты если хэш совпал, иначе false
    """
    for card_bin in bins:
        card_number = f"{card_bin}{main_card_number_part:06d}{last_numbers}"
        if hashlib.sha1(card_number.encode()).hexdigest() == original_hash:
            return card_number
    return False


def enumerate_card_number(original_hash: str, bins: list, last_numbers: str, pools) -> Optional[str]:
    """
    Функция пересчитывает истинный номер карты по известному хэшу
    :param original_hash: хэш функции желаемой карты
    :param bins: список BINs
    :param last_numbers: 4 последние цифры карты
    :param pools: количество процессов
    :return: номер карты если был найден, иначе None
    """
    arguments = []
    for i in range(1000000):
        arguments.append((i, original_hash, bins, last_numbers))
    with mp.Pool(processes=pools) as p:
        for result in p.starmap(
            check_card_number,
            tqdm(arguments, desc="Процесс нахождения номера карты: ", ncols=130, colour="green"),
        ):
            if result:
                p.terminate()
                return result
    return None