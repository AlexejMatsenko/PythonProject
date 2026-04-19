from typing import Any

# from src.logging_config import setup_logging

# logger = setup_logging("masks")


def get_mask_card_number(card_number: Any) -> Any:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера."""
    list_card_number = []
    if card_number == "":
        raise ValueError("Ничего не указано")
    for i in card_number:

        if i.isalpha():
            # logger.error("Номер состоит не только из цифр")
            raise ValueError("Номер должен состоять из цифр")

        if len(card_number) != 16:
            # logger.error("Не соответствие количеству цифр номера карты")
            raise ValueError("Количество цифр карты должно быть 16")

        list_card_number.append(i)
        if len(list_card_number) == 4:
            list_card_number.append(" ")
        elif len(list_card_number) == 9:
            list_card_number.append(" ")
        elif len(list_card_number) == 14:
            list_card_number.append(" ")
            list_card_number[7:14] = ["*", "*", " ", "*", "*", "*", "*"]
    # logger.info("Успешное завершение маскировки")
    return "".join(list_card_number)


def get_mask_account(account_number: Any) -> Any:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера."""
    new_account_number = []
    if account_number == "":
        raise ValueError("Ничего не указано")
    for j in account_number:
        if j.isalpha():
            # logger.error("Счёт состоит не только из цифр")
            raise ValueError("Номер должен состоять из цифр")

        if len(account_number) != 20:
            # logger.error("Не соответствие количеству цифр номера счёта")
            raise ValueError("Количество цифр карты должно быть 20")
        new_account_number.append(j)
    new_account_number[-6:-4] = ["*", "*"]
    # logger.info("Успешное завершение маскировки")
    return "".join(new_account_number[-6:])


# if __name__ == "__main__":
#     print(get_mask_card_number("1234567891236540"))
#     print(get_mask_account("55565269854857231955"))
