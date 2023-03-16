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


def analise_quant():
    st.title("Análise Quantitativa")

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
        
    class Dados:

        def __init__(self, df):
            self.df = df
            
        def tabela_retornos(self):
            # criando novo dataframe com preço de fechamento de cada mês
            fechamento_mensal = self.df.resample("M").last().pct_change()
            
            retorno_mensal = fechamento_mensal.groupby([fechamento_mensal.index.year.rename("Year"), fechamento_mensal.index.month.rename("Month")]).sum()*100
            tabela_retornos = round(retorno_mensal,2)
            tabela_retornos = pd.pivot_table(tabela_retornos, values="Close", index="Year",columns="Month")
            tabela_retornos.columns = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
            return tabela_retornos
        
        def estatistica(self):
            # Construindo novo dataframe com as informações estatísticas
            stats = pd.DataFrame()
            stats["Média"] = self.tabela_retornos().mean()
            stats["Mediana"] = self.tabela_retornos().median()
            return stats.round(1)
        
        def maior_menor(self):
            maior_menor = pd.DataFrame()
            maior_menor["Maior"] = self.tabela_retornos().max()
            maior_menor["Menor"] = self.tabela_retornos().min()
            return maior_menor.round(2)
            
        def volatilidade(self):
            vol = pd.DataFrame()
            vol["Volatilidade"] = self.tabela_retornos().std()
            return vol.round(3)

        def positivo_negativo(self):
            pos_neg = pd.DataFrame()
            # Método gt() -> Greater -> Maior que()
            # Esse método busca quantas vezes o resultado foi maior que, no caso zero.
            # método -> sum() vai soamr quantas vezes a condição foi verdadeira, depois é dividido pela quantidade de items da tabela
            pos_neg["Positivos"] = round(self.tabela_retornos().gt(0).sum()/self.tabela_retornos().count()*100)
            # Mesma lógica, porem agora o método le() vai mostrar os itens menores do que zero
            pos_neg["Negativos"] = round((self.tabela_retornos().le(0).sum()/self.tabela_retornos().count())*100)  
            return pos_neg
        
    ##########################################################

        # Plotando HEATMAP para retornos % mensais
        def plot_retorno_mensal(self,cor_padrao,width=800,height=800):
            fig = px.imshow(self.tabela_retornos(),
                    labels=dict(x="Mês", y="Ano",),
                    x=self.tabela_retornos().columns,
                    y=self.tabela_retornos().index)
            fig = px.imshow(self.tabela_retornos(), text_auto=True, aspect="auto",color_continuous_scale=cor_padrao)
            fig.update_layout(width=width, height=height, font_size=500)
            fig.update_layout(font_size=500)
            fig.update(layout_coloraxis_showscale=False)
            st.plotly_chart(fig,use_container_width=True)
            st.caption("Fonte Yahoo Finance")
        
          # Plotando HEATMAP com Informações estatísticas 
        def plot_estatistica(self, cor_padrao):
            col1,col2,col3 = st.columns(3)
            with col1:        
                fig1 = px.imshow(self.volatilidade(),
                        labels=dict(x="Mês", y="Ano",),
                        x=self.volatilidade().columns,
                        y=self.volatilidade().index)
                fig1 = px.imshow(self.volatilidade(), text_auto=True, aspect="auto",color_continuous_scale=cor_padrao)
                fig1.update_layout(width=1000, height=600, font_size=10)
                fig1.update_layout(font_size=20)
                fig1.update(layout_coloraxis_showscale=False)
                st.plotly_chart(fig1,use_container_width=True)
            with col2: 
                fig2 = px.imshow(self.estatistica(),
                        labels=dict(x="Mês", y="Ano",),
                        x=self.estatistica().columns,
                        y=self.estatistica().index)
                fig2 = px.imshow(self.estatistica(), text_auto=True, aspect="auto",color_continuous_scale=cor_padrao)
                fig2.update_layout(width=1000, height=600, font_size=10)
                fig2.update_layout(font_size=20)
                fig2.update(layout_coloraxis_showscale=False)
                st.plotly_chart(fig2,use_container_width=True)
            with col3:            
                fig3 = px.imshow(self.maior_menor(),
                        labels=dict(x="Mês", y="Ano",),
                        x=self.maior_menor().columns,
                        y=self.maior_menor().index)
                fig3 = px.imshow(self.maior_menor(), text_auto=True, aspect="auto",color_continuous_scale=cor_padrao)
                fig3.update_layout(width=1000, height=600, font_size=10)
                fig3.update_layout(font_size=20)
                fig3.update(layout_coloraxis_showscale=False)
                st.plotly_chart(fig3,use_container_width=True)
                            
            st.caption("Fonte Yahoo Finance")
    
            # Plotando Gráfico de BARRAS para comparação entre meses Positivos X Negativos
        def plot_postivio_negativo(self):
            fig = px.bar(self.positivo_negativo(), color_discrete_map={'Negativos': 'red', 'Positivos': 'green'})
            st.plotly_chart(fig, use_container_width=True)
            st.caption("Fonte Yahoo Finance")
    
        def plot_candlestick(self):
            # criando figura
            fig = go.Figure()
            # criando gráfico
            fig.add_trace(
                go.Candlestick(x=self.df.index,
                            open=self.df['Open'],
                            high=self.df['High'],
                            low=self.df['Low'],
                            close=self.df['Close']))
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
                
    #Criando abas 
    btc, eth, spx, dxy = st.tabs(["Bitcoin", "Ethereum", "SPX", "DXY"])
    with btc:
        
        #Obtendo dados OHLC ---> Aqui vamos utilizar a YahooFinance para obter todos os dados necessários
        btc_ohlc = yf.download("BTC-USD", period="max", interval="1d")
        ##################################################################
        #importando dados
        btc_historico = load_data("https://www.lookintobitcoin.com/bitcoin-price-download/")
        #removendo coluna sem dados 
        btc_historico.drop("Unnamed: 0", axis=1, inplace=True)
        btc_historico = btc_historico.rename(columns={"Price":"Close"})
        
        
        #Plotando Gráfico do BTC
        st.subheader("Gráfico BTC")
        btc_ohlc = Dados(btc_ohlc)
        btc_ohlc.plot_candlestick()
        
        #Criando obejos para cada ciclo e ciclo total
        btc_t = Dados(btc_historico)
        btc_c1 = Dados(btc_historico.iloc[:835])
        btc_c2 = Dados(btc_historico.iloc[835:2124])
        btc_c3 = Dados(btc_historico.iloc[2124:3556])        
        btc_c4 = Dados(btc_historico.iloc[3556:])


        ### PLOTANDO GRAFICO COM OS 3 CICLOS
        
        ciclos = [(0, 835), (835, 2124), (2124, 3556), (3556, len(btc_historico))]
        fig = go.Figure()

        for i, (start, end) in enumerate(ciclos):
            ciclo = btc_historico.iloc[start:end].reset_index()
            ciclo = ciclo.rename(columns={'index': 'Date'})
            ciclo['numero'] = ciclo.index + 1
            ciclo = ciclo[['numero', 'Date', 'Close']]
            fig.add_trace(go.Scatter(x=ciclo['numero'], y=ciclo['Close'], mode='lines', name=f'Ciclo {i+1}'))
        fig.update_yaxes(type="log")
        fig.update_layout(width=1000, height=800, font_size=200)
        
        fig.update_layout(xaxis_range=[0, 1450], xaxis_tickvals=[0, 669, 2130, 3560])
        st.plotly_chart(fig, use_container_width=True)

        
        ###PLOTANDO RETORNOS MENSAIS 
        st.subheader("Retorno % Mensal")
        total, ciclo1, ciclo2, ciclo3, ciclo4 = st.tabs(["Total", "Ciclo 1", "Ciclo 2", "Ciclo 3", "Ciclo4"])
        
        with total:
            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.095, 'yellow'], [1.0, 'green']]
            #plotando heatmap com retornos mensais
            btc_t.plot_retorno_mensal(cor_padrao)
            st.markdown("---")
        
        with ciclo1: 
            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.1, 'yellow'], [1.0, 'green']]
            #plotando heatmap com retornos mensais
            with st.expander("Ciclo 1"):
                st.write("O primeiro ciclo do Bitcoin durou até  o dia 28 de Novembro de 2012")
            btc_c1.plot_retorno_mensal(cor_padrao,900,500)
            st.markdown("---")

        with ciclo2: 
            #Plotando HEATMAP com retornos % mensais 
            cor_padrao = [[0, 'red'], [0.07, 'yellow'], [1.0, 'green']]
            with st.expander("Ciclo 2"):
                st.write("O segundo ciclo do Bitcoin ocorreu entre o dia 28 de Novembro de 2012 até 09 de Julho de 2016")
            #plotando heatmap com retornos mensais
            btc_c2.plot_retorno_mensal(cor_padrao,900,500)
            st.markdown("---")
            
        with ciclo3: 
            
            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.425, 'yellow'], [1.0, 'green']]
            with st.expander("Ciclo 3"):
                st.write("O terceiro ciclo do Bitcoin ocorreu entre o dia 09 de Julho de 2016 até 11 de Maio de 2020")
            
            #plotando heatmap com retornos mensais
            btc_c3.plot_retorno_mensal(cor_padrao,900,500)
            st.markdown("---")
            
        with ciclo4: 
            st.write("O quarto ciclo do Bitcoin ocorreu entre o dia 11 de Maio de 2020 e estima-se que vai terminar em Maio de 2024")
            
            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.425, 'yellow'], [1.0, 'green']]
            #plotando heatmap com retornos mensais
            btc_c4.plot_retorno_mensal(cor_padrao,900,500)
            st.markdown("---")

        ### PLOTANDO ESTATISTICAS
        st.subheader("Resumo Estatístico (%)")
        total, ciclo1, ciclo2, ciclo3, ciclo4 = st.tabs(["Total", "Ciclo 1", "Ciclo 2", "Ciclo 3", "Ciclo4"])
        
        with total: 

            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.08, 'yellow'], [1.0, 'green']]
            #Plotando HEATMAP com resumo estatístico
            btc_t.plot_estatistica(cor_padrao)
            st.markdown("---")

        with ciclo1: 
            st.write("O primeiro ciclo do Bitcoin durou até  o dia 28 de Novembro de 2012")
            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.08, 'yellow'], [1.0, 'green']]
            #Plotando HEATMAP com resumo estatístico
            btc_c1.plot_estatistica(cor_padrao)
            st.markdown("---")
            
        with ciclo2: 
            st.write("O segundo ciclo do Bitcoin ocorreu entre o dia 28 de Novembro de 2012 até 09 de Julho de 2016")
            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.06, 'yellow'], [1.0, 'green']]
            #Plotando HEATMAP com resumo estatístico
            btc_c2.plot_estatistica(cor_padrao)
            st.markdown("---")
        
        with ciclo3: 
            st.write("O terceiro ciclo do Bitcoin ocorreu entre o dia 09 de Julho de 2016 até 11 de Maio de 2020")
            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.3, 'yellow'], [1.0, 'green']]
            #Plotando HEATMAP com resumo estatístico
            btc_c3.plot_estatistica(cor_padrao)
            st.markdown("---")
            
        with ciclo4: 
            st.write("O quarto ciclo do Bitcoin iniciou no dia 11 de Maio de 2020 e estima-se que vai terminar em Maio de 2024")
            #Definindo paleta de cores para o heatmap 
            cor_padrao = [[0, 'red'], [0.5, 'yellow'], [1.0, 'green']]
            #Plotando HEATMAP com resumo estatístico
            btc_c4.plot_estatistica(cor_padrao)
            st.markdown("---")
        
        
        st.subheader("Meses Positivos X Negativo - (%)")
        total, ciclo1, ciclo2, ciclo3, ciclo4 = st.tabs(["Total", "Ciclo 1", "Ciclo 2", "Ciclo 3", "Ciclo4"])

        with total:

        #plotando gráfico de barras com o percentual de resultados positivos e negativos de cada mês
            btc_t.plot_postivio_negativo()   
            st.markdown("---")
        
        with ciclo1:
            st.write("O primeiro ciclo do Bitcoin durou até  o dia 28 de Novembro de 2012")
            #plotando gráfico de barras com o percentual de resultados positivos e negativos de cada mês
            btc_c2.plot_postivio_negativo()   
            st.markdown("---")
            
        with ciclo2:    
            st.write("O segundo ciclo do Bitcoin ocorreu entre o dia 28 de Novembro de 2012 até 09 de Julho de 2016")
            #plotando gráfico de barras com o percentual de resultados positivos e negativos de cada mês
            btc_c2.plot_postivio_negativo()   
            st.markdown("---")
            
        with ciclo3:    
            st.write("O terceiro ciclo do Bitcoin ocorreu entre o dia 09 de Julho de 2016 até 11 de Maio de 2020")
            #plotando gráfico de barras com o percentual de resultados positivos e negativos de cada mês
            btc_c3.plot_postivio_negativo()   
            st.markdown("---")
            
        with ciclo4:    
            st.write("O quarto ciclo do Bitcoin ocorreu entre o dia 11 de Maio de 2020 e estima-se que vai terminar em Maio de 2024")
            
            #plotando gráfico de barras com o percentual de resultados positivos e negativos de cada mês
            btc_c4.plot_postivio_negativo()   
            st.markdown("---") 
              
    with eth: 
        
        #Plotando Gráfico do Ethereum
        st.subheader("Gráfico ETH")
        #Obtendo dados OHLC ---> Aqui vamos utilizar a YahooFinance para obter todos os dados necessários
        eth = yf.download("ETH-USD", period="10y", interval="1d")       
        
        eth_t = Dados(eth)
        
        #Plotando Gráfico
        eth_t.plot_candlestick()
        
        st.subheader("Retorno % Mensal")
        #Plotando HEATMAP com os retornos mensais
        cor_padrao = [[0, 'red'], [0.55, 'yellow'], [1.0, 'green']]
        #plot_retorno_mensal(tabela_retornos,cor_padrao, 100,900)
        eth_t.plot_retorno_mensal(cor_padrao)
        
        st.markdown("---")
        st.subheader("Resumo Estatístico %")

        #plotando informações estatíticas
        #Plotando HEATMAP com resumo estatístico
        eth_t.plot_estatistica(cor_padrao)
        st.markdown("---")
        st.subheader("Meses Positivos X Negativos")

        #plotando gráfico de barras com o percentual de resultados positivos e negativos de cada mês
        eth_t.plot_postivio_negativo()   
        st.markdown("---")     
        
    with spx:

        #Plotando Gráfico do BTC
        st.subheader("Gráfico SPX")
        #Obtendo dados OHLC ---> Aqui vamos utilizar a YahooFinance para obter todos os dados necessários
        spx = yf.download("^GSPC", period="30y", interval="1d")
        
        spx = Dados(spx)

        #Plotando Gráfico
        spx.plot_candlestick()

        #Plotando HEATMAP com os retornos mensais
        cor_padrao = [[0, 'red'], [0.55, 'yellow'], [1.0, 'green']]
        spx.plot_retorno_mensal(cor_padrao, 100,1000)
        st.markdown("---")

        #Plotando HEATMAP com resumo estatístico
        spx.plot_estatistica(cor_padrao)
        st.markdown("---")
        
        #plotando gráfico de barras com o percentual de resultados positivos e negativos de cada mês
        spx.plot_postivio_negativo()   
        st.markdown("---") 
        
        #PLotando BOXPLOT
        #plot_box(spx)
        
        ###########################################
        def load_company():
            url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies" 
            html = pd.read_html(url, header=0)  
            df = html[0]
            return df 
        df_company = load_company()
        df_company = pd.DataFrame(df_company,columns=["Symbol","Security","GICS Sector","GICS Sub-Industry"])

        setor = pd.DataFrame(df_company,columns=["Security","GICS Sector","GICS Sub-Industry"])
        
        setor = df_company.groupby("GICS Sector")
        composicao = round((setor["Symbol"].count()/len(df_company)*100))
        st.bar_chart(composicao)
        sub_setor = df_company.groupby("GICS Sub-Industry")
        composicao2 = round((sub_setor["Symbol"].count()/len(df_company)*100))
        st.bar_chart(composicao2)
        
    with dxy:
        st.write("DXY")
        
        dxy = yf.download("DX-Y.NYB", period="30y", interval="1d")
        
        dxy = Dados(dxy)
        
        dxy.plot_candlestick()
        
        cor_padrao = [[0, 'red'], [0.55, 'yellow'], [1.0, 'green']]
        
        
        dxy.plot_retorno_mensal(cor_padrao,1000,1500)
        dxy.plot_estatistica(cor_padrao)
        dxy.plot_postivio_negativo()