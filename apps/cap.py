# chaine = '    ceci      EST uNe chaine.   \t  de caracteres    '
#
# print('upper : ', chaine.upper())
# print('lower : ', chaine.lower())
# print('title : ', chaine.title())
# print('capitalize : ', chaine.capitalize())
#
# print('strip : $%s$' %chaine.strip())
# print('lstrip : $%s$' %chaine.lstrip())
# print('rstrip : $%s$' %chaine.rstrip())
#
# print('split(.) : $%s$' %chaine.split('.'))
# print('split : $%s$' %chaine.split())
# print('split( ) : $%s$' %chaine.split(' '))
#
#
# mots = ['mot1', 'mot2', 'mot3']
#
# print('join : ', ':'.join(mots))
# print('rjust : $%s$' %'test'.rjust(3))

text = "  bonjour. je M'appelle Julien." # => voulu  "  Bonjour. Je m'appelle Julien.'


# def cap_phrases(phrases):
#     P = phrases.split('.')
#     R = []
#     for phrase in P:
#         R.append(cap_phrase(phrase))
#     return '.'.join(R)
#
#
# def cap_phrase(phrase):
#     return phrase.strip().capitalize().rjust(len(phrase))

def cap_phrases(phrases):
    if '.' not in phrases:
        return phrases.strip().capitalize().rjust(len(phrases))
    else:
        # en utilisant une liste de compréhension :
        # P = [cap_phrases(e) for e in phrases.split('.')]

        # en utilisant un generateur (optimisation)
        P = (cap_phrases(e) for e in phrases.split('.'))
        return '.'.join(P)


def iscap(phrases):
    return phrases == cap_phrases(phrases)


print(':%s:' %cap_phrases(text))
print(iscap(text))

