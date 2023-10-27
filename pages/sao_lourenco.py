import streamlit as st
import pandas as pd
import datetime
from st_pages import add_page_title
from plotting_utils import plot_df
from dashboard import carregar_dados, renderizar_dados

CAMINHO_DADOS = 'https://github.com/GMerencio/sabesp-api/raw/main/dados/sao_lourenco.csv'

add_page_title()
df = carregar_dados(CAMINHO_DADOS)
renderizar_dados(df, 'sao_lourenco')