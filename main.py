# Importando bibliotecas
import streamlit as st

import Pages.Cliente.home as HomePage
import Pages.Cliente.panorama as PanoramaPage
import Pages.Cliente.grafico as ChartPage
import Pages.Cliente.analise as AnalisePage

def main():
    
    st.image("btc_whitepaper_wordcloud.png")
    st.sidebar.title("Panorama Cripto")
    st.sidebar.markdown("---")
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
