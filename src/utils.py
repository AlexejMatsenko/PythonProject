import json

from src.logging_config import setup_logging

logger = setup_logging("utils")


def get_transactions_from_json(file_path: str) -> list:
    """
    Функция принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            transactions = json.load(f)  # Десериализация JSON-данных в Python-объект
            logger.info("Успешное чтение файла")
            if not isinstance(transactions, list):
                raise TypeError("JSON-файл должен содержать список.")
            return transactions

    except FileNotFoundError:
        logger.error("Файл не найден")
        print(f"Ошибка: Файл не найден по пути {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error("Файл не содержит список,либо пустой")
        print(f"Ошибка: Файл '{file_path}' пустой.")
    return []


if __name__ == "__main__":

    print(get_transactions_from_json("../data/operations.json"))
