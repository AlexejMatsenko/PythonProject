from unittest.mock import Mock, patch
from src.external_api import sum_amount_currency_code
import requests

@patch("src.external_api.requests.get")
def test_amount_rub_convert(mock_get) -> None:
    mock_response = Mock()
    mock_response.json.return_value = {"result": 93.5}
    mock_get.return_value = mock_response

    operation = [{"operationAmount": {"amount": "1", "currency": {"code": "USD"}}}]

    # Вызов тестируемой функции
    result = sum_amount_currency_code(operation)

    # Проверка результата
    assert result == 93.5

@patch("src.external_api.requests.get")
def test_amount_rub(mock_get) -> None:
    mock_response = Mock()
    mock_response.json.return_value = {"result": 100.0}
    mock_get.return_value = mock_response

    operation = [{"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}]

    # Вызов тестируемой функции
    result = sum_amount_currency_code(operation)

    # Проверка результата
    assert result == 100.0

# Тест на ошибку HTTP
@patch("src.external_api.requests.get")
def test_amount_rub_convert_status(mock_get):
    # Определение данных транзакции
    transaction = [{"operationAmount": {"currency": {"code": "USD"}, "amount": "100"}}]
    mock_response = mock_get.return_value
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Mocked HTTP error")

    # Проверка, что функция возвращает None
    result = sum_amount_currency_code(transaction)
    assert result == None

    # Убедиться, что raise_for_status был вызван
    mock_get.return_value.raise_for_status.assert_called_once()


@patch("src.external_api.requests.get")
def test_request_exception(mock_get):
    # Настраиваем mock для выбрасывания исключения
    mock_get.side_effect = requests.exceptions.RequestException("Test exception")

    result = sum_amount_currency_code([{"operationAmount": {"currency": {"code": "USD"}, "amount": "100"}}])

    # Проверяем, что функция возвращает None в случае исключения
    assert result == None


@patch("src.external_api.requests.get")
def test_key_error(mock_get) -> None:
    # Имитация ответа API с отсутствующим ключом 'result'
    mock_get.return_value.json.return_value = {}
    mock_get.return_value.status_code = 200

    # Данные транзакции без нужного ключа
    transaction = [{"operationAmount": {"currency": {"code": "USD"}, "amount": "100"}}]

    try:
        sum_amount_currency_code(transaction)
    except KeyError:
        print("KeyError caught as expected")
