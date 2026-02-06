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


def sort_by_date(list_dates: List[Dict[str, Any]], dates: bool = True) -> List[Dict[str, Any]]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание), и возвращает новый список, отсортированный по дате"""

    sorted_dates = sorted(list_dates, key=lambda date: date["date"], reverse=dates)
    return sorted_dates


if __name__ == "__main__":
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )

    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
