#Entrada
while True:
    N1= float (input("Digite a nota 1 Bim: "))
    if N1 <= 10 and N1 >= 0:
        break
while True:
    N2= float (input("Digite a nota 2 Bim: "))
    if N2 <= 10 and N2 >= 0:
        break
while True:
    N3= float (input("Digite a nota 3 Bim: "))
    if N3 <= 10 and N3 >= 0:
        break
while True:
    N4= float (input("Digite a nota 4 Bim: "))
    if N4 <= 10 and N4 >= 0:
        break

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