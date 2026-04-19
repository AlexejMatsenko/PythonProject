from unittest.mock import patch

import pandas as pd
import pytest

from src.utils import read_csv_file, read_excel_file


@patch("pandas.read_csv")
def test_pd_config_csv(mock_read_csv):
    test_data = {
        "id": [650703.0],
        "state": ["EXECUTED"],
        "date": ["2023-09-05T11:30:32Z"],
        "amount": [16210.0],
        "currency_name": ["Sol"],
        "currency_code": ["PEN"],
        "from": ["Счет 58803664561298323391"],
        "to": ["Счет 39745660563456619397"],
        "description": ["Перевод организации"],
    }

    # Создаем DataFrame из test_data
    mock_read_csv.return_value = pd.DataFrame(test_data)

    # Ожидаемый результат
    expected_result = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]

    # Вызываем функцию и проверяем результат
    result = read_csv_file("file_path.csv")
    assert result == expected_result


@patch("builtins.open")
def test_read_json_file_not_found(mock_open) -> None:
    mock_open.side_effect = FileNotFoundError
    result = read_csv_file("data/operations.csv")
    assert result == []


@patch("src.reading_files.pd.read_excel")
def test_pd_config_excel(mock_read_excel):
    # Создаем пример данных, которые будет возвращать мок
    mock_df = pd.DataFrame(
        {
            "id": [650703.0],
            "state": ["EXECUTED"],
            "date": ["2023-09-05T11:30:32Z"],
            "amount": [16210.0],
            "currency_name": ["Sol"],
            "currency_code": ["PEN"],
            "from": ["Счет 58803664561298323391"],
            "to": ["Счет 39745660563456619397"],
            "description": ["Перевод организации"],
        }
    )
    mock_read_excel.return_value = mock_df

    # Вызываем функцию и проверяем результат
    expected_result = mock_df.to_dict(orient="records")
    result = read_excel_file("file_path.xlsx")

    assert result == expected_result


@patch("src.reading_files.pd.read_excel")
def test_read_excel_file_raises_value_error(mock_read_excel) -> None:
    mock_read_excel.side_effect = ValueError("Ошибка при чтении файла Excel")
    with pytest.raises(ValueError, match="Ошибка при чтении файла Excel"):
        read_excel_file("non_existent_file.xlsx")
