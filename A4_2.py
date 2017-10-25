A=[]
B=[]
V=0

for x in range(0,2):
    n=float(input("Informe o " + str(x+1) +  "º numero para o 1ºVetor: "))
    A.append(n)
print(A)

for x in range(0,2):
    c=float(input("Informe o " + str(x+1) + "º numero para o 2ºVetor: "))
    B.append(c)
print(B)

for x in range(0,2):
    V=V+(A[x]*B[x])
print(V)
