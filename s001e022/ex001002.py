# Empacotamento e desempacotamento de dicionários
# a, b = 1, 2
# print(a, b)
# a, b = b, a
# print(a, b)
# print()

pessoa = {
    'nome': 'Taiane',
    'sobrenome': 'Barbosa',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)
# print()

# for chave, valor in pessoa.items():
#     print(chave, valor)
# print('...')

# for chave, valor in dados_pessoa.items():
#     print(chave, valor)
# print('...')

pessoas_completa = {**pessoa, **dados_pessoa}
print(pessoas_completa)
print()


# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


mostro_argumentos_nomeados(1, 2, 3, 4)
print()

mostro_argumentos_nomeados(nome='Joana', qlq=123)
print()

mostro_argumentos_nomeados(**pessoas_completa)
print()

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)
