import pytest

from src.bank_operations import process_bank_operations, process_bank_search


@pytest.fixture
def non_matching():
    return [
        {"id": 1, "description": "Купил торт", "category": "Продукты"},
        {"id": 2, "description": "Заказал наушники", "category": "Товары"},
        {"id": 3, "description": "Бусы", "category": "Подарки"},
    ]


def test_process_bank_operations_no_category(non_matching):
    # Тестируем несовпадение описания с категориями
    category = ["Покупки"]
    expected_result = {}
    result = process_bank_operations(non_matching, category)
    assert result == expected_result


def test_process_bank_operations_category():
    # Тест на нормальную работу функции
    data = [
        {"description": "Food"},
        {"description": "Transport"},
        {"description": "Food"},
        {"description": "Entertainment"},
    ]
    categories = ["Food", "Transport", "Entertainment"]
    result = process_bank_operations(data, categories)
    assert result == {"Food": 2, "Transport": 1, "Entertainment": 1}


def test_process_bank_search_transactions():
    # Тест на нахождение элементов в списке словарей
    data = [
        {"description": "Payment to John"},
        {"description": "Transfer to bank"},
        {"description": "Payment to Jane"},
    ]
    search = "Payment"
    result = process_bank_search(data, search)
    assert len(result) == 2  # Проверка на кол_во нахождений


def test_process_bank_search_no():
    # Тест на отсутствие словарей в списке
    data = []
    search = "Payment"
    result = process_bank_search(data, search)
    assert result == []
