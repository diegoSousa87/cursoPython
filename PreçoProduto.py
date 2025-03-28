#Entrada
def PedirPreço(frase): #função para verificar as notas, evitando varios while. Obs: (frase)= nome da variavel
    while True:
        preço= float (input(frase))
        if preço > 0:
            break
    return preço #funçao retorna o valor de nota para dentro da variavel que chamou PedirNota, N1, N2, ...

P1= PedirPreço ("Digite o preço 1: ")
P2= PedirPreço ("Digite o preço 2: ")
P3= PedirPreço ("Digite o preço 3: ")


#Processamento
mediaPreço= (P1+P2+P3) / 3

#Saída
print(f"O preço médio é {mediaPreço: ,.2f}") # estrutura f string: o primeiro f avisa que dentro das chaves estará uma variável, 2f= 2 casas decimais do tipo float, "," troca . por ,