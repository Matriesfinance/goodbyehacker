import requests
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Fetch live crypto prices from CoinMarketCap (using API)
API_KEY = '97a06108-520b-4b84-85f7-ffc3e5a0dcf3'

def fetch_crypto_data():
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
    data = response.json()
    
    if response.status_code == 200:
        bitcoin_price = next((item for item in data['data'] if item['symbol'] == 'BTC'), None)
        ethereum_price = next((item for item in data['data'] if item['symbol'] == 'ETH'), None)

        if bitcoin_price and ethereum_price:
            return {
                'bitcoin': bitcoin_price['quote']['USD']['price'],
                'ethereum': ethereum_price['quote']['USD']['price']
            }
    return None

# Build the model using the fetched data
def build_crypto_model():
    data = fetch_crypto_data()
    if data is None:
        return None

    # Simulate a simple dataset with prices over time for Bitcoin and Ethereum
    df = pd.DataFrame(list(data.items()), columns=['Crypto', 'Price'])
    
    # Create a simple dataset for linear regression
    X = np.array([i for i in range(len(df))]).reshape(-1, 1)  # time steps
    y = df['Price'].values  # prices

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X, y)
    return model

# Predict the price of crypto (Bitcoin/Ethereum)
def predict_crypto(model):
    if model is None:
        return "Model not built correctly."

    # Simple prediction: predict the next price
    X_new = np.array([[len(model.coef_) + 1]])  # Predict next time step
    prediction = model.predict(X_new)
    return prediction[0]  # Return the predicted price
