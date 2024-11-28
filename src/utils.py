import json
from src.setup_logger import setup_logger
import os
from src.external_api import currency_conversion


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "utils.log")
logger = setup_logger("utils", file_path_1)

def transaction_amount(file_path: str) -> float:
    """Функция которая выводит сумму транзакции"""
    try:
        logger.info(f"Выводим сумму транзакции")
        with open(file_path, "r", encoding="utf-8") as file:
            repos = json.load(file)
        if isinstance(repos, list):
            return repos
        else:
            return []
    except Exception as e:
        print(f"Ошибка {e}")
        logger.error(f"Произошла ошибка {e}")
        return []