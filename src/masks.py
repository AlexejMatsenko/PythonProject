from typing import Any


def get_mask_card_number(card_number: Any) -> Any:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера."""
    list_card_number = []
    if card_number == "":
        raise ValueError("Ничего не указано")
    for i in card_number:

        if i.isalpha():
            raise ValueError("Номер должен состоять из цифр")
        if len(card_number) > 16 or len(card_number) < 16:
            raise ValueError("Количество цифр карты должно быть 16")
        list_card_number.append(i)
        if len(list_card_number) == 4:
            list_card_number.append(" ")
        elif len(list_card_number) == 9:
            list_card_number.append(" ")
        elif len(list_card_number) == 14:
            list_card_number.append(" ")
            list_card_number[7:14] = ["*", "*", " ", "*", "*", "*", "*"]

    return "".join(list_card_number)


def get_mask_account(account_number: Any) -> Any:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера."""
    new_account_number = []
    if account_number == "":
        raise ValueError("Ничего не указано")
    for j in account_number:
        if j.isalpha():
            raise ValueError("Номер должен состоять из цифр")
        if len(account_number) > 20 or len(account_number) < 20:
            raise ValueError("Количество цифр карты должно быть 20")
        new_account_number.append(j)
    new_account_number[-6:-4] = ["*", "*"]
    return "".join(new_account_number[-6:])
