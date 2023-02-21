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
    st.subheader("Mercados pelo Mundo")

    dict_tickers = {
        "Bovespa" : "^BVSP",
        "S&P500" : "^GSPC",
        "NASDAQ" : "^IXIC",
        "DAX" : "^GDAXI",
        "FTSE 100" : "^FTSE",
        "CRUDE OIL" : "CL=F",
        "GOLD" : "GC=F",
        "BITCOIN" : "BTC-USD",
        "ETHEREUM" : "ETH-USD",
        "Dow Jones Industrial":"^DJI",
        "Dow Jones Transportes": "^DJT",
        "HANG SENG": "^HSI"

    }
    #Criando dataframe para armazenar os valores de cada item que serão coletados posteriormente
    df_info = pd.DataFrame({"Ativo": dict_tickers.keys(),
                            "Ticker": dict_tickers.values()})
    #Criando as colunas onde serão armazenados os valores
    df_info["Ult.Valor"]= " "
    df_info["%"] =" "

    #Imprimindo na tela mensagem "Carregando"
    with st.spinner("Coletando Cotações"):

        #Criando loop para download dos dados
        #Utilizando a biblioteca YFinance vamos fazer o download para cada item do dicionário
        count = 0
        for ticker in dict_tickers.values():
           cotacoes = yf.download(ticker,period="1mo",auto_adjust=True)["Close"]
           variacao = ((cotacoes.iloc[-1]/cotacoes.iloc[-2])-1)*100
           df_info["Ult.Valor"][count] = round(cotacoes.iloc[-1],2)
           df_info["%"][count] = round(variacao,2)
           count += 1

    #Criando colunas na tela para exibir o valor de cada índice e a variação % do dia
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(df_info["Ativo"][0], df_info["Ult.Valor"][0], delta=str(df_info["%"][0]) + "%")
        st.metric(df_info["Ativo"][1], df_info["Ult.Valor"][1], delta=str(df_info["%"][1])+ "%")
        st.metric(df_info["Ativo"][2], df_info["Ult.Valor"][2], delta=str(df_info["%"][2])+ "%")
        st.metric(df_info["Ativo"][3], df_info["Ult.Valor"][3], delta=str(df_info["%"][3])+ "%")

    with col2:
        st.metric(df_info["Ativo"][4], df_info["Ult.Valor"][4], delta=str(df_info["%"][4])+ "%")
        st.metric(df_info["Ativo"][5], df_info["Ult.Valor"][5], delta=str(df_info["%"][5])+ "%")
        st.metric(df_info["Ativo"][6], df_info["Ult.Valor"][6], delta=str(df_info["%"][6])+ "%")
        st.metric(df_info["Ativo"][7], df_info["Ult.Valor"][7], delta=str(df_info["%"][7])+ "%")

    with col3:
        st.metric(df_info["Ativo"][8], df_info["Ult.Valor"][8], delta=str(df_info["%"][8])+ "%")
        st.metric(df_info["Ativo"][9], df_info["Ult.Valor"][9], delta=str(df_info["%"][9])+ "%")
        st.metric(df_info["Ativo"][10], df_info["Ult.Valor"][10], delta=str(df_info["%"][10])+ "%")
        st.metric(df_info["Ativo"][11], df_info["Ult.Valor"][11], delta=str(df_info["%"][11])+ "%")

    st.markdown("---")

    st.subheader("Gráfico")

    #Criando caixa com os nomes dos papeis
    indice_selecionado = st.selectbox("Selecione o Índice",dict_tickers.keys())

    for ticker in dict_tickers.keys():
        if not ticker == indice_selecionado:
            pass
        else:
            indice_diario = yf.download(dict_tickers.get(indice_selecionado), period="60d", interval="1d")

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



    #with st.expander("", expanded=True):
    #   opcao = st.radio("Escolha",["Indice","Criptos"])

    #if opcao == "Indice":
    #    with st.form(key="form_indice"):
    #        ticker = st.selectbox("Indice", ["Bovespa", "Financials", "Basic Materials"])
    #        analisar = st.form_submit_button("Analisar")
    #else:
    #    with st.form(key="form_criptos"):
    #        ticker = st.selectbox("Criptos", ["BTC", "ETH", "ADA"])
    #        analisar = st.form_submit_button("Analisar")

    #if analisar:
    #    data_inicial = "01/12/1999"
    #    data_final = "31/12/2023"

    #    if opcao == "Criptos":
    #        retornos = yf.download(ticker+"-USD", period="max")["Close"].pct_change()
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