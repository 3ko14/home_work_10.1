import logging
from src.setup_logger import setup_logger
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "masks.log")
logger = setup_logger("masks", file_path_1)


def get_mask_kard(number: str) -> str:
    """Функция принимает строку и возвращает замаскированный номер карты"""
    logger.info("Принимаем строку и возвращаем замаскированный номер карты")
    new_string = f"{number[0:4]} {number[4:6]}** **** {number[12:]}"
    return new_string


def get_mask_account(number: str) -> str:
    """Функция принимает строку и возвращает замаскированный номер счёта"""
    logger.info("Принимаем строку и возвращаем замаскированный номер счета")
    new_string = f"**{number[-4:]}"
    return new_string
