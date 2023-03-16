# Importando bibliotecas
import pandas as pd
import streamlit as st
import numpy as np
import base64
import seaborn as sns
from bs4 import BeautifulSoup
import requests
import json
import time
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns



def cryptocurency():
    st.write("Hello")

    sp500 = pd.read_html(r'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol']

    tickers = []
    deltas = []
    sectors = []
    market_caps = []

    for ticker in sp500:
        
        try:
            #criando objeto para tickers
            stock = yf.Ticker(ticker)
            tickers.append(ticker)
            
            #download dos dados
            info = stock.fast_info 
            
            #download setor
            #sectors.append(info["sector"])
            
            #download do preço recente
            hist = stock.history("2d")
            
            #calculando o delta
            deltas.append((hist["Close"][1] - hist["Close"][0]/hist["Close"][0]))
            
            #calculando marketcap
            market_caps.append(stock.fast_info["marketCap"])
        except Exception as e:
            print(e)
    
    currency_price_unit = st.selectbox('Select currency for price', ('USD', 'BTC', 'ETH'))

    @st.cache_data
    def load_data():
        cmc = requests.get("https://coinmarketcap.com")
        soup = BeautifulSoup(cmc.content, "html.parser")
        
        data = soup.find("script", id="__NEXT_DATA__", type="application/json")
        coins = {}
        coin_data = json.loads(data.contents[0])
        listings = coin_data["props"]["initialState"]["cryptocurrency"]["listingLatest"]["data"]
        
        for i in listings:
            coins[str(i["id"])] = i["slug"]
        
        coin_name = []
        coin_symbol = []
        market_cap = []
        percent_change_1h = []
        percent_change_24h = []
        percent_change_7d = []
        price = []
        volume_24h = []
        
        for i in listings:
            coin_name.append(i["slug"])
            coin_symbol.append(i["symbol"])
            price.append(i["quote"][currency_price_unit]["price"])
            percent_change_1h.append(i["quote"][currency_price_unit]["percentChange1h"])
            percent_change_24h.append(i["quote"][currency_price_unit]["percentChange24h"])
            percent_change_7d.append(i["quote"][currency_price_unit]["percentChange7d"])
            market_cap.append(i["quote"][currency_price_unit]["marketCap"])
            volume_24h.append(i["quote"][currency_price_unit]["volume24h"])
            
            
        df = pd.DataFrame(columns=["coin_name","coin_symbol","maketcap","percentChange1h","percentChange24h","percentChange7d","price","volume24h"])
        df["coin_name"] = coin_name
        df["coin_symbol"] = coin_symbol
        df["price"] = price
        df["percent_change_1h"] =  percent_change_1h 
        df["percent_change_24h"] = percent_change_24h 
        df["percent_change_7d"] =  percent_change_7d 
        df["marketCap"] = market_cap
        df["volume24h"] = volume_24h
        
    df = load_data()
    
    st.write(df)