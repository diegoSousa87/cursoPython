import streamlit as st #conjunto de ferramentas para trabalho de programação web
import datetime

#para instalar streamlit, comando pip install streamlit
#arquivo com streamlit deve ser executado no próprio terminal, "streamlit run nome do arquivo .py"

st.title("Hello World")
st.write("Hello World! I am back!")

data_minima= datetime.date(1900, 1, 1)
data_maxima= datetime.date(2100, 12, 31)

nome= st.text_input('Qual o seu nome?')
idade= st.number_input('Idade?', step=1, value=0, format='%d')
Dtnasc= st.date_input('Nasc?', format= 'DD/MM/YYYY', min_value= data_minima, max_value= data_maxima)

st.write(f'Olá {nome} de {idade} anos!')

#st.write('Fale um pouco sobre você')
bio= st.text_area('Fale um pouco sobre você') #cria um editor de texto para digitação
