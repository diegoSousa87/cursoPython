#Entrada
def PedirNota(frase): #função para verificar as notas, evitando varios while
    while True:
        nota= float (input(frase))
        if nota >=0 and nota <=10:
            break
    return nota

N1= PedirNota ("Digite a nota 1 Bim: ") #esse laço se repete caso o usuario digite valor maior que 10 e menor que 0
N2= PedirNota ("Digite a nota 2 Bim: ")
N3= PedirNota ("Digite a nota 3 Bim: ")
N4= PedirNota ("Digite a nota 4 Bim: ")


#Processamento
media= (N1+N2+N3+N4) / 4
if (media >= 5):
    print("Aprovado") #python exige 4 espaços para o bloco fazer parte do if
elif(media >=3):
    print("Recuperação")
else:
    print("Reprovado")

#Saída
print(f"Sua média é {media: ,.2f}") # estrutura f string: o primeiro f avisa que dentro das chaves estará uma variável, 2f= 2 casas decimais do tipo float, "," troca . por ,