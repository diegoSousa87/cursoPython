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

def criar_veiculo(nome, marca, veiculo, placa, notaSat, anoFab, idade):
    return{
        'nome': nome,
        'marca': marca,
        'veiculo': veiculo,
        'placa': placa,
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
    placa= st.text_input('Digite a placa:')
    notaSat = st.selectbox("Nota de satisfação com o veiculo:", list(range(11)), index=10)#index deixa pré selecionado o numero 10
    anoFab= st.number_input('Ano de Fabricação', value=ano_atual, min_value= data_minima, max_value= data_maxima)
    idade= ano_atual - anoFab

    st.write(f'Olá {nome}')
    st.write(f'O veículo {veiculo} da marca {marca} possui {idade} ano de uso')

    #bio= st.text_area('Descreva características do veículo') #cria um editor de texto para digitação

    submit_button = st.button("Cadastrar Veiculo")
    
    if submit_button:
        if not placa:
            st.error("Placa é campo obrigatório!")
            return
        
        dados = carregar_dados()
        
        if placa in dados:
            st.error("Veiculo com essa placa já cadastrado!")
            return
        
        veiculo = criar_veiculo(
            nome= nome,
            marca= marca,
            veiculo= veiculo,
            placa=placa,
            notaSat= notaSat,
            anoFab= anoFab,
            idade= idade
        )
        
        dados[placa] = veiculo
        salvar_dados(dados)
        
        st.success("Veiculo cadastrado com sucesso")
        st.balloons()


def listar_veiculo():
    #pass - comando pass 'pula' função
    st.subheader("Lista de Veículos Cadastrados")
    
    dados = carregar_dados()
    
    if not dados:
        st.info("Nenhum veículo cadastrado ainda.")
        return
    
    # Filtro por veiculo
    filtro_marca = st.text_input("Filtrar por marca:")
    
    veiculos_filtrados = []
    for veiculo, marca in dados.items():
        if filtro_marca.lower() in veiculo["marca"].lower():
            veiculos_filtrados.append((veiculo, marca))
    
    if not veiculos_filtrados:
        st.warning("Nenhum veiculo encontrado com o filtro aplicado.")
        return
    
    for veiculo, marca in veiculos_filtrados:
        with st.expander(f"{veiculo['veiculo']} - Marca: {marca}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Ano de fabricação:** {veiculo['anoFab']}")
                st.write(f"**Idade:** {veiculo['idade']}")
                st.write(f"**Placa:** {veiculo['placa']}")
            
            with col2:
                st.write(f"**Nome:** {veiculo['nome']}")
                st.write(f"**Nota Satisfação:** {veiculo['nota satisfação']}")
            
            if veiculo["historico_veicular"]:
                st.write("**Histórico veicular:**")
                for item in veiculo["historico_veicular"]:
                    st.write(f"- {item}")

def editar_veiculo():
    st.subheader("Editar Veiculo")
    
    dados = carregar_dados()
    
    if not dados:
        st.info("Nenhum veiculo cadastrado para editar.")
        return
    
    placa_selecionada = st.selectbox(
        "Selecione o veiculo pela placa",
        options=list(dados.keys()),
        format_func=lambda x: f"{dados[x]['nome']} - {x}"
    )
    
    veiculo = dados[placa_selecionada]
    
    with st.form(key="form_edicao"):
        col1, col2 = st.columns(2)
        
        with col1:
            nova_placa = st.text_input("PLACA", value=veiculo["placa"], max_chars=11)
            novo_veiculo = st.text_input("Veiculo", value=veiculo["veiculo"])
            ano_fabricacao = st.text_input("Ano de fabricação", value=veiculo["ano_fabricacao"])
        
        with col2:
            Nota_satisfacao = st.text_input("Nota de satisfação", value=veiculo["nota de satisfacao"])
        
        submit_button = st.form_submit_button("Atualizar Veiculo")
    
    if submit_button:
        if not nova_placa:
            st.error("Nova placa é obrigatória!")
            return
        
        # Se a placa foi alterada, precisamos verificar se a nova placa já existe (e não é o mesmo veiculo)
        if nova_placa != placa_selecionada and nova_placa in dados:
            st.error("Já existe um veiculo com esta nova placa!")
            return
        
        # Remove o veiculo antigo se a placa foi alterada
        if nova_placa != placa_selecionada:
            dados.pop(placa_selecionada)
        
        # Atualiza os dados do paciente
        veiculo_atualizado = {

            "veiculo": novo_veiculo,
            "placa": nova_placa,
            "notaSat": Nota_satisfacao,
            "anofab": ano_fabricacao
            #"data_atualizacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        
        dados[nova_placa] = veiculo_atualizado
        salvar_dados(dados)
        
        st.success("Veiculo atualizado com sucesso!")

def excluir_veiculo():
    st.subheader("Excluir Veiculo")
    
    dados = carregar_dados()
    
    if not dados:
        st.info("Nenhum veiculo cadastrado para excluir.")
        return
    
    placa_selecionada = st.selectbox(
        "Selecione o veiculo pela placa para excluir",
        options=list(dados.keys()),
        format_func=lambda x: f"{dados[x]['veiculo']} - {x}"
    )
    
    veiculo = dados[placa_selecionada]
    
    st.warning("Você está prestes a excluir o seguinte veiculo:")
    st.json(veiculo)
    
    if st.button("Confirmar Exclusão"):
        dados.pop(placa_selecionada)
        salvar_dados(dados)
        st.success("Veiculo excluído com sucesso!")

# Menu lateral
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

