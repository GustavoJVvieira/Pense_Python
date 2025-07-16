# Calculadora de volume

# 1 - utilização sem o modulo math

raio = 5
pi = 3.14159

volume = (4/3)*pi*(raio**3)

print(f"O volume de {raio} é: {volume:.2f}")

# 2 - utilização do modulo math
import math 

raio = 5

volume = (4/3)* math.pi * pow(raio,3)

print(f"O volume de {raio} é: {volume:.2f}")