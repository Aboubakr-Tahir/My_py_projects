import streamlit as st 
import yfinance as yf 
import pandas as pd

st.write("""
         # Simple stock price app 
         shown are idk bro i dont wanna write all of this
         """) 
tickersymbol = st.text_input("Enter ticker symbol : ","GOOGL") 
ticker_Data = yf.Ticker(tickersymbol) 
tickerDF = ticker_Data.history(start='2020-02-17',end='2024-02-17') 
st.write('Line chart of Close data') 
st.line_chart(tickerDF['Close'])  
st.write(f'Line chart of Open data of {tickersymbol}')  
st.line_chart(tickerDF['Open']) 
