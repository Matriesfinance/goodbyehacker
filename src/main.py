from flask import Flask, render_template, request, jsonify
from models.vulnerability_scanner import scan_for_vulnerabilities
from models.crypto_predictor import build_crypto_model, predict_crypto
from models.stock_predictor import build_stock_model, predict_stock
from utils.live_data import get_google_news
from utils.crypto_data import get_crypto_prices
from utils.self_learning import SelfLearningModel

app = Flask(__name__)

# Initialize models
crypto_model = build_crypto_model()
stock_model = build_stock_model()
learning_model = SelfLearningModel()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/live-news', methods=['GET'])
def live_news():
    news_titles = get_google_news()
    return jsonify({'news': news_titles})

@app.route('/crypto-prices', methods=['GET'])
def crypto_prices():
    prices = get_crypto_prices()
    return jsonify({'prices': prices})

@app.route('/predict', methods=['POST'])
def handle_predict():
    user_input = request.json['input']
    
    # Handle different types of requests
    if "scan" in user_input.lower():
        target_url = user_input.split(' ')[-1]
        scan_result = scan_for_vulnerabilities(target_url)
        return jsonify({'response': scan_result})

    elif "crypto" in user_input.lower():
        prediction = predict_crypto(crypto_model)
        return jsonify({'response': f"Predicted crypto price: {prediction[-1]}"})

    elif "stock" in user_input.lower():
        prediction = predict_stock(stock_model)
        return jsonify({'response': f"Predicted stock price: {prediction[-1]}"})

    elif "joke" in user_input.lower():
        return jsonify({'response': "Why don't skeletons fight each other? They don't have the guts!"})
    
    elif "hello" in user_input.lower():
        return jsonify({'response': "Hey there, professional! Ready for some market analysis?"})

    else:
        return jsonify({'response': "I'm not sure how to help with that. Ask me about crypto, stocks, or a security scan!"})

if __name__ == '__main__':
    app.run(debug=True)
