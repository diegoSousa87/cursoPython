import streamlit as st #conjunto de ferramentas para trabalho de programação web
import datetime

#para instalar streamlit, comando pip install streamlit
#arquivo com streamlit deve ser executado no próprio terminal, "streamlit run nome do arquivo .py"

st.title("World Veiculos")
st.write("Desfile com os melhores modelos")

data_minima= 1900
data_maxima= 2100
ano_atual= datetime.datetime.now().year

nome= st.text_input('Digite seu nome:')
marca= st.text_input('Qual a marca do veículo')
veiculo= st.text_input('Qual o modelo do veículo')
cor= st.text_input('Qual a cor:')
notaSat = st.selectbox("Nota de satisfação com o veiculo:", list(range(11)), index=10)#index deixa pré selecionado o numero 10
anoFab= st.number_input('Ano de Fabricação', value=ano_atual, min_value= data_minima, max_value= data_maxima)
idade= ano_atual - anoFab

st.write(f'Olá {nome}')
st.write(f'O veículo {veiculo} da marca {marca} possui {idade} ano de uso')

bio= st.text_area('Descreva características do veículo') #cria um editor de texto para digitação