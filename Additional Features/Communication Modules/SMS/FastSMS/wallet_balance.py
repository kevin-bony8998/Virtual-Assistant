import requests
import math

url = "https://www.fast2sms.com/dev/wallet"

headers = {
    'authorization': "iZWfNxwR5OIbrtpCkHUq3eB0sY81QnvcgPh6VaDJj2SoAEldu7voO93nRemWXqYxCyMBK5LraGU7ht6j",
    }

response = requests.request("POST", url, headers=headers)

print(response)
print(response.text)
params = response.text.split(",")
acc_details = params[1].split(":")
acc_bal = acc_details[1][1:-2]
print(float(acc_bal))

rem_texts = (float(acc_bal)/0.2)

print(round(rem_texts))