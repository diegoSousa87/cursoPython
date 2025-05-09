import streamlit as st #conjunto de ferramentas para trabalho de programação web
import json
import os
import datetime

ARQUIVO_DADOS= "veiculos.json"

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding="utf-8") as f:
            return json.load(f)
    return{}

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, 'w', encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii= False, indent= 4)

def criar_veiculo(nome, marca, veiculo, cor, notaSat, anoFab, idade):
    return{
        'nome': nome,
        'marca': marca,
        'veiculo': veiculo,
        'cor': cor,
        'notaSat': notaSat,
        'anofab': anoFab,
        'idade': idade
    }

def cadastrar_veiculo():
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

def listar_veiculo():
    pass

def editar_veiculo():
    pass

def excluir_veiculo():
    pass

#menu lateral
st.sidebar.title("Menu")
opcao= st.sidebar.radio(
    "Selecione uma opção:",("Cadastrar Veiculo","Listar Veiculo","Editar Veiculo","Excluir Veiculo")
)

#navegação entre páginas
if opcao == "Cadastrar Veiculo":
    cadastrar_veiculo()
elif opcao == "Listar Veiculo":
    listar_veiculo()
elif opcao == "Editar Veiculo":
    editar_veiculo()
elif opcao == "Excluir Veiculo":
    excluir_veiculo()

#Rodapé
st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por Sousa")
st.sidebar.markdown(f"Total de veículos: ")

#para instalar streamlit, comando pip install streamlit
#arquivo com streamlit deve ser executado no próprio terminal, "streamlit run nome do arquivo .py"

