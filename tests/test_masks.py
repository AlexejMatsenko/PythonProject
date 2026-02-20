import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тестируем функцию get_mask_card_number
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567855534567", "1234 56** **** 4567"),
        ("7365410843044305", "7365 41** **** 4305"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_len():
    with pytest.raises(ValueError):
        assert get_mask_card_number("7365413014544545454545454545")


def test_get_mask_card_number_letter():
    with pytest.raises(ValueError):
        get_mask_card_number("736541ggg3044f05")


def test_get_mask_card_number_none():
    with pytest.raises(ValueError):
        get_mask_card_number("")


# Тестируем функцию get_mask_account
@pytest.mark.parametrize(
    "card_numbers, expecteds",
    [
        ("70007922896063614566", "**4566"),
        ("12345678912388994567", "**4567"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_get_mask_account(card_numbers, expecteds):
    assert get_mask_account(card_numbers) == expecteds


def test_get_mask_account_len(account_numbers1):
    with pytest.raises(ValueError):
        get_mask_account(account_numbers1[:2])


def test_get_mask_account_letter():
    with pytest.raises(ValueError):
        get_mask_account("5454544ggggg54545447")


def test_get_mask_account_none(account_numbers1):
    with pytest.raises(ValueError):
        get_mask_account(account_numbers1[3])
