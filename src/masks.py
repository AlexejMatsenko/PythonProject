def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера."""
    list_card_number = []

    for i in str(card_number):

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



def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера."""
    new_account_number = []
    for i in str(account_number):
        if i.isalpha():
            raise ValueError("Номер должен состоять из цыфр")
        if len(account_number) > 20 or len(account_number) < 20:
            raise ValueError("Количество цыфр карты должно быть 20")
        new_account_number.append(i)
    new_account_number[-6:-4] = ["*", "*"]
    return "".join(new_account_number[-6:])


# if __name__ == "__main__":
#     print(get_mask_card_number("7000792289606361"))
#     print(get_mask_card_number("1234792289605554"))
