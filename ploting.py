import os
import logging
import matplotlib.pyplot as plt

logger = logging.getLogger()
logger.setLevel("INFO")


def visualize_statistics(statistics: dict, settings: dict) -> None:
    """
    Функция создает график по данным
    :param statistics: данные для построения
    :param settings: входные данные
    :return: None
    """
    plt.figure(figsize=(18, 9))
    plt.rcParams["font.size"] = "30"
    plt.ylabel("Time, s")
    plt.xlabel("Processes")
    plt.title("Statistics")
    pools, work_times = statistics.keys(), statistics.values()
    plt.bar(pools, work_times, color="purple", width=0.8)
    plt.savefig(settings['stat'])
    logging.info(f'График сохранен')