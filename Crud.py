import tkinter as tk #importa ferramentas básicas da biblioteca tkinter
from tkinter import ttk, messagebox, filedialog #importa ferramentas específicas do tkinter
import json

def salvar_para_json():
    if not pets:
        messagebox.showwarning('Aviso', 'Não há pets!')
        return

#Abre a janela para selecionar onde salvar o arquivo
    arquivo= filedialog.asksaveasfilename(
        defaultextension='.json',
        filetypes=[('Arquivos JSON',
                '*.json')],
        title='Salvar lista de pets como json'
    )

    if not arquivo: #se o usuário cancelar
        return

    try:
        with open(arquivo, 'w', encoding= 'utf-8') as f: json.dump(pets, f, ensure_ascii=False, indent=4)

        messagebox.showinfo('Sucesso', f,'Dados salvos com sucesso em: \n{arquivo}')
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao salvar:\n{str(e)}')

def carregar_pets(pets_list=None):
    for item in tree.get_children():
        tree.delete(item)

    pets_to_load= pets_list if pets_list is not None else pets

    for pet in pets_to_load:
        tree.insert("", 'end', values=
                    (pet['id'],
                     pet['tutor'],
                     pet['nome'],
                     pet['espécie'],
                     pet['raça'],
                     pet['idade'],
                     ))
        
def adicionar_pet():
    global next_pet_id
    tutor= entry_tutor.get()
    nome= entry_nome.get()
    especie= entry_especie.get()
    raca= entry_raca.get()
    idade= entry_idade.get()

    if not tutor or not nome:
        messagebox.showerror('Erro', 'Tutor e nome do pet são obrigatórios!')
        return

    try:
        idade_int= int(idade) if idade else 0
    except ValueError:
        messagebox.showerror("Erro", "Idade deve ser um número inteiro!")
        return

    novo_pet= {
    'id': next_pet_id,
    'tutor': tutor,
    'nome': nome,
    'espécie': especie,
    'raça': raca,
    'idade': idade_int
    }

    pets.append(novo_pet)
    next_pet_id += 1

    messagebox.showinfo('Sucesso', 'Pet cadastrado com sucesso!')
    limpar_campos()
    carregar_pets()

def selecionar_pet(event):
    selected_item= tree.selection()
    if not selected_item:
        return
    
    values= tree.item(selected_item) ['values']
    limpar_campos()

    entry_tutor.insert(0, values[1])
    entry_nome.insert(0, values[2])
    entry_especie.insert(0, values[3])
    entry_raca.insert(0, values[4])
    entry_idade.insert(0, str(values[5]))

def limpar_campos():
    entry_tutor.delete(0, 'end')
    entry_nome.delete(0, 'end')
    entry_especie.delete(0, 'end')
    entry_raca.delete(0, 'end')
    entry_idade.delete(0, 'end')

def editar_pet():
    selected_item= tree.selection()
    if not selected_item:
        messagebox.showerror('Erro', 'Selecione um pet para editar!')
        return
    
    pet_id= tree.item(selected_item) ['values'][0]
    tutor= entry_tutor.get()
    nome= entry_nome.get()
    especie= entry_especie.get()
    raca= entry_raca.get()
    idade= entry_idade.get()

    if not tutor or not nome:
        messagebox.showerror('Erro', 'Tutor e nome do pet são obrigatórios!')
        return
    
    try:
        idade_int= int(idade) if idade else 0
    except ValueError:
        messagebox.showerror('Erro', 'Idade deve ser um número inteiro!')
        return
    
    for pet in pets:
        if pet['id'] == pet_id:
            pet.update({
                'tutor': tutor,
                'nome': nome,
                'especie': especie,
                'raca': raca,
                'idade': idade_int
            })
            break
    
    messagebox.showinfo('Sucesso', 'Pet atualizado com sucesso!')
    carregar_pets()

def remover_pet():
    selected_item= tree.selection()
    if not selected_item:
        messagebox.showerror('Erro', 'Selecione um pet para remover!')
        return
    
    pet_id= tree.item(selected_item)['values'] [0]

    if messagebox.askyesno('Confirmação', 'Tem certeza que deseja remover este pet?'):
        global pets
        pets= [pet for pet in pets if pet ['id'] != pet_id]
        messagebox.showinfo('Sucesso', 'Pet removido com sucesso!')
        limpar_campos()
        carregar_pets()

def pesquisar_por_tutor():
    termo_pesquisa= entry_tutor.get().lower() #lower converte o texto digitado para minusculo

    if not termo_pesquisa:
        carregar_pets()
        return
    
    pets_encontrados= [pet for pet in pets
                       if termo_pesquisa in pet['tutor'].lower()]
    
    if not pets_encontrados:
        messagebox.showinfo('Pesquisa', 'Nenhum pet encontrado para este tutor')
        carregar_pets()
    else:
        carregar_pets(pets_encontrados)


