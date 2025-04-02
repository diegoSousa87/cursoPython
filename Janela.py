import tkinter #tkinter é uma biblioteca

root= tkinter.Tk() #root é variável, está recebendo objeto do tipo Tk (janela)
root.title("Hello world gráfico")
root.geometry("800x600")

labelFrase= tkinter.Label(root, text= "Olá",
                                font= ("Verdana", 32),
                                fg= "#0000FF",
                                bg= "lightblue")

labelNome= tkinter.Label(root,
                            text="Digite seu nome:",
                            font= ("Arial", 32),
                            fg= "white",
                            bg= "gray")

labelFrase.pack(padx=5, pady=5)

labelNome.pack(padx= 5, pady= 5) #label é comando de saida

entryNome= tkinter.Entry(root, show= "#") #entry é comando de entrada
entryNome.pack(padx= 5, pady= 5)

buttonGravar= tkinter.Button(root, 
                             text= 'Gravar',
                             command= None)
buttonGravar.pack(padx= 5, pady= 5)

root.mainloop()#tem q ser o ultimo comando