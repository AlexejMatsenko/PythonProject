import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(generators1):
    """Тест на сортировку по валюте USD"""

    extected_currency = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
    generator = list(filter_by_currency(generators1, "USD"))[:2]
    assert generator == extected_currency


def test_filter_by_currency_2():
    """Тест на отсутствие списка словарей"""
    with pytest.raises(TypeError):
        list(filter_by_currency({}))


def test_filter_by_currency_3():
    """Тест на отсутствие валюты"""
    with pytest.raises(ValueError):
        list(
            filter_by_currency(
                [
                    {
                        "id": 939719570,
                        "state": "EXECUTED",
                        "date": "2018-06-30T02:08:58.425572",
                        "operationAmount": {"amount": "9824.07", "currency": {"name": "", "code": ""}},
                        "description": "Перевод организации",
                        "from": "Счет 75106830613657916952",
                        "to": "Счет 11776614605963066702",
                    }
                ]
            )
        )


def test_transaction_descriptions(generators1):
    """Тест на возвращение описания каждой операции по очереди."""
    result = list(transaction_descriptions(generators1))
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


def test_transaction_descriptions_2():
    """Тест на отсутствие списка словарей"""
    with pytest.raises(TypeError):
        list(transaction_descriptions({}))


def test_card_number_generator():
    """Тест на выход корректно сгенерированных номеров карт"""
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]

    result = [i for i in card_number_generator(1, 5)]
    assert result == expected
