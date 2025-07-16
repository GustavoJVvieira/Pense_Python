"""
Escreva uma função chamada print_right, que receba uma string chamada text como parametro e exiba essa string com espaços suficientes 
a frente para que a ultima letra esteja alinhada na 40 coluna da tela

"""

def print_right(text):
    vazio = 40 - len(text)

    print(" " * vazio + text)

print_right("Ai calica")
print_right("Ai caralho")
