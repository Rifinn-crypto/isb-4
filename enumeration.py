import hashlib
from typing import Union, Optional
import multiprocessing as mp
from tqdm import tqdm


def check_card_number(main_card_number_part: int, original_hash: str, bins: list, last_numbers: str) -> Union[str, bool]:
    for card_bin in bins:
        card_number = f"{card_bin}{main_card_number_part:06d}{last_numbers}"
        if hashlib.sha1(card_number.encode()).hexdigest() == original_hash:
            return card_number
    return False


def enumerate_card_number(original_hash: str, bins: list, last_numbers: str, pools) -> Optional[str]:
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