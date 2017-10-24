A=[]
soma=0

for x in range(1,11):
    n=float(input("Informe o " + str(x) +  "º numero: "))
    A.append(n)
    if x % 2 == 0:
        soma=soma+n
print(A)
print(soma)