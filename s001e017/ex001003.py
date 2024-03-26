# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set()  # vazio
# s2 = set('Taiane')
# s3 = {'Taiane', 1, 2, 3}  # com dados
# print(s1)
# print(s2)
# print(s3)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# print(l1, type(l1))
# s1 = set(l1)
# print(s1, type(s1))
# l2 = list(s1)
# print(l2, type(l2))
# s1 = {1, 2, 3}
# print(s1, type(s1))
# print(3 not in s1)
# print()

# for numero in s1:
#     print(numero)

# Métodos úteis:
# add, update, clear, discard
s1 = set()
print(s1)
s1.add('Taiane')
print(s1)
s1.add(1)
print(s1)
s1.update(('Olá mundo', 1, 2, 3, 4))
print(s1)
s1.discard('Olá mundo')
print(s1)
s1.discard('Taiane')
print(s1)
s1.clear()
print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
