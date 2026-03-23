from src.utils import get_transactions_from_json
import requests
import os

from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
def sum_amount_currency_code(read_file):
    for operations in read_file:
        operation_code = operations["operationAmount"]["currency"]["code"]
        if operation_code == "RUB":
            # operation_amount = operations["operationAmount"]["amount"]
            return float(operations["operationAmount"]["amount"])
        elif operation_code in ["USD", "EUR"]:
            to = "RUB"
            from_ = operation_code
            amount = operations['operationAmount']['amount']

            url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"

            headers = {"apikey": API_KEY}

            response = requests.get(url, headers=headers)
            result = response.json()
            return float(result['result'])


if __name__ == '__main__':
    read_file = get_transactions_from_json(file_path="../data/operations.json")
    print(sum_amount_currency_code(read_file))

