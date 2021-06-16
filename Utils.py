import pandas as pd
import streamlit as st


def preprocess(df):
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
        df['Date'] = df['date'].dt.strftime('%d-%m-%y')
        df['Date'] = pd.to_datetime(df['Date'])
        df['Date'] = df['Date'].dt.strftime('%d-%m-%y')
    if {'date', 'unix', 'Volume USDT', 'tradecount', 'symbol'}.issubset(df.columns):
        df.drop(['date', 'unix', 'Volume USDT', 'tradecount', 'symbol'], axis='columns', inplace=True)
    df = df[['Date', 'open', 'high', 'low', 'close', 'volume']]
    df = df.set_index(pd.DatetimeIndex(df['Date']))
    return df


def get_input():
    start_date = st.sidebar.date_input("Start Date")
    end_date = st.sidebar.date_input("End Date")
    crypto_symbols = st.sidebar.selectbox("Crypto Symbol", ("BTC", "ETH", "XRP"))
    return start_date, end_date, crypto_symbols


def get_crypto_name(symbol):
    symbol = symbol.upper()
    if symbol == "BTC":
        return "Bitcoin"
    elif symbol == "ETH":
        return "Ethereum"
    elif symbol == "XRP":
        return "Ripple"
    else:
        return "None"


def get_data(symbol, start, end):
    symbol = symbol.upper()
    if symbol == "BTC":
        df = pd.read_csv(
            "https://raw.githubusercontent.com/nikhilsanghi/Datasets/main/crypto_data/bitcoin_daily.csv")
        df = preprocess(df)
    elif symbol == "ETH":
        df = pd.read_csv(
            "https://raw.githubusercontent.com/nikhilsanghi/Datasets/main/crypto_data/ethereum_daily.csv")
        df = preprocess(df)
    elif symbol == "XRP":
        df = pd.read_csv(
            "https://raw.githubusercontent.com/nikhilsanghi/Datasets/main/crypto_data/xrp_daily.csv")
        df = preprocess(df)
    else:
        df = pd.DataFrame(columns=['Date', 'close', 'open', 'volume'])
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    return df.loc[start:end]
