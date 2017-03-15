class Paragraphe(str):


    # def split(self, *args):
    #     liste = list(self)
    #     sep = []
    #     phrases = []
    #     for e in liste:
    #         if e in args:
    #             sep.append((e, liste.index(e)))
    #             liste = liste[liste.index(e)+1:]
    #             phrases.append(''.join(liste[:liste.index(e)+1]))
    #     return phrases, sep

    def cap(self):
        if '.' not in self:
            return Paragraphe(self.strip().capitalize().rjust(len(self)))
        else:
            P = (Paragraphe.cap(e) for e in self.split('.'))
            return Paragraphe('.'.join(P))

    def iscap(self):
        return self == self.cap()

    def __add__(self, other):
        return str.__add__(self, other.cap())

text1 = Paragraphe('je sUis un texte. je suis unE phrase.')
text2 = Paragraphe('je suis Le TEXTE 2.')
print(text1)
print(text1.cap())
print(text1.iscap())
print(text1.cap().iscap())
print(text1 + text2)

# connaitre l'heritage
print(type.mro(Paragraphe))

