
# complex
x = 1+3j
print(x)
print(type(x))

# typage dynamique
x = 3
print(x)
print(type(x))

x = 'test'
print(x)
print(type(x))

# string
x = 'chaine de caractere'
y = 'chaine sur \
    plusieurs lignes'

z = '''chaine sur plusieurs
   lignes'''

print(y)
print(z)

# conversion

var = str(10)
print(type(var))
my_int = int(var)
print(type(my_int))

my_int = int('test') # => erreur
my_float = int('10.')
