import importlib

import ex001001_m

print(ex001001_m.variavel)

for i in range(10):
    importlib.reload(ex001001_m)
    print(i)

print('Fim')
