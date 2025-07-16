# Escreva uma função chamada rectangle que receba uma string e dois número inteiro, e desenhe um retangulo com a largura e altura especificada, composto de multiplas copias da string

def rectangle (string,x,y):
    for _ in range(1, x + 1):
        print(string * y)

rectangle('H',5,4)