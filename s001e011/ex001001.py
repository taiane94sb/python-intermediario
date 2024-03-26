# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }

# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])
print(pessoa['idade'])
print(pessoa['altura'])
print(pessoa['endereços'])
print(pessoa['endereços'][0])
print(pessoa['endereços'][0]['rua'])
print(pessoa['endereços'][0]['número'])
print(pessoa['endereços'][1])
print(pessoa['endereços'][1]['rua'])
print(pessoa['endereços'][1]['número'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])
print('....')

for chave, valor in pessoa.items():
    print(chave, valor)
print('....')
