# Importando bibliotecas
import streamlit as st
#from streamlit_option_menu import option_menu

import Pages.Cliente.home as HomePage
import Pages.Cliente.panorama as PanoramaPage
import Pages.Cliente.grafico as ChartPage
import Pages.Cliente.grafico_copy as CryptoPage
import Pages.Cliente.analise as AnalisePage



st.set_page_config(
     page_title="Panorama Cripto",
     page_icon="💸",
     initial_sidebar_state="collapsed",
     layout="centered",
     menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    })


hide_menu_style = """

<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_menu_style, unsafe_allow_html=True)


# Inclua o código HTML do TradingView em uma string
tradingview_widget = """
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
    <div class="tradingview-widget-container__widget"></div>

    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>
    {
    "symbols": [
        {
        "proName": "FOREXCOM:SPXUSD",
        "title": "S&P 500"
        },
        {
        "proName": "FOREXCOM:NSXUSD",
        "title": "US 100"
        },
        {
        "proName": "FX_IDC:EURUSD",
        "title": "EUR/USD"
        },
        {
        "proName": "BITSTAMP:BTCUSD",
        "title": "Bitcoin"
        },
        {
        "proName": "BITSTAMP:ETHUSD",
        "title": "Ethereum"
        },
        {
        "description": "BRL/USD",
        "proName": "FX_IDC:BRLUSD"
        },
        {
        "description": "Crypto Index",
        "proName": "CAPITALCOM:CIX"
        }
    ],
    "showSymbolLogo": true,
    "colorTheme": "dark",
    "isTransparent": true,
    "displayMode": "adaptive",
    "locale": "en"
    }
    </script>
    </div>
    <!-- TradingView Widget END -->

"""




def main():    
    #st.image("btc_whitepaper_wordcloud.png", width=1800,output_format="auto",use_column_width=False)
    
    # 3. CSS style definitions
    # escolha = option_menu(None, ["Panorama",  "Gráficos", 'Análise Quantitativa',"Home" ], 
    # icons=['bi-binoculars', "graph-up-arrow", 'clipboard-data','house'], 
    # menu_icon="cast", default_index=0, orientation="horizontal",
    # styles={
    #     "container": {"padding": "0!important", "background-color": "#0E1117"},
    #     "icon": {"color": "green", "font-size": "30px"}, 
    #     "nav-link": {"font-size": "25px", "text-align": "center", "margin":"0px", "--hover-color": "#AAA"},
    #     "nav-link-selected": {"background-color": "orange"},
    # }
    # )

    st.components.v1.html(tradingview_widget, height=75)

    # if escolha == "Panorama":
    #     PanoramaPage.panorama()
        
    # if escolha == "Home":
    #     HomePage.home()
        
    # if escolha == "Gráficos":
    #     ChartPage.graficos()
    
    # if escolha == "Cryptos":
    #     CryptoPage.cryptocurency()

    # if escolha == "Análise Quantitativa":
    #     AnalisePage.analise_quant()
    lista_menu = ["Home","Análise Quantitativa","Panorama", "Gráficos"]
    escolha = st.sidebar.radio("Escolha uma opção", lista_menu)

    if escolha == "Home":
        HomePage.home()

    if escolha == "Panorama":
        PanoramaPage.panorama()

    if escolha == "Gráficos":
        ChartPage.graficos()

    if escolha == "Análise Quantitativa":
        AnalisePage.analise_quant()
        
        
    st.sidebar.markdown("---")
    
main()
