import re
from typing import Any, Dict, List


def filter_by_state(
    by_states: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """Функция принимает список словарей и опционально значение для ключа state
     (по умолчанию 'EXECUTED'), и возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""

    list_state_executed = []  # Списки для отсортированных ключей
    list_state_other = []
    for by_state in by_states:
        if not by_state["state"] or by_state["state"] == "":
            raise KeyError("Необходимы данные по ключу")
        if by_state["state"] == state:  # Сортировка по ключу по умолчанию
            list_state_executed.append(by_state)
        else:
            list_state_other.append(by_state)  # Сортировки по другим ключам
    return list_state_executed or list_state_other


def sort_by_date(
    operation: List[Dict[str, Any]], descending: bool = True
) -> List[Dict[str, Any]]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание), и возвращает новый список, отсортированный по дате"""
    for operations in operation:
        if operations == [] or operations["date"] == "":
            raise TypeError("Дата отсутствует")
        if not re.match(
            r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}", operations["date"]
        ):
            raise ValueError("Некорректный формат даты")
    sorted_dates = sorted(operation, key=lambda x: x["date"], reverse=descending)
    return sorted_dates
