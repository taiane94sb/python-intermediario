# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = copy.deepcopy(d1)  # alterando um altera, não altera o outro
print(d1)
print(d2)
print()

d2['c1'] = 1000  # não altera o 'c1' do d1
d2['l1'][1] = 999999  # não altera o 'l1'1 do d1
print(d1)
print(d2)
print()
