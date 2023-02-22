# Importando bibliotecas
import pandas as pd
import streamlit as st
import numpy as np
from datetime import date
import yfinance as yf
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

    #Criando funções que vão imprimir o conteúdo na tela.
    #Cada uma referente à uma determinada página que posteriormente,
    #serão chamadas através da barra de menu lateral.


    #Home -> Página inicial
def home():
    col1,col2,col3 = st.columns(3)
    with col2:
        st.sidebar.markdown("---")
        st.title("App Financeiro")

    #Panorama -> Screener dos principais ativos e índices do mercado
def panorama():
    st.title("Panorama Do Mercado")
    st.markdown(date.today().strftime("%d/%m/%Y"))
    st.markdown("---")
    st.subheader("Índices")

    # Criando Dicionários para cara classe de ativo

    #Dicionário de Índices
    index_tck = {
        "Crypto200":"^CMC200",
        "DXY": "DX-Y.NYB",
        "S&P500" : "^GSPC",
        "Volatility":"^VIX",
        "NASDAQ" : "^IXIC",
        "NYSE":"^NYA",
        "FTSE 100" : "^FTSE",
        "Dow Jones Industrial":"^DJI",
        "Dow Jones Transportes": "^DJT",
        "HANG SENG": "^HSI",
        "Nikkei 225": "^N225",
        "DAX": "^GDAXI",
        "Bovespa": "^BVSP",
    }

    #Dicionário de Criptomoedas
    crypto_tck = {
        "BITCOIN": "BTC-USD",
        "ETHEREUM": "ETH-USD",
        "POLYGON": "MATIC-USD",
        "CHAINLINK": "LINK-USD",
        "GMX": "GMX-USD",
        "SYNTHETIX": "SNX-USD",
        "SINGULARITY DAO": "SDAO-USD",
        "NUNET": "NTX-USD",
        "POLKADOT":"DOT-USD",
    }

    #Dicionário de Juros
    yeld_tck = {
        "13 Week Treasury Bill":"^IRX",
        "5 Years Yeld":"^FVX",
        "10 Years Yeld": "^TNX",
        "30 Years Yeld": "^TYX",
    }

    #Dicionário de Empresas Americanas
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


    #Criando dataframe para armazenar as cotacoes de cada item que serão coletados posteriormente
    #Criando as colunas onde serão armazenados os valores e a variação %

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

    #Imprimindo na tela mensagem "Carregando"
    with st.spinner("Coletando Cotações"):

        #Criando loop para download dos dados
        #Utilizando a biblioteca YFinance vamos fazer o download para cada item do dicionário
        count = 0
        for ticker in index_tck.values():
           cotacoes = yf.download(ticker,period="1mo",auto_adjust=True)["Close"]
           variacao = ((cotacoes.iloc[-1]/cotacoes.iloc[-2])-1)*100
           df_index["Ult.Valor"][count] = round(cotacoes.iloc[-1],2)
           df_index["%"][count] = round(variacao,2)
           count += 1

        count=0
        for ticker in crypto_tck.values():
            cotacoes = yf.download(ticker, period="1mo", auto_adjust=True)["Close"]
            variacao = ((cotacoes.iloc[-1] / cotacoes.iloc[-2]) - 1) * 100
            df_crypto["Ult.Valor"][count] = round(cotacoes.iloc[-1], 3)
            df_crypto["%"][count] = round(variacao, 2)
            count += 1

        count=0
        for ticker in commodity_tck.values():
            cotacoes = yf.download(ticker, period="1mo", auto_adjust=True)["Close"]
            variacao = ((cotacoes.iloc[-1] / cotacoes.iloc[-2]) - 1) * 100
            df_commodity["Ult.Valor"][count] = round(cotacoes.iloc[-1], 3)
            df_commodity["%"][count] = round(variacao, 2)
            count += 1


    # PLOTANDO INDICES
    #Criando colunas na tela para exibir o valor de cada índice e a variação % do dia
    #st.write(df_index)

    col1, col2, col3,col4 = st.columns(4)

    # Crypto200 - NASDAQ - HANG SENG
    with col1:
        st.metric(df_index["Ativo"][0], df_index["Ult.Valor"][0], delta=str(df_index["%"][0]) + "%")
        st.metric(df_index["Ativo"][4], df_index["Ult.Valor"][4], delta=str(df_index["%"][4]) + "%")
        st.metric(df_index["Ativo"][9], df_index["Ult.Valor"][9], delta=str(df_index["%"][9]) + "%")

    #
    with col2:
        st.metric(df_index["Ativo"][1], df_index["Ult.Valor"][1], delta=str(df_index["%"][1]) + "%")
        st.metric(df_index["Ativo"][5], df_index["Ult.Valor"][5], delta=str(df_index["%"][5]) + "%")
        st.metric(df_index["Ativo"][11], df_index["Ult.Valor"][11], delta=str(df_index["%"][11]) + "%")


    with col3:
        st.metric(df_index["Ativo"][2], df_index["Ult.Valor"][2], delta=str(df_index["%"][2]) + "%")
        st.metric(df_index["Ativo"][6], df_index["Ult.Valor"][6], delta=str(df_index["%"][6]) + "%")
        st.metric(df_index["Ativo"][10], df_index["Ult.Valor"][10], delta=str(df_index["%"][10]) + "%")


    with col4:
        st.metric(df_index["Ativo"][3], df_index["Ult.Valor"][3], delta=str(df_index["%"][3]) + "%")
        st.metric(df_index["Ativo"][7], df_index["Ult.Valor"][7], delta=str(df_index["%"][7]) + "%")
        st.metric(df_index["Ativo"][12], df_index["Ult.Valor"][12], delta=str(df_index["%"][12]) + "%")

    st.markdown("---")
    st.subheader("Criptomoedas")

    #PLOTANDO CRIPTOS
    #Criando colunas na tela para exibir o valor de cada índice e a variação % do dia
    #st.write(df_crypto)

    col1, col2, col3 = st.columns(3)

    # Crypto200 - NASDAQ - HANG SENG
    with col1:
        st.metric(df_crypto["Ativo"][0], df_crypto["Ult.Valor"][0], delta=str(df_crypto["%"][0]) + "%")
        st.metric(df_crypto["Ativo"][8], df_crypto["Ult.Valor"][8], delta=str(df_crypto["%"][8]) + "%")

    #
    with col2:
        st.metric(df_crypto["Ativo"][1], df_crypto["Ult.Valor"][1], delta=str(df_crypto["%"][1]) + "%")
        st.metric(df_crypto["Ativo"][5], df_crypto["Ult.Valor"][5], delta=str(df_crypto["%"][5]) + "%")


    with col3:
        st.metric(df_crypto["Ativo"][2], df_crypto["Ult.Valor"][2], delta=str(df_crypto["%"][2]) + "%")
        st.metric(df_crypto["Ativo"][6], df_crypto["Ult.Valor"][6], delta=str(df_crypto["%"][6]) + "%")

    st.markdown("---")

    st.subheader("Gráfico")
    tab1, tab2, tab5, tab6 = st.tabs(["Índices", "Criptomoedas", "Yeld","Commodities"])

    with tab1:
        #Criando caixa com os nomes dos papeis
        indice_selecionado = st.selectbox("Selecione o Índice",index_tck.keys())

        for ticker in index_tck.keys():
            if not ticker == indice_selecionado:
                pass
            else:
                indice_diario = yf.download(index_tck.get(indice_selecionado), period="60d", interval="1d")

        fig = go.Figure(data=[go.Candlestick(x=indice_diario.index,
                                                  open = indice_diario["Open"],
                                                  high=indice_diario["High"],
                                                  low=indice_diario["Low"],
                                                  close=indice_diario["Close"])])
        fig.update_layout(title=indice_selecionado, xaxis_rangeslider_visible=False)


        st.plotly_chart(fig)
    with tab2:
        #Criando caixa com os nomes dos papeis
        indice_selecionado = st.selectbox("Selecione a Criptomoeda",crypto_tck.keys())

        for ticker in crypto_tck.keys():
            if not ticker == indice_selecionado:
                pass
            else:
                indice_diario = yf.download(crypto_tck.get(indice_selecionado), period="60d", interval="1d")

        fig = go.Figure(data=[go.Candlestick(x=indice_diario.index,
                                                  open = indice_diario["Open"],
                                                  high=indice_diario["High"],
                                                  low=indice_diario["Low"],
                                                  close=indice_diario["Close"])])
        fig.update_layout(title=indice_selecionado, xaxis_rangeslider_visible=False)
        st.plotly_chart(fig)

    with tab5:
        #Criando caixa com os nomes dos papeis
        indice_selecionado = st.selectbox("Selecione o Juro",yeld_tck.keys())

        for ticker in yeld_tck.keys():
            if not ticker == indice_selecionado:
                pass
            else:
                indice_diario = yf.download(yeld_tck.get(indice_selecionado), period="60d", interval="1d")

        fig = go.Figure(data=[go.Candlestick(x=indice_diario.index,
                                                  open = indice_diario["Open"],
                                                  high=indice_diario["High"],
                                                  low=indice_diario["Low"],
                                                  close=indice_diario["Close"])])
        fig.update_layout(title=indice_selecionado, xaxis_rangeslider_visible=False)
        st.plotly_chart(fig)
    with tab6:
        #Criando caixa com os nomes dos papeis
        indice_selecionado = st.selectbox("Selecione a Commoditie",commodity_tck.keys())

        for ticker in commodity_tck.keys():
            if not ticker == indice_selecionado:
                pass
            else:
                indice_diario = yf.download(commodity_tck.get(indice_selecionado), period="60d", interval="1d")

        fig = go.Figure(data=[go.Candlestick(x=indice_diario.index,
                                                  open = indice_diario["Open"],
                                                  high=indice_diario["High"],
                                                  low=indice_diario["Low"],
                                                  close=indice_diario["Close"])])
        fig.update_layout(title=indice_selecionado, xaxis_rangeslider_visible=False)
        st.plotly_chart(fig)
    st.markdown("---")

