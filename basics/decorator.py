def decorator(f):
    print('debut decorateur')

    def f_out(arg):
        print('pre traitement')
        out = f(arg)
        print('post traitement')
        return out
    print('fin decorateur')
    return f_out


@decorator
def ma_fonction(arg):
    return('la fonction', arg)


print(ma_fonction(ma_fonction.__name__))
