L = (5,9,23,4,6,7,2,6,8,74,9)

###
M=[]
for e in L:
    if e%3 == 0:
        M.append(e**2)

print(M)

###
N = [e**2 for e in L if e%3==0]
print(N)

###
def f(x):
    return x**2

def cdt(x):
    return (x%3 == 0)

Q = [f(e) for e in L if cdt(e)]
print(Q)

###
O = [e**2 if e % 3 == 0 else e**3 for e in L]
print(O)

###
fichiers = ['1.py', '2.pdf', 'pdf.txt', '4.xpdf']
P = [x for x in fichiers if x[-4:] == '.pdf' ]
print(P)
