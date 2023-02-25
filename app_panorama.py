# Importando bibliotecas
import pandas as pd
import streamlit as st
import numpy as np
from datetime import date
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


##################################################################################
##################################################################################
##################################################################################

    # Criando funções que vão imprimir o conteúdo na tela.
    # Cada uma referente à uma determinada página que posteriormente,
    # serão chamadas através da barra de menu lateral.

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

##################################################################################
##################################################################################
##################################################################################

# Mapa Mensal -> Mostrar retornos de algum ativo selecionado

def mapa_mensal(option):

    if option == "Bitcoin":

        st.title("Análise Quantitativa " + option)
        st.markdown("---")

        # Função que realiza o download dos dados do btc
        def load_data():
            btc_data = pd.read_csv(
                "https://www.lookintobitcoin.com/bitcoin-price-download/",
                index_col="Date",
                parse_dates=True
            )
            btc_data.drop("Unnamed: 0", axis=1, inplace=True)
            return btc_data
        
        btc_data = load_data()
        
        # criando novo dataframe com preço de fechamento de cada mês
        btc_mensal = btc_data.resample("M").last()

        # Criando coluna para armazenar a variação percentual do preço
        btc_mensal['%'] = (btc_mensal['Price'].pct_change() * 100).round(2)
        
        # Selecionando a coluna % do objeto btc_mensal
        btc_percent = pd.DataFrame(btc_mensal['%'])
        
        # Agrupando por ano e mês e somando os valores da coluna %
        retorno_mensal = btc_percent.groupby(
            [btc_percent.index.year.rename("Year"), btc_percent.index.month.rename("Month")]).sum()
        
        df_retorno_mensal = pd.DataFrame(retorno_mensal)
        
        # Transformando o índice em colunas
        df_retorno_mensal.reset_index(inplace=True)
        
        #Transformando dataframe em tabela
        tabela_retornos = (df_retorno_mensal.pivot_table(values='%',index="Year", columns="Month"))
        
        #Definindo o nome das colunas como o nome de cada mês
        tabela_retornos.columns = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

        #Plotando HEATMAP com retornos % mensais 
        st.subheader("Retorno % Mensal")
        fig = px.imshow(tabela_retornos,
                labels=dict(x="Mês", y="Ano",),
                x=tabela_retornos.columns,
                y=tabela_retornos.index
               )
        fig = px.imshow(tabela_retornos, text_auto=True, aspect="auto",color_continuous_scale=[[0, 'red'], [0.12, 'yellow'], [1.0, 'green']])
        fig.update_layout(width=900, height=900, font_size=200)
        fig.update_layout(font_size=200)
        st.plotly_chart(fig)

        st.markdown("---")
    
    
        # Construindo novo dataframe com as informações estatísticas
        stats = pd.DataFrame(tabela_retornos.mean(), columns=["Média"])
        stats["Mediana"] = tabela_retornos.median()
        stats["Maior"] = tabela_retornos.max()
        stats["Menor"] = tabela_retornos.min()

        # trocando indice pelas colunas e arredondando o valor para duas casas decimais 
        stats_a = stats.transpose().round(2)
        
        #Plotando HEATMAP com resumo estatístico
        st.subheader("Resumo Estatístico")
        fig = px.imshow(stats_a,
                labels=dict(x="Mês", y="Ano",),
                x=stats_a.columns,
                y=stats_a.index
               )
        fig = px.imshow(stats_a, text_auto=True, aspect="auto",color_continuous_scale=[[0, 'red'], [0.12, 'yellow'], [1.0, 'green']])
        fig.update_layout(width=900, height=400, font_size=200)
        fig.update_layout(font_size=200)
        st.plotly_chart(fig)
        
        st.markdown("---")

        #Adcionando ao DataFrame ´stats´ coluna Positivos e coluna Negativos
        
        # Método gt() -> Greater -> Maior que()
        # Esse método busca quantas vezes o resultado foi maior que, no caso zero.
        # método -> sum() vai soamr quantas vezes a condição foi verdadeira, depois é dividido pela quantidade de items da tabela
        stats["Positivos"] = round(tabela_retornos.gt(0).sum()/tabela_retornos.count()*100)
        # Mesma lógica, porem agora o método le() vai mostrar os itens menores do que zero
        stats["Negativos"] = round((tabela_retornos.le(0).sum()/tabela_retornos.count())*100)

        #criando novo dataframe apenas com essas colunas
        stats_b = stats[["Positivos", "Negativos"]]
        
        #plotando gráfico de barras com o percentual de resultados positivos e negativos de cada mês
        st.subheader("Positivo X Negativo - Mensal (%) ")
        fig = px.bar(stats_b, color_discrete_map={'Negativos': 'red', 'Positivos': 'green'})
        st.plotly_chart(fig)


    
        
        pd.DataFrame()
        
        st.markdown("---")

    if option == "SP500":
        
        st.write("")
        btc_data = pd.read_csv("https://www.lookintobitcoin.com/bitcoin-price-download/", index_col="Date",
                               parse_dates=True)
        # removendo coluna vazia
        btc_data = btc_data.drop("Unnamed: 0", axis=1)
        # st.write(btc_data)

        st.write("Gráfico BTC")
        st.line_chart(btc_data, x=None, y=None, width=0,
                      height=0, use_container_width=True)

        # criando dataframe com variação percentual
        btc_pct = btc_data.pct_change()
        # st.write(btc_pct)

        # Criando dataframe que agrupa os dados em Ano e Mes
        retorno_mensal = btc_pct.groupby([btc_pct.index.year.rename(
            "Year"), btc_pct.index.month.rename("Month")]).mean()
        # st.write(retorno_mensal)

        # criando dataframe/tabela onde o Indice é o ANO, e as colunas são os retornos mensais
        tabela_retornos = pd.DataFrame(retorno_mensal)
        tabela_retornos = pd.pivot_table(
            tabela_retornos, values="Price", index="Year", columns="Month")
        # Trocando formato do nome dos meses Numero->Nome Abreviado
        tabela_retornos.columns = ["Jan", "Fev", "Mar", "Abr",
                                   "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        # st.write(tabela_retornos)

        fig = px.imshow(retorno_mensal*100,
            labels=dict(x="Day of Week", y="Time of Day",),
            x=tabela_retornos.columns,
            y=tabela_retornos.index
            )
        fig = px.imshow(retorno_mensal, text_auto=True, aspect="auto",color_continuous_scale=[[0, 'red'], [0.3, 'yellow'], [1.0, 'green']])
        fig.update_layout(width=900, height=900, font_size=200)
        fig.update_layout(font_size=200)
        st.plotly_chart(fig)

##################################################################################
##################################################################################
##################################################################################

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
        fig = go.Figure(data=[go.Candlestick(x=ticker.index,open=ticker["Open"],
                                            high=ticker["High"],low=ticker["Low"],close=ticker["Close"])])
        fig.update_layout(xaxis_rangeslider_visible=False)
        return st.plotly_chart(fig)

        
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


##################################################################################
##################################################################################
##################################################################################

def main():
    with st.container():
        st.image("btc_whitepaper_wordcloud.png")
    st.sidebar.title("Crypto Screener")
    st.sidebar.markdown("---")
    lista_menu = ["Panorama", "Gráficos","Rentabilidade Mensal"]
    
    escolha = st.sidebar.radio("Escolha uma opção", lista_menu)


    if escolha == "Panorama":
        panorama()
    if escolha == "Gráficos":
        graficos()
    if escolha == "Rentabilidade Mensal":
        option = st.sidebar.selectbox("Escolha um Ativo", ("Bitcoin","SP500"))
        mapa_mensal(option)
    st.sidebar.markdown("---")


main()
