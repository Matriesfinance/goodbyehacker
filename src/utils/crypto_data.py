import requests

# Your actual CoinMarketCap API key
API_KEY = '97a06108-520b-4b84-85f7-ffc3e5a0dcf3'

def get_crypto_prices():
    # Fetch live crypto prices from CoinMarketCap API
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY
    }
    params = {
        'limit': 2,  # Limit to first 2 cryptos (Bitcoin and Ethereum)
        'convert': 'USD'
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        bitcoin_price = next((item for item in data['data'] if item['symbol'] == 'BTC'), None)
        ethereum_price = next((item for item in data['data'] if item['symbol'] == 'ETH'), None)

        if bitcoin_price and ethereum_price:
            return {
                'bitcoin': bitcoin_price['quote']['USD']['price'],
                'ethereum': ethereum_price['quote']['USD']['price']
            }
        else:
            return {'error': 'Could not find Bitcoin or Ethereum data'}
    else:
        return {'error': 'Failed to fetch data'}
