def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """Функция фильтрует список словарей по ключу state"""
    filtered_list = []
    for dictionary in list_of_dicts:
        if dictionary.get("state") == state:
            filtered_list.append(dictionary)
    return filtered_list


def sort_by_date(list_of_dicts: list, direction: bool = False) -> list:
    """Функция сортирует словари по дате"""
    sorted_list = sorted(list_of_dicts, key=lambda x: x["date"], reverse=direction)
    return sorted_list
