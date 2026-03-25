import json


def get_transactions_from_json(file_path: str) -> list:
    """
    Функция принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            transactions = json.load(f)  # Десериализация JSON-данных в Python-объект

            if not isinstance(transactions, list):
                raise TypeError("JSON-файл должен содержать список.")

            return transactions
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: Файл '{file_path}' пустой.")
    return []
