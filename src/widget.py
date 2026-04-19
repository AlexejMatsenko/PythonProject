import re
from typing import Any

# Импортируем функции из модуля masks
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(num_card_account: str) -> str | None:
    """Функция принимает название карты и номер или счёт и номер,
    отделяем цифры и импортируем для маскировки."""

    if num_card_account and isinstance(num_card_account, str):
        *words, number = num_card_account.split()
        if len(number) == 16:
            mask_number = get_mask_card_number(number)
        elif len(number) == 20:
            mask_number = get_mask_account(number)
        else:
            raise ValueError("Некорректное количество цифр")
        return f"{" ".join(words)} {mask_number}"


def get_date(data: str) -> Any:
    """Принимает на вход строку с датой в смешанном формате, и возвращаем 'ДД.ММ.ГГГГ'"""
    data_new = data.split()
    if not re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}", data):
        raise ValueError("Некорректный формат даты")

    formated_date = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", data_new[0])

    return formated_date[:10]


#
# if __name__ == "__main__":
#     print(mask_account_card("Visa Platinum 1246377376343588"))
