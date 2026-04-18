from src.bank_operations import process_bank_operations,process_bank_search
import pytest
@pytest.fixture

def non_matching():
    return [{"id": 1, "describtion": "Купил торт", "category": "Продукты"},
            {"id": 2, "describtion": "Заказал наушники", "category": "Товары"},
            {"id": 3, "describtion": "Бусы", "category": "Подарки"}]

def test_process_bank_operations_no_match(non_matching):
    # Тестируем несовпадение описания с категориями
    category = ["Покупки", "Перевод", "Оплата"]
    expected_result = {"Покупки": 0, "Перевод": 0, "Оплата": 0}
    result =  process_bank_operations(non_matching, category)
    assert result == ""



def data_():
    return [
        {'description': 'Food'},
        {'description': 'Transport'},
        {'description': 'Food'},
        {'description': 'Entertainment'},
        {'description': 'Payment to John'},
        {'description': 'Transfer to bank'},
        {'description': 'Payment to Jane'},
    ]

@pytest.mark.parametrize(
    "description_word, data_frm",
    [
       ("Payment", [{'description': 'Payment to Jane'},{'description': 'Payment to John'}]),
       ("payment", [{'description': 'Payment to Jane'},{'description': 'Payment to John'}]),
       ("Groceries", []),
       ([], []),
    ],
)
def test_process_bank_search(data_, description_word, data_frm):
    result = process_bank_search(data_, description_word)
    assert result == data_frm