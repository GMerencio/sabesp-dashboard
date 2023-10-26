import pandas as pd
import plotly.graph_objs as go

def plot_df(df, ylabel='Volume (hm³)'):
	line_width = 2
	marker_size = 4
	figsize = (900, 600)
	xlabel = 'Data'
	
	prediction_color = '#0072B2'
	actual_color = 'black'
	trend_color = '#B23B00'
	bg_color = 'white'
	txt_color = 'black'
	grid_color = '#cfcfcf'
	btn_color = 'white'
	hover_bg_color = 'white'
	
	data = []
	
	if ylabel == 'Chuva (mm)':
		df_mes = df.copy()
		df_mes = df_mes[['Data', 'Chuva (mm)']]
		
		data_inicio = df.iloc[0]['Data']
		data_final = df.iloc[-1]['Data']
		dif_segundos = (data_final - data_inicio).total_seconds()
		dif_anos = divmod(dif_segundos, 31536000)[0]
		
		if dif_anos >= 10:
			df_mes['Data'] = pd.to_datetime(df_mes['Data']).dt.strftime('%Y')
		else:
			df_mes['Data'] = pd.to_datetime(df_mes['Data']).dt.strftime('%m/%y')
		
		gp_mes = df_mes.groupby(['Data'], sort=False).sum().reset_index()
		
		data.append(go.Bar(
  		x=gp_mes['Data'],
  		y=gp_mes[ylabel]
		))
	else:
		data.append(go.Scattergl(
  		name='Observado',
  		x=df['Data'],
  		y=df[ylabel],
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
          	rangeslider=dict(
              	visible=False
          	),
      	),
  	)
    
	fig = go.Figure(data=data, layout=None)
	return fig