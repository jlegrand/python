def decorator(f):
    # print('debut decorateur')

    def f_out(arg):
        print('pre traitement')
        out = f(arg)
        print('post traitement')
        return out
    # print('fin decorateur')
    return f_out


@decorator
def ma_fonction(arg):
    return('la fonction', arg)


# print(ma_fonction(ma_fonction.__name__))


####
def convert(f):
    def f_convert(x, y):
        return f(int(x), int(y))
    return f_convert

@convert
def somme(x, y):
    return x+y

@convert
def produit(x, y):
    return x*y

print(somme(1.2, 3.2))  # => doit retourner 4
print(produit(1.2, 3.2))  # => doit retourner 3

###
