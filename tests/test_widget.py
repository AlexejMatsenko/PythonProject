import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "num_card_account, expected",
    [
        ("Master Card 7000792289606361", "Master Card 7000 79** **** 6361"),
        ("Visa 7000792289606361", "Visa 7000 79** **** 6361"),
    ],
)
def test_mask_account_card(num_card_account, expected):
    assert mask_account_card(num_card_account) == expected


def test_mask_account_card_letter():
    with pytest.raises(ValueError):
        mask_account_card("fgfgfg")


def test_mask_account_card_number_len():
    with pytest.raises(ValueError):
        mask_account_card("")


# Параметризация теста для get_date
@pytest.mark.parametrize(
    "data, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2020-01-01T00:00:00.000000", "01.01.2020"),
        ("1999-12-31T23:59:59.999999", "31.12.1999"),
        (" ", None),
    ],
)
def test_get_date_various_formats(data: str, expected: str) -> None:
    if expected is None:
        with pytest.raises(ValueError):
            get_date(data)
    else:
        assert get_date(data) == expected
