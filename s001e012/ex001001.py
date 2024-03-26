# Manipulando chaves e valores em dicionários
pessoa = {}
print(pessoa)
chave = 'nome'
print()

pessoa[chave] = 'Taiane'
pessoa['sobrenome'] = 'Barbosa'
print(pessoa)
print(pessoa[chave])
print(pessoa['nome'])
print(pessoa['sobrenome'])
print()

pessoa[chave] = 'Matheus'
print(pessoa)
print(pessoa[chave])
print(pessoa['nome'])
print(pessoa['sobrenome'])
print()

del pessoa['sobrenome']
print(pessoa)
print(pessoa[chave])
print(pessoa['nome'])
print()

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])
