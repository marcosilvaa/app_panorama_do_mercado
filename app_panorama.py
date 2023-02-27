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


##################################################################################
##################################################################################
##################################################################################

    # Criando funções que vão imprimir o conteúdo na tela.
    # Cada uma referente à uma determinada página que posteriormente,
    # serão chamadas através da barra de menu lateral.

def home():
    st.title("Bem Vindo ao Panorama Cripto")
    st.write("Aqui você encontra as principais informações que precisa para se atualizar sobre o mercado!")
    st.markdown("___")
    
    st.header("Como utilizar?")
    st.write("Na aba ao lado você encontra as opções disponíveis, confira abaixo o que vai encontrar em cada uma delas.")
    st.write("Caso esteja utilizando pelo celular e aba não esteja aparecendo, clique na setinha (>) no canto superior esquerdo. Neste caso, vire o celular para melhor visualização das análises quantitativas.  ")
    st.subheader("Panorama")
    st.write("Na aba Panorama estão disponíveis as cotações das principais criptomoedas, índices mundiais, ações americanas, e das principais moedas FIAT pareadas com o Dólar. ")
    
    st.subheader("Gráfico")
    st.write("Na aba gráficos, você pode conferir como está o gráfico de cada uma das cotações listadas na aba Panorama.")
    
    st.subheader("Análise Quantitativa")
    st.write("Em Análise Quantitativa, temos diversas análises de dados que nos mostram aquilo que somente os gráficos não mostram.")
    st.write("Por enquanto só estão disponíveis análises referentes ao Bitcoin e ao SP500.")
    
    st.markdown("___")
    
    
    
    st.subheader("Quem sou eu?")
    st.write("Marco Aurélio dos Santos Silva, sou Engenheiro Civil, aspirante à Analista de Dados estou desenvolvendo este projeto como parte do meu portfólio.")
    github = 'https://github.com/marcosilvaa/app_panorama_do_mercado'
    text_git = 'GitHub'
    st.markdown("Você pode conferir o código fonte no meu "+f'<a href="{github}">{text_git}</a>', unsafe_allow_html=True)
    linkedin ="https://www.linkedin.com/in/marcosilvaa/"
    st.markdown("E fique a vontade para se conectar ao meu "+f'<a href="{linkedin}">{"LinkedIn"}</a>', unsafe_allow_html=True)

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
   
##################################################################################
##################################################################################
##################################################################################

# Mapa Mensal -> Mostrar retornos de algum ativo selecionado

def analise_quant(option):

    
    ###Criando funções que serão utilizadas 
    
    ### RETORNO ---> Essa função criar um dataframe que vai agrupar os valores em ano e mês     
    # Função que realiza o download dos dados do btc
    def load_data(link):
        dataframe = pd.read_csv(
            link,
            index_col="Date",
            parse_dates=True
        )
        return dataframe

####################################################
##         FUNÇÕES PARA CRIAR DATAFRAMES          ##
####################################################
    
        
    def retorno(DataFrame):
        # Agrupando por ano e mês e somando os valores da coluna %
        retorno_mensal = DataFrame.groupby([DataFrame.index.year.rename("Year"), DataFrame.index.month.rename("Month")]).sum()
        retorno_mensal = pd.DataFrame(retorno_mensal)
        # Transformando o índice em colunas
        retorno_mensal.reset_index(inplace=True)
        return retorno_mensal
    
    ### ESTATISTICA ---> Essa função vai criar um novo dataframe com as informações estatísticas,
    #                    e valores máximos positivos e mínimos negatívos 
    def estatistica(DataFrame):
        # Construindo novo dataframe com as informações estatísticas
        stats = pd.DataFrame(DataFrame.mean(), columns=["Média"])
        stats["Mediana"] = DataFrame.median()
        stats["Maior"] = DataFrame.max()
        stats["Menor"] = DataFrame.min()
        # Método gt() -> Greater -> Maior que()
        # Esse método busca quantas vezes o resultado foi maior que, no caso zero.
        # método -> sum() vai soamr quantas vezes a condição foi verdadeira, depois é dividido pela quantidade de items da tabela
        stats["Positivos"] = round(DataFrame.gt(0).sum()/DataFrame.count()*100)
        # Mesma lógica, porem agora o método le() vai mostrar os itens menores do que zero
        stats["Negativos"] = round((DataFrame.le(0).sum()/DataFrame.count())*100)
        return stats

