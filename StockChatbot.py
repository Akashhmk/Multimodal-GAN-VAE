import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import datetime

def fetch_stock_data(ticker):
    end_date = datetime.datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.datetime.today() - datetime.timedelta(days=365)).strftime('%Y-%m-%d')
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def train_model(stock_data):
    stock_data['Date'] = stock_data.index
    stock_data['Date'] = stock_data['Date'].map(datetime.datetime.toordinal)
    X = stock_data[['Date']]
    y = stock_data['Close']
    
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_next_day(model):
    next_day = datetime.datetime.today() + datetime.timedelta(days=1)
    next_day_ordinal = np.array([[next_day.toordinal()]], dtype=float)
    prediction = model.predict(next_day_ordinal)
    return prediction[0]

def chatbot():
    print("Welcome to the Stock Prediction Chatbot!")
    while True:
        ticker = input("Enter a stock ticker symbol (or type 'exit' to quit): ").upper()
        if ticker == 'EXIT':
            print("Goodbye!")
            break
        try:
            stock_data = fetch_stock_data(ticker)
            if stock_data.empty:
                print("Invalid ticker or no data available.")
                continue
            
            model = train_model(stock_data)
            prediction = predict_next_day(model)
            print(f"Predicted closing price for {ticker} on the next trading day: ${float(prediction):.2f}")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    chatbot()