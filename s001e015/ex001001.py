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

p1 = {
    'nome': 'Taiane',
    'sobrenome': 'Barbosa',
}
print(p1)
print(p1['nome'])
print(p1['sobrenome'])
print(p1.get('nome', 'Não existe'))
print(p1.get('sobrenome', 'Não existe'))
print(p1.get('idade', 'Idade não existe'))
print()

nome = p1.pop('nome')
print(nome)
print(p1)
ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)
p1.update({
    'nome': 'novo valor',
    'idade': 30,
})
print(p1)
p1.update(nome='novo valor 2', idade=40)
print(p1)
print()

tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor 2'], ['idade', 40]]
print(tupla)
print(lista)
print()

p1.update(tupla)
print(p1)
p1.update(lista)
print(p1)
