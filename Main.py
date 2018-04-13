import requests
import json
from bi

pair = "EOS-BTC"

bin = requests.get()

data = requests.get("https://api.kucoin.com/v1/EOS-BTC/open/tick/").json()


print(data)