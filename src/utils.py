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

import pandas as pd


def read_csv_file(file_csv_path: str) -> list[dict]:
    """Функция принимает путь к файлу csv, и возвращает список словарей"""
    try:
        df = pd.read_csv(file_csv_path, encoding="utf-8-sig", delimiter=";")
        dict_list = df.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути {file_csv_path}")
        return []
    return dict_list


def read_excel_file(file_excel: str) -> list[dict]:
    """Функция принимает путь к файлу excel, и возвращает список словарей"""
    try:
        df_excel = pd.read_excel(file_excel)
        dict_list = df_excel.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути {file_excel}")
        return []
    except ValueError as e:
        raise ValueError(f"Ошибка при чтении файла Excel: {e}")

    return dict_list


if __name__ == "__main__":
    print(read_csv_file("../data/transactions.csv"))
# print(read_excel_file("../data/transactions_excel.xlsx"))
    print(get_transactions_from_json("../data/operations.json"))
