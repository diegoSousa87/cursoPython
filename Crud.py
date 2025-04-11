import tkinter as tk #importa ferramentas básicas da biblioteca tkinter
from tkinter import ttk, messagebox #importa ferramentas específicas do tkinter

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
entry_tutor= ttk.Entry(frame_form, width= 40)
entry_tutor.grid(row= 1, column= 1, padx= 5, pady= 5)

ttk.Label(frame_form, text= 'Espécie:').grid(row= 2, column= 0, padx= 5, pady= 5, sticky= 'e')
entry_tutor= ttk.Entry(frame_form, width= 40)
entry_tutor.grid(row= 2, column= 1, padx= 5, pady= 5)

ttk.Label(frame_form, text= 'Raça:').grid(row= 3, column= 0, padx= 5, pady= 5, sticky= 'e')
entry_tutor= ttk.Entry(frame_form, width= 40)
entry_tutor.grid(row= 3, column= 1, padx= 5, pady= 5)

ttk.Label(frame_form, text= 'Idade:').grid(row= 4, column= 0, padx= 5, pady= 5, sticky= 'e') #sticky alinha o quadro na tela, conforme ela aumenta ou diminui
entry_tutor= ttk.Entry(frame_form, width= 40)
entry_tutor.grid(row= 4, column= 1, padx= 5, pady= 5)

# frame de botões
frame_botoes= ttk.Frame(root)
frame_botoes.pack(pady= 5)

btn_adicionar= ttk.Button(frame_botoes, text= 'Adicionar', command= None)
btn_adicionar.grid(row= 0, column= 0, padx= 5)

btn_editar= ttk.Button(frame_botoes, text= 'Editar', command= None)
btn_editar.grid(row= 0, column= 1, padx= 5)

btn_remover= ttk.Button(frame_botoes, text= 'Remover', command= None)
btn_remover.grid(row= 0, column= 2, padx= 5)

btn_limpar= ttk.Button(frame_botoes, text= 'Limpar', command= None)
btn_limpar.grid(row= 0, column= 3, padx= 5)

# frame tabela de pets
frame_tabela= ttk.Frame(root)
frame_tabela.pack(padx= 10, pady= 5, fill= 'both', expand= True)

tree= ttk.Treeview(frame_tabela, columns=('ID', 'Tutor', 'Nome', 'Espécie', 'Raça', 'Idade'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Tutor', text='Tutor')
tree.heading('Nome', text='Nome')
tree.heading('Espécie', text='Espécie')
tree.heading('Raça', text='Raça')
tree.heading('Idade', text='Idade')




root.mainloop() #deve ser o ultimo comando

