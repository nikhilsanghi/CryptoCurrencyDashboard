# Description : A cryptocurrency dashboard

# Import Important libraries
import streamlit as st
import Utils
import plotly.graph_objects as go
from PIL import Image

# Dashboard headline
st.write("""
# Cryptocurrency Dashboard Application
Visually show data on cryptocurrency
""")

#  Creating some sidebar inputs
st.sidebar.header("User Input")

# This will add a homepage pic to the dashboard
image = Image.open(
    "/Users/nikhilsanghi/Documents/Pycharm_Projects/CryptoCurrency/Images/CryptoDashboardPic.png")
st.image(image, use_column_width=True)

# fetching the start_date, end_date and the symbol from user
start, end, symbol = Utils.get_input()

# depending upon the input porvided by the user, we will fetch the required data
df = Utils.get_data(symbol, start, end)

# Fetching the cryptocurrency name from the abbreviated form
crypto_name = Utils.get_crypto_name(symbol)

#Creating a candlestick graph for deatail analysis on daily changes in the prices of currencies
df = Utils.get_data(symbol, start, end)
fig = go.Figure(
    data=[
        go.Candlestick(
            x=df.index,
            open=df['open'],
            close=df['close'],
            high=df['high'],
            low=df['low']
        )
    ]
)


st.header("Data")
st.write(df)

st.header(crypto_name + " Data Statistics")
st.write(df.describe())

st.header(crypto_name + " Close")
st.line_chart(df['close'])

st.header(crypto_name + " Volume")
st.bar_chart(df["volume"])

st.header(crypto_name + " Candle stick")
st.plotly_chart(fig)