# dados em memória
pets= [] #cria um array (lista)
next_pet_id= 1 #contador, cada pet cadastrado recebe um código, 1, 2, 3, ...

# configuração da janela principal
root= tk.Tk() #cria janela
root.title('Sistema de cadastro de pets')
root.geometry('800x500')

# frame do formulário
frame_form= ttk.LabelFrame(root, text= 'Formulário de Pet')
frame_form.pack(padx= 10, pady= 5, fill= 'x') #pack gerencia o layout, inserindo a informação uma abaixo da outra

# campos do formulário
ttk.Label(frame_form, text= 'Tutor:').grid(row= 0, column= 0, padx= 5, pady= 5, sticky= 'e')
entry_tutor= ttk.Entry(frame_form, width= 40)
entry_tutor.grid(row= 0, column= 1, padx= 5, pady= 5)

ttk.Label(frame_form, text= 'Nome:').grid(row= 1, column= 0, padx= 5, pady= 5, sticky= 'e')
entry_nome= ttk.Entry(frame_form, width= 40)
entry_nome.grid(row= 1, column= 1, padx= 5, pady= 5)

ttk.Label(frame_form, text= 'Espécie:').grid(row= 2, column= 0, padx= 5, pady= 5, sticky= 'e')
entry_especie= ttk.Entry(frame_form, width= 40)
entry_especie.grid(row= 2, column= 1, padx= 5, pady= 5)

ttk.Label(frame_form, text= 'Raça:').grid(row= 3, column= 0, padx= 5, pady= 5, sticky= 'e')
entry_raca= ttk.Entry(frame_form, width= 40)
entry_raca.grid(row= 3, column= 1, padx= 5, pady= 5)

ttk.Label(frame_form, text= 'Idade:').grid(row= 4, column= 0, padx= 5, pady= 5, sticky= 'e') #sticky alinha o quadro na tela, conforme ela aumenta ou diminui
entry_idade= ttk.Entry(frame_form, width= 40)
entry_idade.grid(row= 4, column= 1, padx= 5, pady= 5)

# frame de botões
frame_botoes= ttk.Frame(root)
frame_botoes.pack(pady= 5)

btn_adicionar= ttk.Button(frame_botoes, text= 'Adicionar', command= adicionar_pet)
btn_adicionar.grid(row= 0, column= 0, padx= 5)

btn_editar= ttk.Button(frame_botoes, text= 'Editar', command= editar_pet)
btn_editar.grid(row= 0, column= 1, padx= 5)

btn_remover= ttk.Button(frame_botoes, text= 'Remover', command= remover_pet)
btn_remover.grid(row= 0, column= 2, padx= 5)

btn_limpar= ttk.Button(frame_botoes, text= 'Limpar', command= limpar_campos)
btn_limpar.grid(row= 0, column= 3, padx= 5)

btn_pesquisar= ttk.Button(frame_botoes, text= 'Pesquisar Tutor', command= pesquisar_por_tutor)
btn_pesquisar.grid(row= 0, column= 4, padx= 5)

btn_salvar_json= ttk.Button(frame_botoes, text= 'Salvar Json', command= salvar_para_json)
btn_salvar_json.grid(row= 0, column= 5, padx= 5)

# frame tabela de pets
frame_tabela= ttk.Frame(root)
frame_tabela.pack(padx= 10, pady= 5, fill= 'both', expand= True)

tree= ttk.Treeview(frame_tabela, columns=('ID', 'Tutor', 'Nome', 'Espécie', 'Raça', 'Idade'), show='headings')
tree.heading('ID', text='ID') #criação de cabeçalho
tree.heading('Tutor', text='Tutor')
tree.heading('Nome', text='Nome')
tree.heading('Espécie', text='Espécie')
tree.heading('Raça', text='Raça')
tree.heading('Idade', text='Idade')

tree.column('ID', width= 50) #largura na horizontal
tree.column('Tutor', width= 150)
tree.column('Nome', width= 100)
tree.column('Espécie', width= 100)
tree.column('Raça', width= 100)
tree.column('Idade', width= 50)

scrollbar= ttk.Scrollbar(frame_tabela, orient= 'vertical', command=tree.yview) #cria barra de rolagem lateral
tree.configure(yscrollcommand= scrollbar.set)

tree.pack(side= 'left', fill= 'both', expand= True)
scrollbar.pack(side= 'right', fill= 'y')

tree.bind('<<TreeviewSelect>>', selecionar_pet) #bind monitora eventos no tree - TreeviewSelect deixa faixa azul sobre o item selecionado e dispara o evento

root.mainloop() #deve ser o ultimo comando