#Mapa Mensal -> Mostrar retornos de algum ativo selecionado
def mapa_mensal():
    st.title("Análise Quantitativa")
    st.markdown("---")
    tab1, tab2, tab3 = st.tabs(["Bitcoin", "S&P500", "DXY"])

    with tab1:

        #importando dados de preço do BITCOIN e definindo a data como o índice

        btc_data = pd.read_csv("https://www.lookintobitcoin.com/bitcoin-price-download/", index_col="Date",
                               parse_dates=True)
        #removendo coluna vazia
        btc_data = btc_data.drop("Unnamed: 0", axis=1)
        #st.write(btc_data)

        st.write("Gráfico BTC")
        st.line_chart(btc_data, x=None, y=None, width=0, height=0, use_container_width=True)

        #criando dataframe com variação percentual
        btc_pct = btc_data.pct_change()
        #st.write(btc_pct)

        #Criando dataframe que agrupa os dados em Ano e Mes
        retorno_mensal = btc_pct.groupby([btc_pct.index.year.rename("Year"),btc_pct.index.month.rename("Month")]).mean()
        #st.write(retorno_mensal)

        #criando dataframe/tabela onde o Indice é o ANO, e as colunas são os retornos mensais
        tabela_retornos = pd.DataFrame(retorno_mensal)
        tabela_retornos = pd.pivot_table(tabela_retornos, values="Price", index="Year", columns="Month")
        #Trocando formato do nome dos meses Numero->Nome Abreviado
        tabela_retornos.columns = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
        #st.write(tabela_retornos)

        #Criando Heatmap para retornos mensais
        fig, ax = plt.subplots(figsize=(16,16))
        #Definindo paleta de cores
        cmap = sns.color_palette("RdYlGn",300)
        #definindo parametros
        sns.heatmap(tabela_retornos, cmap=cmap, annot=True,annot_kws={"size":13}, fmt=".2%", center=0, vmax=0.01, vmin=-0.01, cbar=False,
                    linewidths=2, xticklabels=True, yticklabels=True, ax=ax,square=True)
        ax.set_title("Retornos Mensais Bitcoin", fontsize=34)
        ax.set_yticklabels(ax.get_yticklabels(), rotation=0, verticalalignment="center", fontsize="16")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=0, verticalalignment="center", fontsize="16")
        plt.ylabel("")
        st.pyplot(fig)

        st.markdown("---")


        #Plotando informações estatísticas
        stats = pd.DataFrame(tabela_retornos.mean(), columns=["Média"])
        stats["Mediana"] = tabela_retornos.median()
        stats["Maior"] = tabela_retornos.max()
        stats["Menor"] = tabela_retornos.min()
        #Método gt() -> Greater -> Maior que()
        #Esse método conta quantas vezes o resultado foi maior que, no caso zero.
        #método -> sum() vai soamr quantas vezes a condição foi verdadeira, depois é dividido pela quantidade de items da tabela
        stats["Positivos"] = tabela_retornos.gt(0).sum()/tabela_retornos.count()
        #Mesma lógica, porem agora o método le() vai mostrar os itens menores do que zero
        stats["Negativos"] = (tabela_retornos.le(0).sum()/tabela_retornos.count())

        stats_a = stats[["Média","Mediana","Maior","Menor"]]
        stats_a = stats_a.transpose()

        #Criando Heatmap para Estatísticas
        fig, ax = plt.subplots(figsize=(15,6))
        #Definindo paleta de cores
        cmap = sns.color_palette("RdYlGn",300)
        #definindo parametros
        sns.heatmap(stats_a, cmap=cmap, annot=True,annot_kws={"size":13}, fmt=".2%", center=0, vmax=0.05, vmin=-0.05, cbar=False,
                    linewidths=2, xticklabels=True, yticklabels=True, ax=ax, square=True)
        ax.set_title("Resumo Estatístico", fontsize=24)
        ax.set_yticklabels(ax.get_yticklabels(), rotation=0, verticalalignment="center", fontsize="16")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=0, verticalalignment="center", fontsize="16")
        plt.ylabel("")
        st.pyplot(fig)

        st.markdown("---")


        stats_b = stats[["Positivos","Negativos"]]
        stats_b = stats_b.transpose()
        # Criando Heatmap para Estatísticas
        fig, ax = plt.subplots(figsize=(16, 3))
        # Definindo paleta de cores
        cmap = sns.color_palette("magma", as_cmap=True)
        # definindo parametros
        sns.heatmap(stats_b,cmap=cmap, annot=True,annot_kws={"size":13}, vmax=1, fmt=".2%", center=0, cbar=False,
                    linewidths=2, xticklabels=True, yticklabels=True, ax=ax,square=True)
        ax.set_title("Resumo Estatístico", fontsize=24)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=0, verticalalignment="center", fontsize="16")
        ax.set_yticklabels(ax.get_yticklabels(), rotation=0, verticalalignment="center", fontsize="16")
        plt.ylabel("")
        st.pyplot(fig)

        st.markdown("---")



def fundamentos():
    st.title("Fundamentos")
    st.sidebar.markdown("---")

def main():
    with st.container():
        st.image("btc_whitepaper_wordcloud.png")
    st.sidebar.title("Crypto Screener")
    st.sidebar.markdown("---")
    lista_menu=["Home", "Panorama", "Rentabilidade Mensal", "Fundamentos"]
    escolha = st.sidebar.radio("Escolha uma opção", lista_menu)

    if escolha == "Home":
        home()
    if escolha =="Panorama":
        panorama()
    if escolha =="Rentabilidade Mensal":
        mapa_mensal()
    if escolha == "Fundamentos":
        fundamentos()
    st.sidebar.markdown("---")

main()
