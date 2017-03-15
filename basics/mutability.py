### mutabilité
var = 10
print(id(var))
var = 11
print(id(var))

ch = 'test'
print(ch[0]) # => t
ch[0] = 'c' # => error
print(ch[0])
