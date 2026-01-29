from masks import get_mask_account, get_mask_card_number


def mask_account_card(num_card_account: str):
    """Функция принимает название карты,номер или счёт,"""
    num_card_account_split = num_card_account.split()
    number = num_card_account_split[-1]
    card = []
    for i in num_card_account_split:
        if i.isalpha():
            card.append(i)
            if len(number) == 16:
                numbers = get_mask_card_number(number)
            elif len(number) == 20:
                numbers = get_mask_account(number)
    return f" {" ".join(card)} {numbers}"


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 64686473678894779589"))