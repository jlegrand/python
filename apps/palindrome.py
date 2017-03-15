mot = input('mot palindrome à tester : ')

def palindrome(chaine):
    return chaine[::-1] == chaine

print(palindrome(mot))
