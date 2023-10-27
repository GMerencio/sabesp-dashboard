import streamlit as st
import pandas as pd
from st_pages import add_page_title

add_page_title()

st.markdown('''A fonte dos dados do projeto é a [Sabesp](https://mananciais.sabesp.com.br/HistoricoSistemas?SistemaId=0), que disponibiliza dados referentes ao sistemas produtores. A nível de sistemas, as seguintes informações estão disponíveis: 

* Data: data do registro, no formato AAAA-MM-DD (por exemplo, 2000-12-31);
* Volume (hm³): corresponde ao volume armazenado, em hectômetros cúbicos; 
* Vazão natural (m³/s): representa a vazão média diária afluente, em metros cúbicos por segundo, sem considerar as alterações antrópicas; 
* Vazão a jusante (m³/s): indica a vazão média diária descarregada, em metros cúbicos por segundo, para a jusante da barragem, ou seja, a quantidade de água liberada que segue pelo rio ou canal após o barramento; 
* Chuva (mm): refere-se à precipitação acumulada nas últimas 24 horas no local do barramento, em milímetros. 

Os dados são atualizados diariamente através de um script e disponibilizados via API. Você pode acessar o código-fonte e os dados, incluindo os dados dos reservatórios de cada sistema, [neste repositóro do GitHub](https://github.com/GMerencio/sabesp-api).''')