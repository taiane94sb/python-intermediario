# Variáveis livres + nonlocal (locals, globals)
print(globals())
print()


def fora(x):
    a = x

    def dentro():
        print(locals())

        return a
    return dentro


dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print()

print(dentro2())
