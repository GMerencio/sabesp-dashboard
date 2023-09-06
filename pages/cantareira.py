import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import datetime
from st_pages import add_page_title

# Carregar dados

@st.cache_data
def carregar_dados():
	df = pd.read_csv('cantareira_2011-2023.csv')
	df['Data'] = df['Data'].astype('datetime64[ns]')
	df['Volume (hm³)'] = df['Volume (hm³)'].astype(float)
	df['Volume (%)'] = df['Volume (%)'].astype(float)
	df['Chuva (mm)'] = df['Chuva (mm)'].astype(float)
	df['Vazão natural (m³/s)'] = df['Vazão natural (m³/s)'].astype(float)
	df['Vazão a jusante (m³/s)'] = df['Vazão a jusante (m³/s)'].astype(float)
	return df

def plot(df):
	line_width = 2
	marker_size = 4
	figsize = (900, 600)
	xlabel = 'Data'
	ylabel = 'Volume (hm³)'
	
	prediction_color = '#0072B2'
	actual_color = 'black'
	trend_color = '#B23B00'
	bg_color = 'white'
	txt_color = 'black'
	grid_color = '#cfcfcf'
	btn_color = 'white'
	hover_bg_color = 'white'
	
	data = []
  	
	# Add actual
	data.append(go.Scattergl(
  	name='Observado',
  	x=df['Data'],
  	y=df['Volume (hm³)'],
  	marker=dict(color=actual_color, size=marker_size),
  	mode='markers',
  	xhoverformat='%d/%m/%Y'
	))
	
	layout = dict(
      	showlegend=False,
      	width=figsize[0],
      	height=figsize[1],
      	plot_bgcolor=bg_color,
      	paper_bgcolor=bg_color,
      	font=dict(
        		color=txt_color,
        		size=15
      	),
      	hoverlabel=dict(
        		bgcolor=hover_bg_color,
        		font=dict(
        				color=txt_color
        		)
      	),
      	yaxis=dict(
          	title=dict(
            		text=ylabel,
            		font=dict(
            				color=txt_color,
            				size=15
            		)
          	),
          	tickfont=dict(
            		color=txt_color,
            		size=15
          	),
          	gridcolor=grid_color
      	),
      	xaxis=dict(
          	title=dict(
            		text=xlabel,
            		font=dict(
            				color=txt_color,
            				size=15
            		)
          	),
          	tickfont=dict(
            		color=txt_color,
            		size=15
          	),
          	type='date',
          	gridcolor=grid_color,
          	rangeselector=dict(
            		bgcolor=btn_color,
              	buttons=list([
                  	dict(count=7,
                        	label='1 semana',
                        	step='day',
                        	stepmode='backward'),
                  	dict(count=1,
                        	label='1 mês',
                        	step='month',
                        	stepmode='backward'),
                  	dict(count=6,
                        	label='6 meses',
                        	step='month',
                        	stepmode='backward'),
                  	dict(count=1,
                        	label='1 ano',
                        	step='year',
                        	stepmode='backward'),
                  	dict(label='Tudo',
                        	step='all')
              	])
          	),
          	rangeslider=dict(
              	visible=False
          	),
      	),
  	)
    
	fig = go.Figure(data=data, layout=layout)
	return fig

add_page_title()

df = carregar_dados()

st.markdown('''Bem-vindo! Este dashboard disponibiliza os dados dos sistemas produtores que abastacem a Região Metropolitana de São Paulo. Acesse os dados de cada sistema pelo menu à esquerda.''')

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

coluna = st.selectbox(
    'Selecione qual dado quer visualizar',
    df.columns[1:])

st.plotly_chart(plot(df), use_container_width=True)

st.write(df)

st.download_button(
	label="Baixar os dados como .csv",
	data=df.to_csv().encode('utf-8'),
	file_name='dados_cantareira.csv',
	mime='text/csv'
)