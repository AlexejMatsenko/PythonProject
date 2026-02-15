import pytest

from src.processing import filter_by_state, sort_by_date


# Тестируем функцию filter_by_state различными способами
def test_filter_by_state(processing_by_state1):
    assert filter_by_state(processing_by_state1) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state2(processing_by_state2):
    assert filter_by_state(processing_by_state2) == [
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


def test_filter_by_state3():
    assert filter_by_state([]) == []


def test_filter_by_state4(processing_by_state3):
    with pytest.raises(KeyError):
        assert filter_by_state(processing_by_state3)


# Тестируем функцию sort_by_date


def test_sort_by_date1(processing_by_state1):
    assert sort_by_date(processing_by_state1) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date2(processing_by_state2):
    assert sort_by_date(processing_by_state2) == [
        {
            "id": 615064591,
            "state": "TESTING",
            "date": "2018-10-14T08:21:33.419441",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
    ]


def test_sort_by_date3(processing_by_state3):
    with pytest.raises(TypeError):
        assert sort_by_date(processing_by_state3)


def test_sort_by_date4(processing_by_state4):
    with pytest.raises(ValueError):
        assert sort_by_date(processing_by_state4)
