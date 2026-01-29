# Импортируем функции из модуля masks
import re

from masks import get_mask_account, get_mask_card_number


def mask_account_card(num_card_account: str) -> str:
    """Функция принимает название карты и номер или счёт и номер
    отделяем цыфры и импортируем для маскировки."""
    num_card_account_split = num_card_account.split()
    number = num_card_account_split[-1]
    card = []
    for i in num_card_account_split:
        if i.isalpha():
            card.append(i)
            if len(number) == 16:
                result = get_mask_card_number(number)
            elif len(number) == 20:
                result = get_mask_account(number)
    return f" {" ".join(card)} {result}"


def get_date(data: str) -> str:
    """Принимает на вход строку с датой в смешанном формате, и возвращаем 'ДД.ММ.ГГГГ'"""
    data_new = data.split()
    formated_date = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", data_new[0])
    return formated_date[:10]


print(get_date("2024-03-11T02:26:18.671407"))

if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 64686473678894779589"))
