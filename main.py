import requests

api_key = ""
offset = 1000
contract_address = "0xc5c01568a3b5d8c203964049615401aaf0783191"

counter = 0
results = {}

with open('wallets.txt', 'r', encoding='utf-8-sig') as file:
    wallets = [line.strip() for line in file]

try:
    for wallet in wallets:
        url = f"https://api.ftmscan.com//api?module=account&action=txlist&address={wallet}&startblock=0&endblock=99999999&page=1&offset={offset}&sort=asc&apikey={api_key}"
        data = requests.get(url).json()
        response_status = data.get("status")
        response_result = data.get("result")

        if response_status == "1":
            for item in response_result:
                to_value = item.get("to")
                txreceipt_status_value = item.get("txreceipt_status")
                if to_value == contract_address and txreceipt_status_value == "1":
                    counter += 1
            results[wallet] = counter
        else:
            print(response_result)

        counter = 0

    with open("results.txt", "w") as file:
        for wallet, result in results.items():
            file.write(f"{wallet}: {result}\n")

except requests.exceptions.RequestException as e:
    print(f"Непредвиденная ошибка: {e}")
