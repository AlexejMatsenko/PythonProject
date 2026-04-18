import re

from src.bank_operations import process_bank_search
from src.processing import filter_by_state
from src.utils import get_transactions_from_json, read_csv_file, read_excel_file
from src.widget import mask_account_card

# Приветствуем пользователя и предлагаем выбор файлов для дальнейшей работы.
print(
    "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
    "Выберите необходимый пункт меню:\n"
    "1. Получить информацию о транзакциях из JSON-файла\n"
    "2. Получить информацию о транзакциях из CSV-файла\n"
    "3. Получить информацию о транзакциях из XLSX-файла\n"
)


def main():
    # Запрашиваем у пользователя номер файла.
    while True:

        number_file = input("Введите соответствующую цыфру: \n").strip()

        if number_file == "1":
            print("Для обработки выбран JSON-файл.\n")
            file_patches = get_transactions_from_json("../data/operations.json")

            break
        elif number_file == "2":
            print("Для обработки выбран CSV-файл.\n")
            file_patches = read_csv_file("../data/transactions.csv")
            break
        elif number_file == "3":
            print("Для обработки выбран XLSX-файл.\n")
            file_patches = read_excel_file("../data/transactions_excel.xlsx")
            break
        else:
            print("Неоходимо ввести 1, 2 или 3")
            continue
    # Запрос у пользователя статуса для фильтрации
    while True:
        status = ["EXECUTED", "CANCELED", "PENDING"]
        status_input = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:\n"
        )

        if status_input.upper() in status:
            by_status = filter_by_state(file_patches, status_input.upper())
            print(f"Операции отфильтрованы по статусу {status_input.upper()}\n")
            break

        else:
            print(f"Статус операции {status_input} недоступен.\n")
        continue
    # Запрос о необходимости сортировки(если да,то по возрастанию или убыванию.
    while True:
        date_operation_input = input("Отсортировать операции по дате? Да/Нет\n").lower().strip()
        new_dict_sort = []
        if date_operation_input == "нет":
            for i in by_status:
                new_date = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", i.get("date", ""))
                i.update({"date": new_date[:10]})
                new_dict_sort.append(i)
            break
        elif date_operation_input == "да":
            while True:
                reverserd_date = input("Отсортировать по возрастанию или по убыванию?\n").lower().strip()

                if reverserd_date == "по возрастанию":
                    reverse_true = sorted(by_status, key=lambda x: x["date"], reverse=False)
                    for i in reverse_true:
                        new_date = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", i.get("date", ""))
                        i.update({"date": new_date[:10]})
                        new_dict_sort.append(i)
                    break
                elif reverserd_date == "по убыванию":
                    reverse_false = sorted(by_status, key=lambda x: x["date"], reverse=True)
                    for i in reverse_false:
                        new_date = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", i.get("date", ""))
                        i.update({"date": new_date[:10]})
                        new_dict_sort.append(i)

                    break
                elif reverserd_date != "по возрастанию" or reverserd_date != "по убыванию":
                    print("Некорректный ввод")
            break
        elif date_operation_input != "да" or date_operation_input != "нет":
            print("Некорректный ввод")
        continue

    # age = [x for x in date_operation if x["date"]]
    # print(age)
    # Запрос у пользователя фильтрации по валюте.
    while True:
        code_currency_rub = input("Выводить только рублевые транзакции? Да/Нет\n").lower().strip()

        if code_currency_rub == "да" and number_file == "1":
            filter_by_currency_code = [
                codes for codes in new_dict_sort if codes.get("operationAmount").get("currency").get("code") == "RUB"
            ]
            break
        elif code_currency_rub == "да" and number_file == "2" or number_file == "3":
            filter_by_currency_code = [codes for codes in new_dict_sort if codes.get("currency_code") == "RUB"]
            break
        elif code_currency_rub == "нет":
            filter_by_currency_code = new_dict_sort
            break
        elif code_currency_rub != "да" or code_currency_rub != "нет":
            print("Некорректный ввод")
        continue

    # Запрос у пользователя о фильтрации по определённому слову.
    while True:

        filter_descript = (
            input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower().strip()
        )
        if filter_descript == "нет":
            filter_seatch_word = process_bank_search(filter_by_currency_code, "")
            print("Распечатываю итоговый список транзакций...\n")
            print(f"Всего банковских операций в выборке:{len(filter_by_currency_code)}\n")
            break
        elif filter_descript == "да":
            while True:
                seatch_word = input("По какому слову хотите отфильтровать?:\n").lower().strip()
                if seatch_word:
                    filter_seatch_word = process_bank_search(filter_by_currency_code, seatch_word)

                if len(filter_seatch_word) > 0:
                    print("Распечатываю итоговый список транзакций...\n")
                    print(f"Всего банковских операций в выборке:{len(filter_seatch_word)}\n")
                    break
                elif len(filter_seatch_word) == 0:
                    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации!")
                    break
            break
        elif filter_descript != "да" or filter_descript != "нет":
            print("Некорректный ввод")
        continue

    # Вывод конечной информации по фильтрации.
    while True:
        my_dict = {}

        for i in filter_seatch_word:
            if number_file == "1":
                my_dict["amount"] = i["operationAmount"]["amount"]
                my_dict["code"] = i["operationAmount"]["currency"]["code"]
            else:
                my_dict["amount"] = i.get("amount")
                # my_dict.update({"amount": my_dict[round(int("amount"))]})
                my_dict["code"] = i.get("currency_code")

            my_dict["date"] = i["date"]
            my_dict["description"] = i["description"]
            my_dict["from"] = mask_account_card(i.get("from", ""))
            my_dict["to"] = mask_account_card(i.get("to", ""))

            print(f"{my_dict["date"]} {my_dict.get("description")}")
            if my_dict.get("from"):
                print(f"{my_dict.get("from")} -> {my_dict.get("to")}")
            else:
                print(my_dict.get("to"))
            print(f"Сумма: {round(float(my_dict["amount"]))} {my_dict.get("code")}.\n")

        break


if __name__ == "__main__":
    print(main())
