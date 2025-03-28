#Entrada
tabuada= int(2)
contador= int(1)

while tabuada <= 10:
    print(tabuada, "*" ,contador,"=", tabuada * contador)
    contador= contador+1
    if contador == 11:
        tabuada= tabuada+1
        contador= 1

  