
from unittest.mock import mock_open, patch

from src.utils import get_transactions_from_json

mock_file = mock_open(read_data=
                      '[{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",'
                      ' "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},'
                      ' "description": "Перевод организации", "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"}]')


# Тест на проверку работы функции
@patch("builtins.open", mock_file)
def test_read_json_file_valid() -> None:
    with patch("json.load", return_value=
    [
        {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
         "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод организации", "from": "Maestro 1596837868705199",
         "to": "Счет 64686473678894779589"}]) as mock_file:
        assert get_transactions_from_json("../data/operations.json") == [
            {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
             "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
             "description": "Перевод организации", "from": "Maestro 1596837868705199",
             "to": "Счет 64686473678894779589"}]


# Тест, если файл не найден
@patch("builtins.open")
def test_read_json_file_not_found(mock_open) -> None:
    mock_open.side_effect = FileNotFoundError
    result = get_transactions_from_json("data/operations.json")
    assert result == []

mock_file_errror = mock_open(read_data=None)
