import tkinter as tk #chama a biblioteca tkinter com apelido de tk

def fnAdicao(): #def cria função
    n1= float(entryNumero1.get())
    n2= float(entryNumero2.get())
    resultado= n1+n2
    lblResultado.config(text=f'A soma é {resultado}') #config altera o texto que tinha sido criado inicialmente (0.00)

def fnSubtracao(): #def cria função
    n1= float(entryNumero1.get())
    n2= float(entryNumero2.get())
    resultado= n1-n2
    lblResultado.config(text=f'A subtração é {resultado}')

def fnDivisao(): #def cria função
    n1= float(entryNumero1.get())
    n2= float(entryNumero2.get())
    resultado= n1/n2
    lblResultado.config(text=f'A divisão é {resultado}')

def fnMultiplicacao(): #def cria função
    n1= float(entryNumero1.get())
    n2= float(entryNumero2.get())
    resultado= n1*n2
    lblResultado.config(text=f'A multiplicação é {resultado}')

janela= tk.Tk() #desenha uma janela
janela.title("WinCalc - A super calculadora") #comando title altera o titulo da janela
janela.geometry('800x600') #tamanho da janela

lblTitulo= tk.Label(janela,
                    text='Calculadora',
                    font= ('Old English Text MT', 50),
                    fg= 'White',
                    bg= 'Blue',
                    width= 800) #estende a faixa onde está escrito calculadora
lblTitulo.pack(padx= 5, pady= 5) #pack deixa os textos um embaixo do outro

lblNumero1= tk.Label(janela,
                     text= 'Digite um número',
                     font= ('Calibri', 22))
lblNumero1.pack(padx=5, pady= 5)

entryNumero1= tk.Entry(janela,
                       #width= 100,
                       font= ('Calibri', 22))
entryNumero1.pack(padx= 5, pady= 5)

lblNumero2= tk.Label(janela,
                     text= 'Digite outro número',
                     font= ('Calibri', 22))
lblNumero2.pack(padx=5, pady= 5)

entryNumero2= tk.Entry(janela,
                       #width= 100,
                       font= ('Calibri', 22))
entryNumero2.pack(padx= 5, pady= 5)

btnAdicao= tk.Button(janela,
                     text= "Adição",
                     font= ('Calibri', 22),
                     width= 12,
                     command= fnAdicao, #fn é abreviação de função
                     fg= 'white',
                     bg= 'grey')
btnAdicao.pack(padx= 5, pady= 5)

btnSubtracao= tk.Button(janela, #btn é abreviação de button
                     text= "Subtração",
                     font= ('Calibri', 22),
                     width= 12,
                     command= fnSubtracao,
                     fg= 'white',
                     bg= 'grey')
btnSubtracao.pack(padx= 5, pady= 5)

btnDivisao= tk.Button(janela,
                     text= "Divisão",
                     font= ('Calibri', 22),
                     width= 12,
                     command= fnDivisao,
                     fg= 'white',
                     bg= 'grey')
btnDivisao.pack(padx= 5, pady= 5)

btnMultiplicacao= tk.Button(janela,
                     text= "Multiplicação",
                     font= ('Calibri', 22),
                     width= 12,
                     command= fnMultiplicacao,
                     fg= 'white',
                     bg= 'grey')
btnMultiplicacao.pack(padx= 5, pady= 5)

lblResultado= tk.Label(janela,
                       text=('0.00'),
                       font= ('Calibri', 22))
lblResultado.pack(padx= 5, pady= 5)

janela.mainloop() #mantem o programa rodando, deve ser o último comando