A=[]
cont=0

for x in range(1,11):
    n=float(input("Informe o " + str(x) +  "º numero: "))
    A.append(n)
    if n == 2:
        cont=cont+1
print (cont)
