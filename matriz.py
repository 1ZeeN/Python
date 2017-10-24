mat=[]
matT=[]

n=int(input(("Informe a Ordem da matriz: ")))
for i in range(n):
    aux=[]
    for j in range(n):
        a=float(input("Informe um valor de valor para a" + str(i+1)+str(j+1)+": "))
        aux.append(a)
    mat.append(aux)

for j in range(n):
    aux=[]
    for i in range(n):
        aux.append(mat[i][j])
    matT.append(aux)

# print(mat)
# print(matT)

msg= "A matriz eh: \n"
for i in range(n):
    for j in range(n):
        msg+= str((mat[i][j])) + " "
    msg+= "\n"


msg1= "A matriz Transposta eh: \n"
for i in range(n):
    for j in range(n):
        msg1+= str((matT[i][j])) + " "
    msg1+= "\n"

print (msg)
print (msg1)


