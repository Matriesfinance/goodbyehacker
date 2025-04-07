import yfinance as yf
from sklearn.linear_model import LinearRegression
import numpy as np

def fetch_stock_data(stock_symbol='AAPL'):
    data = yf.download(stock_symbol, period='1y', interval='1d')
    return data[['Close']]

def build_stock_model():
    data = fetch_stock_data()
    X = np.array([i for i in range(len(data))]).reshape(-1, 1)
    y = data['Close'].values
    
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_stock(model):
    X_new = np.array([[len(model.coef_) + 1]])  # Simple prediction model
    prediction = model.predict(X_new)
    return prediction
