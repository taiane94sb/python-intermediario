"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y

def soma(*args):
    print(args, type(args))
    total = 0
    for numero in args:
        total += numero
    return total


soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)
print()

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)
print()

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(numeros)
print(*numeros)
print()

outra_soma = soma(*numeros)
print(outra_soma)
print()

print(sum(numeros))
print(*numeros)
