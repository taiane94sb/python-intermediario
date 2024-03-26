from sys import path

import s001e042_package.modulo

import s001e042_package.modulo
from s001e042_package import modulo
from s001e042_package.modulo import *

# from s001e042_package.modulo import soma_do_modulo, variavel, nova_variavel

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(s001e042_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)
