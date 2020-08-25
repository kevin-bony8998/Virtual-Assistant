import requests

url = "https://www.fast2sms.com/dev/bulk"

num="<number>"
querystring = {"authorization":"iZWfNxwR5OIbrtpCkHUq3eB0sY81QnvcgPh6VaDJj2SoAEldu7voO93nRemWXqYxCyMBK5LraGU7ht6j","sender_id":"FSTSMS","message":"This is test message","language":"english","route":"p","numbers":num}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
