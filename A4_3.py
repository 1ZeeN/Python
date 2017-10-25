A=[]
cont=0

i=int(input(("Quantos numeros: ")))
for x in range(0,i):
    n=float(input("Informe o " + str(x+1) +  "º numero: "))
    A.append(n)
    if n %2 == 0:
        cont=cont+1
print (cont)
print (A)

