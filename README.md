# sabesp-dashboard

Projeto parte de um TCC em Ciência de Dados da Univesp que visa aumentar a acessibilidade dos dados de sistemas produtores fornecios pela SABESP. Este repositório foca na visualização dos dados para o público geral. O [segundo repositório](https://github.com/GMerencio/sabesp-api) foca na construção de uma API para desenvolvedores e disponibilização dos dados em formatos acessíveis.

[A aplicação pode ser acessada aqui](https://sabesp-dashboard.streamlit.app/).

## Tecnologias

As principais tecnologias usadas no projeto são:

* [Python 3.8](https://www.python.org/)
* [Plotly](https://plotly.com/)
* [Streamlit](https://streamlit.io/)

## Estrutura do projeto

Os principais arquivos e diretórios são:

* `streamlit-app.py`: Arquivo de entrada e página principal da aplicação Streamlit responsável pela interface de visualização.
* `plotting_utils.py`: Funções de auxílio para as visualizações de dados.
* `dashboard.py`: Arquivo contendo as funções básicas usada na maioria das páginas, incluindo os gráficos e filtros.
* `pages`: Diretório contendo as demais páginas da aplicação Streamlit, cada uma em um arquivo.

## Setup 

 1. Instale [`pipenv`](https://pypi.org/project/pipenv/).
 2. No diretório do projeto, execute `pipenv install` no terminal.
 3. Para ativar o ambiente virtual, execute `pipenv shell`.
 4. Para rodar a aplicação Streamlit localmente, execute `streamlit run streamlit-app.py` no terminal. Lembre de ativar o ambiente virtual antes.
