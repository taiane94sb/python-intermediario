# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)
print()

pessoa = {
    'nome': 'Taiane',
    'sobrenome': 'Barbosa',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)
print()

for chave, valor in pessoa.items():
    print(chave, valor)
print('...')

for chave, valor in dados_pessoa.items():
    print(chave, valor)
print('...')

pessoas_completa = {**pessoa, **dados_pessoa}
print(pessoas_completa)
