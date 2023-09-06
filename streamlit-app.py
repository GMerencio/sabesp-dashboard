import pandas as pd
import streamlit as st
import datetime as dt
from st_pages import Page, show_pages

# Configurações da página

st.set_page_config(
	page_title='Dashboard Sabesp'
)

# Definição das páginas da aplicação

show_pages(
    [
        Page('streamlit-app.py', 'Página inicial', ':house:'),
        Page('pages/cantareira.py', 'Sistema Cantareira'),
        Page('pages/alto_tiete.py', 'Sistema Alto Tietê'),
        Page('pages/guarapiranga.py', 'Sistema Guarapiranga'),
        Page('pages/cotia.py', 'Sistema Cotia'),
        Page('pages/rio_grande.py', 'Sistema Rio Grande'),
        Page('pages/rio_claro.py', 'Sistema Rio Claro'),
        Page('pages/sao_lourenco.py', 'Sistema São Lourenço'),
        Page('pages/dados.py', 'Sobre os dados'),
        Page('pages/api.py', 'API'),
    ]
)
	
# Interface

st.title('Dashboard Sabesp')

st.markdown('''Bem-vindo! Este dashboard disponibiliza os dados dos sistemas produtores que abastacem a Região Metropolitana de São Paulo. Acesse os dados de cada sistema pelo menu à esquerda.''')