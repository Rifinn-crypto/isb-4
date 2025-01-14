import json

SETTINGS = {
    "card_number_file": "file/card_number.json",
    "statistics_file": "file/statistics.txt",
    "stat": "file/statistics.png",
    "hash": "754a917a9c82f5247412006a5abe1c0eb76e1007",
    "bins": [519998, 529025, 516451, 522327, 522329, 523760, 527652, 528528, 529158, 529460, 529856, 530176, 530429, 531452, 531456, 531855, 531866, 531963, 532465, 534133, 534135, 534299, 510144, 518591, 518640, 540989, 526589, 528154],
    "last_numbers": "0758",
}


if __name__ == "__main__":
    with open("settings.json", "w") as fp:
        json.dump(SETTINGS, fp)