from typing import Any, Dict, List

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transaction_dict: List[Dict[str, Any]], currency_code: str = "USD") -> Any:
    """Функция принимает на вход список словарей, представляющих транзакции и
    возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""

    if not isinstance(transaction_dict, list):
        raise TypeError("Фильтрация возможна только по списку словарей!")
    for transaction in transaction_dict:
        transactions_currency_code = transaction.get("operationAmount").get("currency").get("code", "Error")
        if transactions_currency_code == "":
            raise ValueError("В списке словарей нет кода валют!")

        elif transactions_currency_code == currency_code:
            yield transaction


# usd_transactions = filter_by_currency(transactions, "USD")
#
# for _ in range(10):
#     print(next(usd_transactions))


def transaction_descriptions(transactions_descript: Any) -> Any:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    if not isinstance(transactions_descript, list):
        raise TypeError("Фильтрация возможна только по списку словарей!")
    for transaction in transactions:
        yield transaction.get("description")


descriptions = transaction_descriptions(transactions)

# for _ in range(5):
#     print(next(descriptions))


def card_number_generator(start: int, stop: int) -> Any:
    """Функция выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,где X — цифра номера карты."""
    for number in range(int(start), int(stop) + 1):
        card_number_generators = str(number).zfill(16)  # заполняем нулями до 16 цифр
        formated_card_number = (
            f"{card_number_generators[:4]} {card_number_generators[4:8]} "
            f"{card_number_generators[8:12]} {card_number_generators[12:]}"
        )
        yield formated_card_number


#
# for card_number in card_number_generator(1, 5):
#     print(card_number)
