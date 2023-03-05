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



def graficos():
    st.title("Gráficos")
    st.markdown("---")

    #Criando dicionários
    # Dicionário de Índices
    index = {
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
    crypto = {
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
    yeld = {
        "13 Week Treasury Bill": "^IRX",
        "5 Years Yeld": "^FVX",
        "10 Years Yeld": "^TNX",
        "30 Years Yeld": "^TYX",
    }

    # Dicionário de Empresas Americanas
    stocks = {
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
    currency = {
        "BRLUSD=X": "BRL/USD",
        "EURUSD=X": "EUR/USD",
        "GBPUSD=X": "GBP/USD",
        "BRLEUR=X": "BRL/EUR",
        "BRLGBP=X": "BRL/GBP",
    }

    # Dicionário de Commodities
    commodity = {
        "CRUDE OIL": "CL=F",
        "OURO": "GC=F",
        "PRATA": "SI=F",
        "SOJA": "ZS=F",
        "MILHO": "ZC=F",
    }

    def get_quotes(classe,ticker, period,timeframe):
        data = yf.download(classe.get(ticker), period=period, interval=timeframe)
        return data


    def plot_graph(ticker):
        fig = go.Figure()

        # criando gráfico
        fig.add_trace(
            go.Candlestick(x=ticker.index,
                        open=ticker['Open'],
                        high=ticker['High'],
                        low=ticker['Low'],
                        close=ticker['Close']))


        # configurando botoes de seleção de período de tempo
        fig.update_layout(
            xaxis=dict(
                rangeselector = dict(
                    buttons = ([
                                #1 mes
                                dict(count = 1,
                                    label = '1m',
                                    step = 'month',
                                    stepmode = 'backward'),
                                #3 meses
                                dict(count = 3,
                                    label = '3m',
                                    step = 'month',
                                    stepmode = 'backward'),
                                # 6 meses
                                dict(count = 6,
                                    label = '6m',
                                    step = 'month',
                                    stepmode = 'backward'),
                                # 1 ano
                                dict(count = 1,
                                    label = '1y',
                                    step = 'year',
                                    stepmode = 'backward'),
                                # ultimos 12 meses
                                dict(count = 1,
                                    label = 'YTD',
                                    step = 'year',
                                    stepmode = 'todate'),
                                # total
                                dict(step='all')
                    ])
                ),

                # configurando slider
                rangeslider = dict( visible = True),
                
                type='date'
            )
        )
            
        # configurando escala logarítimica 
        # configurando tamanho do gráfico 
        fig.update_layout(width=1000, height=700, font_size=16)
        fig.update_yaxes(type="log")
        # plotando figura
        st.plotly_chart(fig,use_container_width=True)

        
    tab1, tab2, tab3, tab4, tab5,tab6 = st.tabs(["Índices", "Criptomoedas","Ações","Commodities", "Yeld", "Câmbio"])
    
    with tab1:
        
        # Formulario para o cliente informar como deseja visualizar o gráfico
        with st.form(key="form1"):    
            indice_selecionado = st.selectbox(
                "Selecione o Índice", index.keys())
            period = st.selectbox(
                "Defina o Período",
                options=["1d","7d","30d","60d","1y"])
            timeframe = st.selectbox(
                "Escolha o tempo gráfico",
                options=[ "5m", "15m", "30m", "60m", "1d", "1wk", "1mo", "3mo"])
            st.form_submit_button()
            
        for ticker in index.keys():
            if not ticker == indice_selecionado:
                pass
            else:
                indice_diario = get_quotes(index,indice_selecionado,period,timeframe)

        plot_graph(indice_diario)
        st.write("---")


    
    with tab2:
        with st.form(key="form2"):    
            indice_selecionado = st.selectbox(
                "Selecione o Índice", crypto.keys())
            period = st.selectbox(
                "Defina o Período",
                options=["1d","7d","30d","60d","1y"])
            timeframe = st.selectbox(
                "Escolha o tempo gráfico",
                options=[ "5m", "15m", "30m", "60m", "1d", "1wk", "1mo", "3mo"])
            st.form_submit_button()
            
        for ticker in crypto.keys():
            if not ticker == indice_selecionado:
                pass
            else:
                indice_diario = get_quotes(crypto,indice_selecionado,period,timeframe)

        plot_graph(indice_diario)   
        st.write("---")

    with tab3:
        with st.form(key="form3"):    
            indice_selecionado = st.selectbox(
                "Selecione o Índice", stocks.keys())
            period = st.selectbox(
                "Defina o Período",
                options=["1d","7d","30d","60d","1y"])
            timeframe = st.selectbox( 
                "Escolha o tempo gráfico",
                options=[ "5m", "15m", "30m", "60m", "1d", "1wk", "1mo", "3mo"])
            st.form_submit_button()
        
        for ticker in stocks.keys():
            if not ticker == indice_selecionado:
                pass
            else:
                indice_diario = get_quotes(stocks,indice_selecionado,period,timeframe)

        plot_graph(indice_diario)
        st.write("---")
        
    with tab4:
        with st.form(key="form4"):    
            indice_selecionado = st.selectbox(
                "Selecione o Índice", commodity.keys())
            period = st.selectbox(
                "Defina o Período",
                options=["1d","7d","30d","60d","1y"])
            timeframe = st.selectbox( 
                "Escolha o tempo gráfico",
                options=[ "5m", "15m", "30m", "60m", "1d", "1wk", "1mo", "3mo"])
            st.form_submit_button()
        
        for ticker in commodity.keys():
            if not ticker == indice_selecionado:
                pass
            else:
                indice_diario = get_quotes(commodity,indice_selecionado,period,timeframe)

            plot_graph(indice_diario)
            st.write("---")


    with tab5:
        with st.form(key="form5"):    
            indice_selecionado = st.selectbox(
                "Selecione o Índice", yeld.keys())
            period = st.selectbox(
                "Defina o Período",
                options=["1d","7d","30d","60d","1y"])
            timeframe = st.selectbox( 
                "Escolha o tempo gráfico",
                options=[ "5m", "15m", "30m", "60m", "1d", "1wk", "1mo", "3mo"])
            st.form_submit_button()
        
        for ticker in yeld.keys():
            if not ticker == indice_selecionado:
                pass
            else:
                indice_diario = get_quotes(yeld,indice_selecionado,period,timeframe)

            plot_graph(indice_diario)
            st.write("---")


    with tab6:
        with st.form(key="form6"):    
            indice_selecionado = st.selectbox(
                "Selecione o Índice", currency.keys())
            period = st.selectbox(
                "Defina o Período",
                options=["1d","7d","30d","60d","1y"])
            timeframe = st.selectbox( 
                "Escolha o tempo gráfico",
                options=[ "5m", "15m", "30m", "60m", "1d", "1wk", "1mo", "3mo"])
            st.form_submit_button()
        
        for ticker in currency.keys():
            if not ticker == indice_selecionado:
                pass
            else:
                indice_diario = get_quotes(currency,indice_selecionado,period,timeframe)

            plot_graph(indice_diario)
            st.write("---")
