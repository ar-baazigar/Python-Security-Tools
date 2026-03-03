import requests # The library for web requests
# We are using a free API from CoinGecko
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
print("[*] Contacting the Crypto Server...")

# 1. Fetch the data
response = requests.get(url)

# 2. Convert the raw text into a Python Dictionary (JSON)
data = response.json()

# 3. Dig into the data to find the price
price = data['bitcoin']['usd']

print(f"[+] The current price of 1 Bitcoin is: ${price}")