import pytest


@pytest.fixture()
def account_numbers1():
    return "63614566", "1234567891238899456700000", "73654108430ghghh", ""


# Фикстуры для модуля processing
@pytest.fixture()
# Входные данные сортировки по ключу "state"
def processing_by_state1():
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
    ]


@pytest.fixture()
# Входные данные по неизвестным ключам
def processing_by_state2():
    return [
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 615064591,
            "state": "TESTING",
            "date": "2018-10-14T08:21:33.419441",
        },
    ]


@pytest.fixture()
# Входные данные с отсутсвием информации по date и state
def processing_by_state3():
    return [
        {
            "id": 41428829,
            "state": "",
            "date": "",
        },
        {},
    ]


@pytest.fixture()
# Входные данные с не корректной датой
def processing_by_state4():
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "0000-06-30T02:08:58.425572",
        },
        {"id": 939719570, "state": "EXECUTED", "date": "-06-30T02:08:58.425572"},
    ]
