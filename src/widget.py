import re
from typing import Any

# Импортируем функции из модуля masks
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(num_card_account: Any):
    """Функция принимает название карты и номер или счёт и номер,
    отделяем цифры и импортируем для маскировки."""

    num_card_account_split = num_card_account.split()
    number = []
    letter_card = []
    mask_number = []
    number_account: Any = []
    number_card: Any = []

    if num_card_account == "":
        raise ValueError(
            "Небходимо ввести название карты или счёта,и соответствующий номер"
        )

    for i in num_card_account_split:
        if i.isalpha():
            letter_card.append(i)
        elif i.isdigit():
            number += i
        if len(number) == 16:
            number_card = number
            mask_number = get_mask_card_number(number_card)
        elif len(number) == 20:
            number_account = number
            mask_number = get_mask_account(number_account)
    if len(number_account) != 20 and len(number_card) != 16:
        raise ValueError("Номер счёта должен содержать 20 цифр,а номер карты 16")

    return f"{" ".join(letter_card)} {mask_number}"


def get_date(data: str) -> Any:
    """Принимает на вход строку с датой в смешанном формате, и возвращаем 'ДД.ММ.ГГГГ'"""
    data_new = data.split()
    if not re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}", data):
        raise ValueError("Некорректный формат даты")

    formated_date = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", data_new[0])

    return formated_date[:10]

#
# if __name__ == "__main__":
#     print(mask_account_card("Master Card 7000792289606361"))
