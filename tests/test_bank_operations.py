import pytest

from src.bank_operations import process_bank_operations, process_bank_search


@pytest.fixture
def non_matching():
    return [
        {"id": 1, "description": "Купил торт", "category": "Продукты"},
        {"id": 2, "description": "Заказал наушники", "category": "Товары"},
        {"id": 3, "description": "Бусы", "category": "Подарки"},
    ]


def test_process_bank_operations_no_match(non_matching):
    # Тестируем несовпадение описания с категориями
    category = ["Покупки"]
    expected_result = {}
    result = process_bank_operations(non_matching, category)
    assert result == expected_result


@pytest.fixture
def matching():
    return [{"id": 1, "description": "Купил торт", "category": "Продукты"}]
    # {"id": 2, "description": "Заказал наушники", "category": "Товары"},
    # {"id": 3, "description": "Бусы", "category": "Подарки"}]


def test_process_bank_operations(matching):
    category = ["Продукты"]
    expected_result = {"Продукты": 1}
    result = process_bank_operations(matching, category)
    assert result == expected_result


def data_():
    return [
        {"description": "Food"},
        {"description": "Transport"},
        {"description": "Food"},
        {"description": "Entertainment"},
        {"description": "Payment to John"},
        {"description": "Transfer to bank"},
        {"description": "Payment to Jane"},
    ]


@pytest.mark.parametrize(
    "description_word, data_frm",
    [
        ("Payment", [{"description": "Payment to Jane"}, {"description": "Payment to John"}]),
        ("payment", [{"description": "Payment to Jane"}, {"description": "Payment to John"}]),
        ("Groceries", []),
        ([], []),
    ],
)
def test_process_bank_search(data_, description_word, data_frm):
    result = process_bank_search(data_, description_word)
    assert result == data_frm
