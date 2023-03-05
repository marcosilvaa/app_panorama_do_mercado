import streamlit as st

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
