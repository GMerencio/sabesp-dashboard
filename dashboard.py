import streamlit as st
import pandas as pd
import datetime
from st_pages import add_page_title
from plotting_utils import plot_df

# Carregar dados

def carregar_dados(caminho_dados):
	df = pd.read_csv(caminho_dados)
	df['Data'] = pd.to_datetime(df['Data']).dt.date
	df['Volume (hm³)'] = df['Volume (hm³)'].astype(float)
	df['Volume (%)'] = df['Volume (%)'].astype(float)
	df['Chuva (mm)'] = df['Chuva (mm)'].astype(float)
	df['Vazão natural (m³/s)'] = df['Vazão natural (m³/s)'].astype(float)
	df['Vazão a jusante (m³/s)'] = df['Vazão a jusante (m³/s)'].astype(float)
	return df

def renderizar_dados(df, sistema):
	st.markdown('''Selecione o período de consulta e o dado que deseja visualizar.''')
	
	data_hoje = datetime.datetime.now()
	data_inicio = datetime.date(2000, 1, 1)
	
	inicio_consulta = st.date_input(
		'Início do período de consulta',
   	data_inicio,
   	data_inicio,
   	data_hoje,
   	format="DD.MM.YYYY",
	)
	
	final_consulta = st.date_input(
		'Final do período de consulta',
   	data_hoje,
   	data_inicio,
   	data_hoje,
   	format="DD.MM.YYYY",
	)
	
	colunas = df.columns[1:].to_list()
	
	coluna1 = st.selectbox(
		'Selecione qual dado quer visualizar no primeiro gráfico',
  	colunas
	)
	
	coluna2 = st.selectbox(
		'Selecione qual dado quer visualizar no segundo gráfico',
  	colunas,
  	index=colunas.index('Chuva (mm)')
	)
	
	df = df[(df['Data'] >= inicio_consulta) & (df['Data'] <= final_consulta)]
	
	col1, col2 = st.columns(2)
	
	with col1:
		st.plotly_chart(plot_df(df, ylabel=coluna1), use_container_width=True)
	with col2:
		st.plotly_chart(plot_df(df, ylabel=coluna2), use_container_width=True)
	
	st.write(df)
	
	st.download_button(
		label="Baixar os dados como .csv",
		data=df.to_csv().encode('utf-8'),
		file_name=f'dados_{sistema}.csv',
		mime='text/csv'
	)