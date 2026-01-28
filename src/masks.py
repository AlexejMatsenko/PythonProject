from typing import Union


def get_mask_card_number(card_number: Union[int | str]) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера."""
    list_card_number = []
    for i in str(card_number):
        list_card_number.append(i)
        if len(list_card_number) == 4:
            list_card_number.append(" ")
        elif len(list_card_number) == 9:
            list_card_number.append(" ")
        elif len(list_card_number) == 14:
            list_card_number.append(" ")
            list_card_number[7:14] = ["*", "*", " ", "*", "*", "*", "*"]

    return "".join(list_card_number)


card_numbers = 7000792289606361
print(get_mask_card_number(card_numbers))


def get_mask_account(account_number: int | str) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера."""
    list_account_number = []
    for i in str(account_number):
        list_account_number.append(i)
    list_account_number[-6:-4] = ["*", "*"]
    return "".join(list_account_number[-6:])


account_numbers = 73654108430135874305
print(get_mask_account(account_numbers))
