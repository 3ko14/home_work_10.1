def get_mask_kard(number: str) -> str:
    """Функция принимает строку и возвращает замаскированный номер карты"""
    new_string = f"{number[0:4]} {number[4:6]}** **** {number[12:]}"
    return new_string


def get_mask_account(number: str) -> str:
    """Функция принимает строку и возвращает замаскированный номер счёта"""
    new_string = f"**{number[-4:]}"
    return new_string
