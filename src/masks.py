# from widget import *

def get_mask_card_number(card_number: str) -> str:
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

# print(get_mask_card_number(numbers))
# print(mask_account_card(number))


def get_mask_account(account_number: int | str) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера."""
    list_account_number = []
    for i in str(account_number):
        list_account_number.append(i)
    list_account_number[-6:-4] = ["*", "*"]
    return "".join(list_account_number[-6:])


# print(get_mask_account(""))

# if __name__ == "__main__":
#     print(get_mask_card_number(numbers))
#     print(get_mask_account(numbers))

