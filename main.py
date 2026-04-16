from src.generators import filter_by_currency

from src.processing import filter_by_state, sort_by_date

from src.bank_operations import process_bank_search
from src.utils import get_transactions_from_json, read_csv_file, read_excel_file


def main():
    while True:
        print(f"Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
              f"Выберите необходимый пункт меню:\n"
              f"1. Получить информацию о транзакциях из JSON-файла\n"
              f"2. Получить информацию о транзакциях из CSV-файла\n"
              f"3. Получить информацию о транзакциях из XLSX-файла\n")


        number_file = int(input(f"Введите соответствующую цыфру: "))

        if number_file == 1:
            print(f"Для обработки выбран JSON-файл.")
            file_patches = get_transactions_from_json("/data/operations.json")
            break
        elif number_file == 2:
            print(f"Для обработки выбран CSV-файл.")
            file_patches = read_csv_file("/data/transactions.csv")
            break
        elif number_file == 3:
            print(f"Для обработки выбран XLSX-файл.")
            file_patches = read_excel_file("/data/transactions_excel.xlsx")
            break
        else:
            print('Неоходимо ввести 1, 2 или 3')
            continue

    while True:
        status = ["EXECUTED", "CANCELED", "PENDING"]
        status_input = input(f"Введите статус, по которому необходимо выполнить фильтрацию.\n"
                                   f"Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:\n")

        if status_input.upper() in status:
            code_states = status_input
            by_status = filter_by_state(file_patches, code_states)
            print(f"Операции отфильтрованы по статусу {status_input}")
            break
        else:
            print(f"Статус операции {status_input} недоступен.\n")
            continue

    while True:

        date_operation_input = input("Отсортировать операции по дате? Да/Нет\n").lower()
        code_currency_rub = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
        filter_descript = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()


        if date_operation_input == "да":
            reversrd_date = input("Отсортировать по возрастанию или по убыванию?\n").lower()
            if reversrd_date == "по возрастанию":
                date_operation = sort_by_date(by_status, False)
            elif reversrd_date == "по убыванию":
                date_operation = sort_by_date(file_patches, True)
        elif date_operation_input == "нет":
            break

        if code_currency_rub == 'да':
            filter_by_currency_code = filter_by_currency(date_operation, "RUB")
            filter_by_currency_code = filter_by_currency(by_status, "RUB")
        elif code_currency_rub == "нет":
            break


        if filter_descript == "да":
            seatch_word = input("По какому слову хотите отфильтровать?:\n")
            if seatch_word:
                filter_descript_word = process_bank_search(filter_by_currency_code, seatch_word)
        elif filter_descript == "нет":
            return by_status

        print("Распечатываю итоговый список транзакций...")

    return filter_descript_word





if __name__ == "__main__":
    print(main())





