import os
from typing import Any

import requests
from dotenv import load_dotenv

from src.utils import get_transactions_from_json

load_dotenv()
API_KEY = os.getenv("API_KEY")


def sum_amount_currency_code(read_files: Any) -> float | None:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
     и конвертации суммы операции в рубли"""

    for operations in read_files:
        operation_code = operations["operationAmount"]["currency"]["code"]
        if operation_code == "RUB":
            operation_amount = operations["operationAmount"]["amount"]
            return float(operation_amount)
        elif operation_code == "USD" or "EUR":
            to = "RUB"
            from_ = operation_code
            amount = operations["operationAmount"]["amount"]

            url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"

            headers = {"apikey": API_KEY}

            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                result = response.json()
                return float(result["result"])
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
            except requests.exceptions.RequestException as err:
                print(f"Other error occurred: {err}")
            except KeyError:
                print("Unexpected response format")
    return None


read_file = get_transactions_from_json("../data/operations.json")
# if __name__ == "__main__":
#
# print(sum_amount_currency_code(read_file))
# print(
#     sum_amount_currency_code(
#         [
#             {
#                 "id": 41428829,
#                 "state": "EXECUTED",
#                 "date": "2019-07-03T18:35:29.512364",
#                 "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
#                 "description": "Перевод организации",
#                 "from": "MasterCard 7158300734726758",
#                 "to": "Счет 35383033474447895560",
#             }
#         ]
#     )
# )
# print(
#     sum_amount_currency_code(
#         [
#             {
#                 "id": 15948212,
#                 "state": "EXECUTED",
#                 "date": "2018-12-23T11:47:52.403285",
#                 "operationAmount": {"amount": "47408.20", "currency": {"name": "USD", "code": "USD"}},
#                 "description": "Перевод с карты на карту",
#                 "from": "МИР 8665240839126074",
#                 "to": "Maestro 3000704277834087",
#             }
#         ]
#     )
# )
#     print(
#         sum_amount_currency_code(
#             [
#                 {
#                     "id": 176798279,
#                     "state": "CANCELED",
#                     "date": "2019-04-18T11:22:18.800453",
#                     "operationAmount": {"amount": "73778.48", "currency": {"name": "руб.", "code": "RUB"}},
#                     "description": "Открытие вклада",
#                     "to": "Счет 90417871337969064865",
#                 }
#             ]
#         )
#     )
