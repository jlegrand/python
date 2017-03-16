fichier = open('test.txt', 'r')  # => open retourne un iterator

# for e in fichier:
#     print(e)

contenu = fichier.read()
print('#' *30)
print(contenu)
print('#' *30)

fichier.close()


### read
with open('test.txt', 'r') as fichier:
    contenu = fichier.read()
    print(fichier.closed)

print('#' *30)
print(contenu)
print('#' *30)
fichier.close()

### readline
with open('test.txt', 'r') as fichier:
    contenu = fichier.readline(5)

print('#' *30)
print(contenu)
print('#' *30)
fichier.close()

### readlines
with open('test.txt', 'r') as fichier:
    contenu = fichier.readlines()

print('#' *30)
print(contenu)
print('#' *30)
fichier.close()

### writelines
with open('test_write.txt', 'w') as fichier:
    contenu = ['write1\n', 'write2\n']
    fichier.writelines(contenu)

### seek
fichier = open('test_write.txt', 'a')
print(fichier.tell())
fichier.seek(0,2)
# seek offset (0 = debut, 1 = courant, 2 = fin
fichier.write('test')