####################################################
##       FUNÇÕES PARA PLOTAGEM DE GRÁFICOS        ##
####################################################
    
    # plotando gráfico de CandleSticks
    def plot_candlestick(DataFrame):
        # criando figura
        fig = go.Figure()
        # criando gráfico
        fig.add_trace(
            go.Candlestick(x=DataFrame.index,
                        open=DataFrame['Open'],
                        high=DataFrame['High'],
                        low=DataFrame['Low'],
                        close=DataFrame['Close']))
        # configurando botoes de seleção de período de tempo
        fig.update_layout(
            xaxis=dict(
                # configurando slider
                rangeslider = dict( visible = False)))
        # configurando escala logarítimica 
        fig.update_yaxes(type="log")
        # configurando tamanho do gráfico 
        fig.update_layout(width=800, height=500)
        # plotando figura
        st.plotly_chart(fig,use_container_width=True)

    # Plotando HEATMAP para retornos % mensais
    def plot_retorno_mensal(DataFrame,cor_padrao,width,height):
        fig = px.imshow(DataFrame,
                labels=dict(x="Mês", y="Ano",),
                x=DataFrame.columns,
                y=DataFrame.index)
        fig = px.imshow(DataFrame, text_auto=True, aspect="auto",color_continuous_scale=cor_padrao)
        fig.update_layout(width=width, height=height, font_size=500)
        fig.update_layout(font_size=500)
        fig.update(layout_coloraxis_showscale=False)
        st.plotly_chart(fig,use_container_width=True)
        st.caption("Fonte Yahoo Finance")
    
    # Plotando HEATMAP com Informações estatísticas 
    def plot_estatistica(DataFrame, cor_padrao):
        fig = px.imshow(stats_a,
                labels=dict(x="Mês", y="Ano",),
                x=stats_a.columns,
                y=stats_a.index)
        fig = px.imshow(DataFrame, text_auto=True, aspect="auto",color_continuous_scale=cor_padrao)
        fig.update_layout(width=1000, height=400, font_size=200)
        fig.update_layout(font_size=200)
        fig.update(layout_coloraxis_showscale=True)
        st.plotly_chart(fig,use_container_width=True)
        st.caption("Fonte Yahoo Finance")
        
    # Plotando Gráfico de BARRAS para comparação entre meses Positivos X Negativos
    def plot_postivio_negativo(DataFrame):
        fig = px.bar(DataFrame, color_discrete_map={'Negativos': 'red', 'Positivos': 'green'})
        #EM CONSTRUÇÂO ---> adicionando linha média  
        #fig.add_trace(go.Scatter(x=[-0.5, len(stats_b)-0.5], y=[mean_value]*2, mode='lines', name='Média', line=dict(color='white')))
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Fonte Yahoo Finance")
        
    def plot_all(width,height):
        #Plotando HEATMAP com os retornos mensais
        cor_padrao = [[0, 'red'], [0.55, 'yellow'], [1.0, 'green']]
        plot_retorno_mensal(tabela_retornos,cor_padrao, 100,900)
        st.markdown("---")
        #plotando informações estatíticas
        stats_a = estatistica(tabela_retornos)[["Média","Mediana","Maior","Menor"]]
        # trocando indice pelas colunas e arredondando o valor para duas casas decimais 
        stats_a = stats_a.transpose().round(1)
        #Definindo paleta de cores para o heatmap 
        #Plotando HEATMAP com resumo estatístico
        plot_estatistica(stats_a,cor_padrao)
        st.markdown("---")
        #plotando gráfico de barras com o percentual de resultados positivos e negativos de cada mês
        stats_b = estatistica(tabela_retornos)[["Positivos", "Negativos"]]
        plot_postivio_negativo(stats_b)   
        st.markdown("---") 

    if option == "Bitcoin":

        st.title("Análise Quantitativa " + option)
        st.markdown("---")
        
        ################################
        #Plotando Gráfico do BTC
        st.subheader("Gráfico BTC")
        #Obtendo dados OHLC ---> Aqui vamos utilizar a YahooFinance para obter todos os dados necessários
        btc = yf.download("BTC-USD", period="15y", interval="1d")

        #Plotando Gráfico
        plot_candlestick(btc)


        ################################
        #Começando estudo quantitativo
        
        #importando dados
        btc_data = load_data("https://www.lookintobitcoin.com/bitcoin-price-download/")
        #removendo coluna sem dados 
        btc_data.drop("Unnamed: 0", axis=1, inplace=True)
        # criando novo dataframe com preço de fechamento de cada mês
        btc_mensal = btc_data.resample("M").last()
        # Criando coluna para armazenar a variação percentual do preço
        btc_mensal['%'] = (btc_mensal['Price'].pct_change() * 100).round()        
        # Selecionando a coluna % do objeto btc_mensal
        btc_percent = pd.DataFrame(btc_mensal['%'])
        
              
        # Criando Dataframe TOTAL
        retorno_mensal_total = retorno(btc_percent)
        #Transformando dataframe em tabela
        tabela_retornos_total = retorno_mensal_total.pivot_table(values='%',index="Year", columns="Month")
        #Definindo o nome das colunas como o nome de cada mês
        tabela_retornos_total.columns = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
              
        # Criando Dataframe com o ---> CICLO 1 do Bitcoin 
        btc_ciclo1 = btc_percent.iloc[:17]
        retorno_mensal1 = retorno(btc_ciclo1)
        #Transformando dataframe em tabela
        tabela_retornos1 = retorno_mensal1.pivot_table(values='%',index="Year", columns="Month")
        #Definindo o nome das colunas como o nome de cada mês
        tabela_retornos1.columns = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        
        # Criando Dataframe com o ---> CICLO 2 do Bitcoin 
        btc_ciclo2 = btc_percent.iloc[17:65]
        retorno_mensal2 = retorno(btc_ciclo2)
        #Transformando dataframe em tabela
        tabela_retornos2 = retorno_mensal2.pivot_table(values='%',index="Year", columns="Month")
        #Definindo o nome das colunas como o nome de cada mês
        tabela_retornos2.columns = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
              
        # Criando Dataframe com o ---> CICLO 3 do Bitcoin 
        btc_ciclo3 = btc_percent.iloc[65:113]
        retorno_mensal3 = retorno(btc_ciclo3)
        #Transformando dataframe em tabela
        tabela_retornos3 = retorno_mensal3.pivot_table(values='%',index="Year", columns="Month")
        #Definindo o nome das colunas como o nome de cada mês
        tabela_retornos3.columns = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        
        # Criando Dataframe com o ---> CICLO 4 do Bitcoin 
        btc_ciclo4 = btc_percent.iloc[113:]
        retorno_mensal4 = retorno(btc_ciclo4)        
        #Transformando dataframe em tabela
        tabela_retornos4 = retorno_mensal4.pivot_table(values='%',index="Year", columns="Month")
        #Definindo o nome das colunas como o nome de cada mês
        tabela_retornos4.columns = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
              
        
        ###PLOTANDO RETORNOS MENSAIS 
        st.subheader("Retorno % Mensal")
        total, ciclo1, ciclo2, ciclo3, ciclo4 = st.tabs(["Total", "Ciclo 1", "Ciclo 2", "Ciclo 3", "Ciclo4"])
        with total:
            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.095, 'yellow'], [1.0, 'green']]
            #plotando heatmap com retornos mensais
            plot_retorno_mensal(tabela_retornos_total,cor_padrao,900,900)
            st.markdown("---")
        
        with ciclo1: 
            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.1, 'yellow'], [1.0, 'green']]
            #plotando heatmap com retornos mensais
            plot_retorno_mensal(tabela_retornos1,cor_padrao,900,500)
            st.markdown("---")

        with ciclo2: 
            #Plotando HEATMAP com retornos % mensais 
            cor_padrao = [[0, 'red'], [0.07, 'yellow'], [1.0, 'green']]
            #plotando heatmap com retornos mensais
            plot_retorno_mensal(tabela_retornos2,cor_padrao,900,500)
            st.markdown("---")
            
        with ciclo3: 
            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.425, 'yellow'], [1.0, 'green']]
            #plotando heatmap com retornos mensais
            plot_retorno_mensal(tabela_retornos3,cor_padrao,900,500)
            st.markdown("---")
            
        with ciclo4: 
            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.425, 'yellow'], [1.0, 'green']]
            #plotando heatmap com retornos mensais
            plot_retorno_mensal(tabela_retornos4,cor_padrao,900,500)
            st.markdown("---")

        ### PLOTANDO ESTATISTICAS
        st.subheader("Resumo Estatístico (%)")
        total, ciclo1, ciclo2, ciclo3, ciclo4 = st.tabs(["Total", "Ciclo 1", "Ciclo 2", "Ciclo 3", "Ciclo4"])
        
        with total: 
            #plotando informações estatíticas
            stats_a = estatistica(tabela_retornos_total)[["Média","Mediana","Maior","Menor"]]
            # trocando indice pelas colunas e arredondando o valor para duas casas decimais 
            stats_a = stats_a.transpose().round(1)
            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.08, 'yellow'], [1.0, 'green']]
            #Plotando HEATMAP com resumo estatístico
            plot_estatistica(stats_a,cor_padrao)
            st.markdown("---")

        with ciclo1: 
            #plotando informações estatíticas
            stats_a = estatistica(tabela_retornos1)[["Média","Mediana","Maior","Menor"]]
            # trocando indice pelas colunas e arredondando o valor para duas casas decimais 
            stats_a = stats_a.transpose().round(1)
            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.08, 'yellow'], [1.0, 'green']]
            #Plotando HEATMAP com resumo estatístico
            plot_estatistica(stats_a,cor_padrao)
            st.markdown("---")
            
        with ciclo2: 
            #plotando informações estatíticas
            stats_a = estatistica(tabela_retornos2)[["Média","Mediana","Maior","Menor"]]
            # trocando indice pelas colunas e arredondando o valor para duas casas decimais 
            stats_a = stats_a.transpose().round(1)
            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.06, 'yellow'], [1.0, 'green']]
            #Plotando HEATMAP com resumo estatístico
            plot_estatistica(stats_a,cor_padrao)
            st.markdown("---")
        
        with ciclo3: 
            #plotando informações estatíticas
            stats_a = estatistica(tabela_retornos3)[["Média","Mediana","Maior","Menor"]]
            # trocando indice pelas colunas e arredondando o valor para duas casas decimais 
            stats_a = stats_a.transpose().round(1)
            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.3, 'yellow'], [1.0, 'green']]
            #Plotando HEATMAP com resumo estatístico
            plot_estatistica(stats_a,cor_padrao)
            st.markdown("---")
            
        with ciclo4: 
            #plotando informações estatíticas
            stats_a = estatistica(tabela_retornos4)[["Média","Mediana","Maior","Menor"]]
            # trocando indice pelas colunas e arredondando o valor para duas casas decimais 
            stats_a = stats_a.transpose().round(1)
            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.5, 'yellow'], [1.0, 'green']]
            #Plotando HEATMAP com resumo estatístico
            plot_estatistica(stats_a,cor_padrao)
            st.markdown("---")
        
        
        st.subheader("Meses Positivos X Negativo - (%)")
        total, ciclo1, ciclo2, ciclo3, ciclo4 = st.tabs(["Total", "Ciclo 1", "Ciclo 2", "Ciclo 3", "Ciclo4"])

        with total:

        #plotando gráfico de barras com o percentual de resultados positivos e negativos de cada mês
            stats_b = estatistica(tabela_retornos_total)[["Positivos", "Negativos"]]
            plot_postivio_negativo(stats_b)   
            st.markdown("---")
        
        with ciclo1:
            #plotando gráfico de barras com o percentual de resultados positivos e negativos de cada mês
            stats_b = estatistica(tabela_retornos1)[["Positivos", "Negativos"]]
            plot_postivio_negativo(stats_b)   
            st.markdown("---")
            
        with ciclo2:    
            #plotando gráfico de barras com o percentual de resultados positivos e negativos de cada mês
            stats_b = estatistica(tabela_retornos2)[["Positivos", "Negativos"]]
            plot_postivio_negativo(stats_b)   
            st.markdown("---")
            
        with ciclo3:    
            #plotando gráfico de barras com o percentual de resultados positivos e negativos de cada mês
            stats_b = estatistica(tabela_retornos3)[["Positivos", "Negativos"]]
            plot_postivio_negativo(stats_b)   
            st.markdown("---")
            
            
        with ciclo4:    
            #plotando gráfico de barras com o percentual de resultados positivos e negativos de cada mês
            stats_b = estatistica(tabela_retornos4)[["Positivos", "Negativos"]]
            plot_postivio_negativo(stats_b)   
            st.markdown("---") 
            
    if option == "Ethereum":
        st.title("Análise Quantitativa " + option)
        st.markdown("---")
        ################################
        #Plotando Gráfico do Ethereum
        st.subheader("Gráfico ETH")
        #Obtendo dados OHLC ---> Aqui vamos utilizar a YahooFinance para obter todos os dados necessários
        eth = yf.download("ETH-USD", period="10y", interval="1d")       
        #Plotando Gráfico
        plot_candlestick(eth)
        
        # criando dataframe com variação percentual do preço de fechamento
        eth_percent = round(eth["Close"].pct_change()*100).dropna()
        # Criando dataframe que agrupa os dados em Ano e Mes
        retorno_mensal = retorno(eth_percent)

        # criando dataframe/tabela onde o Indice é o ANO, e as colunas são os retornos mensais
        tabela_retornos = pd.DataFrame(retorno_mensal)
        tabela_retornos = pd.pivot_table(tabela_retornos, values=["Close"], index="Year", columns="Month")
        # Trocando formato do nome dos meses Numero->Nome Abreviado
        tabela_retornos.columns = ["Jan", "Fev", "Mar", "Abr","Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        
        st.subheader("Retorno % Mensal")
        #Plotando HEATMAP com os retornos mensais
        cor_padrao = [[0, 'red'], [0.55, 'yellow'], [1.0, 'green']]
        plot_retorno_mensal(tabela_retornos,cor_padrao, 100,900)
        st.markdown("---")
        st.subheader("Resumo Estatístico %")
        #plotando informações estatíticas
        stats_a = estatistica(tabela_retornos)[["Média","Mediana","Maior","Menor"]]
        # trocando indice pelas colunas e arredondando o valor para duas casas decimais 
        stats_a = stats_a.transpose().round(1)
        #Definindo paleta de cores para o heatmap 
        #Plotando HEATMAP com resumo estatístico
        plot_estatistica(stats_a,cor_padrao)
        st.markdown("---")
        st.subheader("Meses Positivos X Negativos")
        #plotando gráfico de barras com o percentual de resultados positivos e negativos de cada mês
        stats_b = estatistica(tabela_retornos)[["Positivos", "Negativos"]]
        plot_postivio_negativo(stats_b)   
        st.markdown("---") 

    if option == "SP500":
        
        st.title("Análise Quantitativa " + option)
        st.markdown("---")
        ################################
        #Plotando Gráfico do BTC
        st.subheader("Gráfico SPX")
        #Obtendo dados OHLC ---> Aqui vamos utilizar a YahooFinance para obter todos os dados necessários
        spx = yf.download("^GSPC", period="10y", interval="1d")
        
        #Plotando Gráfico
        plot_candlestick(spx)

        #importando dataframe
        spx_data = load_data("SPX.csv")
        # removendo coluna vazia
        spx_data.drop("Volume", axis=1)
        #criando dataset com valores a partir do ano 2000 
        spx_recente = spx_data[18078:]

        # criando dataframe com variação percentual
        spx_percent = round(spx_recente["Adj Close"].pct_change()*100)

        # Criando dataframe que agrupa os dados em Ano e Mes
        retorno_mensal = retorno(spx_percent)

        # criando dataframe/tabela onde o Indice é o ANO, e as colunas são os retornos mensais
        tabela_retornos = pd.DataFrame(retorno_mensal)
        tabela_retornos = pd.pivot_table(tabela_retornos, values=["Adj Close"], index="Year", columns="Month")
        # Trocando formato do nome dos meses Numero->Nome Abreviado
        tabela_retornos.columns = ["Jan", "Fev", "Mar", "Abr","Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

        #Plotando HEATMAP com os retornos mensais
        cor_padrao = [[0, 'red'], [0.55, 'yellow'], [1.0, 'green']]
        plot_retorno_mensal(tabela_retornos,cor_padrao, 100,900)
        st.markdown("---")
        #plotando informações estatíticas
        stats_a = estatistica(tabela_retornos)[["Média","Mediana","Maior","Menor"]]
        # trocando indice pelas colunas e arredondando o valor para duas casas decimais 
        stats_a = stats_a.transpose().round(2)
        #Definindo paleta de cores para o heatmap 
        #Plotando HEATMAP com resumo estatístico
        plot_estatistica(stats_a,cor_padrao)
        st.markdown("---")
        
        #plotando gráfico de barras com o percentual de resultados positivos e negativos de cada mês
        stats_b = estatistica(tabela_retornos)[["Positivos", "Negativos"]]
        plot_postivio_negativo(stats_b)   
        st.markdown("---") 
        


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


##################################################################################
##################################################################################
##################################################################################

def main():
    with st.container():
        st.image("btc_whitepaper_wordcloud.png")
    st.sidebar.title("Panorama Cripto")
    st.sidebar.markdown("---")
    lista_menu = ["Home","Panorama", "Gráficos","Análise Quantitativa"]
    escolha = st.sidebar.radio("Escolha uma opção", lista_menu)

    if escolha == "Home":
        home()
    if escolha == "Panorama":
        panorama()
    if escolha == "Gráficos":
        graficos()
    if escolha == "Análise Quantitativa":
        option = st.sidebar.selectbox("Escolha um Ativo", ("Bitcoin","Ethereum","SP500"))
        analise_quant(option)
    st.sidebar.markdown("---")


main()
