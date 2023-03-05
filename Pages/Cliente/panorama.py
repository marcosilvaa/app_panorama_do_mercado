# Importando bibliotecas
import pandas as pd
import streamlit as st
import numpy as np
from datetime import date
import time
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

    # Panorama -> Screener dos principais ativos e índices do mercado
def panorama():
    st.title("Panorama Do Mercado")
    st.markdown(date.today().strftime("%d/%m/%Y"))
    st.markdown("---")
    st.subheader("Índices")

    # Dicionário de Índices
    index_tck = {
        "Crypto200": "^CMC200",
        "DXY": "DX-Y.NYB",
        "S&P500": "^GSPC",
        "Volatility": "^VIX",
        "NASDAQ": "^IXIC",
        "NYSE": "^NYA",
        "FTSE 100": "^FTSE",
        "Dow Jones Industrial": "^DJI",
        "Dow Jones Transportes": "^DJT",
        "HANG SENG": "^HSI",
        "Nikkei 225": "^N225",
        "DAX": "^GDAXI",
        "Bovespa": "^BVSP",
    }

    # Dicionário de Criptomoedas
    crypto_tck = {
        "BITCOIN": "BTC-USD",
        "ETHEREUM": "ETH-USD",
        "POLYGON": "MATIC-USD",
        "CHAINLINK": "LINK-USD",
        "GMX": "GMX-USD",
        "SYNTHETIX": "SNX-USD",
        "SINGULARITY DAO": "SDAO-USD",
        "NUNET": "NTX-USD",
        "POLKADOT": "DOT-USD",
    }

    # Dicionário de Juros
    yeld_tck = {
        "13 Week Treasury Bill": "^IRX",
        "5 Years Yeld": "^FVX",
        "10 Years Yeld": "^TNX",
        "30 Years Yeld": "^TYX",
    }

    # Dicionário de Empresas Americanas
    stocks_tck = {
        "AAPL": "Apple",
        "MSFT": "Microsoft",
        "GOOGL": "Alphabet",
        "AMZN": "Amazon",
        "TSLA": "Tesla",
        "NVDA": "NVIDIA",
        "XOM": "Exxon Mobil",
        "META": "Meta Plataforms",
        "BAC": "Bank of America",
        "BABA": "Alibaba",
    }

    # Dicionário de CÂMBIO
    currency_tck = {
        "BRLUSD=X": "BRL/USD",
        "EURUSD=X": "EUR/USD",
        "GBPUSD=X": "GBP/USD",
        "BRLEUR=X": "BRL/EUR",
        "BRLGBP=X": "BRL/GBP",
    }

    # Dicionário de Commodities
    commodity_tck = {
        "CRUDE OIL": "CL=F",
        "OURO": "GC=F",
        "PRATA": "SI=F",
        "SOJA": "ZS=F",
        "MILHO": "ZC=F",
    }
    
    
    # Imprimindo na tela mensagem "Carregando"
    with st.spinner("Coletando Cotações"):
        
        def get_quotes(tickers):
            data = yf.download(tickers, period="1mo", auto_adjust=True)["Close"]
            return data
    
        # Criando loop para download dos dados
        # Utilizando a biblioteca YFinance vamos fazer o download para cada item do dicionário
        
        

    # Criando dataframe para armazenar as cotacoes de cada item que serão coletados posteriormente
    # Criando as colunas onde serão armazenados os valores e a variação %

    # dataframe para Index
    df_index = pd.DataFrame({"Ativo": index_tck.keys(),
                             "Ticker": index_tck.values()})
    df_index["Ult.Valor"] = " "
    df_index["%"] = " "

    # dataframe para Crypto
    df_crypto = pd.DataFrame({"Ativo": crypto_tck.keys(),
                             "Ticker": crypto_tck.values()})
    df_crypto["Ult.Valor"] = " "
    df_crypto["%"] = " "

    # dataframe para Stocks
    df_stocks = pd.DataFrame({"Ativo": stocks_tck.keys(),
                             "Ticker": stocks_tck.values()})
    df_stocks["Ult.Valor"] = " "
    df_stocks["%"] = " "

    # dataframe para Commodity
    df_commodity = pd.DataFrame({"Ativo": commodity_tck.keys(),
                                 "Ticker": commodity_tck.values()})
    df_commodity["Ult.Valor"] = " "
    df_commodity["%"] = " "

    # Imprimindo na tela mensagem "Carregando"
    with st.spinner("Coletando Cotações"):
        
        def get_quotes(tickers):
            data = yf.download(tickers, period="1mo", auto_adjust=True)["Close"]
            return data
    
        # Criando loop para download dos dados
        # Utilizando a biblioteca YFinance vamos fazer o download para cada item do dicionário
        
        
        count = 0
        for ticker in index_tck.values():
            cotacoes = get_quotes(ticker)
            variacao = ((cotacoes.iloc[-1]/cotacoes.iloc[-2])-1)*100
            df_index["Ult.Valor"][count] = round(cotacoes.iloc[-1], 2)
            df_index["%"][count] = round(variacao, 2)
            count += 1


        count = 0
        for ticker in crypto_tck.values():
            cotacoes = yf.download(ticker, period="1mo",
                                   auto_adjust=True)["Close"]
            variacao = ((cotacoes.iloc[-1] / cotacoes.iloc[-2]) - 1) * 100
            df_crypto["Ult.Valor"][count] = round(cotacoes.iloc[-1], 3)
            df_crypto["%"][count] = round(variacao, 2)
            count += 1

        count = 0
        for ticker in commodity_tck.values():
            cotacoes = yf.download(ticker, period="1mo",
                                   auto_adjust=True)["Close"]
            variacao = ((cotacoes.iloc[-1] / cotacoes.iloc[-2]) - 1) * 100
            df_commodity["Ult.Valor"][count] = round(cotacoes.iloc[-1], 3)
            df_commodity["%"][count] = round(variacao, 2)
            count += 1
        count = 0

    # PLOTANDO COTAÇÕES
    # Criando colunas na tela para exibir o valor de cada índice e a variação % do dia


    #função que recebe como parâmetro o nome do dataframe para coletar o dado,
    # e o número da lista do ativo. 
    def metrica(df, n):
        st.metric(df["Ativo"][n], df["Ult.Valor"][n], delta=str(df["%"][n]) + "%")

    # PLOTANDO INDICES
    #Definindo layout 
    col1, col2, col3, col4 = st.columns(4)
    with st.container():
        with col1:
            metrica(df_index,0) #Crypto200
            metrica(df_index,4) #NASDAQ
            metrica(df_index,9) #HANGSENG 
        
        with col2:
            metrica(df_index,1) 
            metrica(df_index,5) 
            metrica(df_index,11)
            
        with col3:
            metrica(df_index,2) 
            metrica(df_index,6) 
            metrica(df_index,10)
            
        with col4:
            metrica(df_index,3) 
            metrica(df_index,7) 
            metrica(df_index,12) 
        
            
    st.markdown("---")
    st.subheader("Criptomoedas")

    # PLOTANDO CRIPTOS
    # Criando colunas na tela para exibir o valor de cada índice e a variação % do dia
    # st.write(df_crypto)

    #Definindo layout
    col1, col2, col3 = st.columns(3)

    with col1:
        metrica(df_crypto,0) 
        metrica(df_crypto,8) 

    with col2:
        metrica(df_crypto,1) 
        metrica(df_crypto,5) 

    with col3:
        metrica(df_crypto,2) 
        metrica(df_crypto,6) 
        
    st.markdown("---")

    col1,col2 = st.columns(2)
    
    with col1:
        st.subheader("Commodities")
        metrica(df_commodity,0) 
        metrica(df_commodity,1) 
        metrica(df_commodity,2) 
        metrica(df_commodity,3) 
        metrica(df_commodity,4)

        
    with col2: 
        st.subheader("Commodities")
        metrica(df_commodity,0) 
        metrica(df_commodity,1) 
        metrica(df_commodity,2) 
        metrica(df_commodity,3) 
        metrica(df_commodity,4) 
    
    st.markdown("---")
   