# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]
print(produtos)
print()

def funcao_do_reduce(acumulador, produto):
    # print('acumulador', acumulador)
    # print('produto', produto)
    # print()
    return acumulador + produto['preco']

total1 = reduce(
    funcao_do_reduce,
    produtos,
    0
)
print('Total (usando função) é', total1)
print()

total2 = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)
print('Total (usando lambda) é', total2)
print()

total = 0
for p in produtos:
    total += p['preco']

print('Total é', total)
print()

print('Total é', sum([p['preco'] for p in produtos]))
