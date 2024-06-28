from src.masks import get_mask_account, get_mask_kard


def mask_account_card(number: str) -> str:
    """Функция принимает строку и маскирует номер карты/счета"""
    if len(number.split()[-1]) == 16:
        new_number = get_mask_kard(number.split()[-1])
        result = f"{number[:-16]}{new_number}"
    elif len(number.split()[-1]) == 20:
        new_number = get_mask_account(number.split()[-1])
        result = f"{number[:-20]}{new_number}"
    return result


def get_data(old_data: str) -> str:
    """Функция принимает строку и возвращает число месяц год"""
    data_slice = old_data[0:10].split("-")
    result = ".".join(data_slice[::-1])
    return result
