# Escreva uma função chamada triangle que receba uma string e um número inteiro, e desenhe um triangulo com a altura especificada, composto de multiplas copias da string



def triangle(string, number):
    for i in range(1, number + 1):
        print(string * i)


triangle('L',5)
