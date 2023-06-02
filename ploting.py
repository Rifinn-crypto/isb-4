import os
import logging
import matplotlib.pyplot as plt

logger = logging.getLogger()
logger.setLevel("INFO")


def visualize_statistics(statistics: dict, visual_directory: str) -> None:
    """
    Функция создает график по данным
    :param statistics: данные для построения
    :param visual_directory: путь к папке
    :return: None
    """
    fig = plt.figure(figsize=(40, 30))
    plt.rcParams["font.size"] = "30"
    plt.ylabel("Время работы, с", fontsize=24)
    plt.xlabel("Количество процессов", fontsize=24)
    plt.title("График зависимости времени от количества процессов", fontsize=60)
    pools, work_times = statistics.keys(), statistics.values()
    plt.bar(pools, work_times, color="purple", width=0.8)
    plt.savefig(os.path.join(visual_directory, "statistics.png"))
    logging.info(f'График сохранен в папку "{visual_directory}"')