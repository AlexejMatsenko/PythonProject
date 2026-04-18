import re
from collections import Counter
from typing import Dict, List

from src.utils import read_csv_file, read_excel_file


def process_bank_search(data: List[Dict[str, str]], search: str) -> list[Dict[str, str]] | None:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    и возвращает список словарей, у которых в описании есть строка 'search'"""

    filter_description = [
        x for x in data if x.get("description") and re.search(search, str(x.get("description")), flags=re.IGNORECASE)
    ]
    if len(filter_description) == 0:
        return []
    #
    # read_csv = read_csv_file("../data/transactions.csv")
    # read_excel = read_excel_file("../data/transactions.xlsx")

    return filter_description


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    и возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""

    list_description = []
    if categories is None:
        return {}
    else:
        for i in categories:
            description = [
                x for x in data if x["description"] and re.search(i, str(x["description"]), flags=re.IGNORECASE)
            ]

            for j in description:
                list_description.append(j["description"])
                # contered = Counter(list_description)
        return dict(Counter(list_description))
        # return dict_description


if __name__ == "__main__":
    #
    read_csv = read_csv_file("../data/transactions.csv")
    read_excel = read_excel_file("../data/transactions_excel.xlsx")
    categoriy = ["Открытие вклада", "Перевод со счета на счет", "Перевод с карты на карту", "Перевод организации"]
    categoriy = ["перевод"]
    print(process_bank_search(read_excel, search="открытие"))
    print(process_bank_operations(read_csv, categoriy))
