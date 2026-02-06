from typing import Any, Dict, List


def filter_by_state(by_states: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция принимает список словарей и опционально значение для ключа state
     (по умолчанию 'EXECUTED'), и возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""

    list_state_executed = []  # Списки для отсортированных ключей
    list_state_other = []
    for by_state in by_states:
        if by_state["state"] == state:  # Сортировка по ключу по умолчанию
            list_state_executed.append(by_state)
        else:
            list_state_other.append(by_state)  # Сортировки по другим ключам
    return list_state_executed or list_state_other