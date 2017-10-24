import easygui as ei
import pylab as py

A=[]
aux=[]
b=[]


msg= 'Informe o numero de linnhas e colunas da matriz'
title= 'Sistema Linear'
op= ('Linhas','Colunas')
coef= ei.multenterbox(msg,title,op)
if (coef[0]!=coef[1]):
    ei.msgbox('A Matriz nao e quadrada! Informe valores iguais para Linha e Coluna')
else:
    for i in range(1,int(coef[0])+1):
        mat = []
        for j in range(1,int(coef[1])+1):
            mat.append(['a'+ str(i) + str(j)])

        msg = 'Informe o valor para o termo:'
        c =ei.multenterbox(msg, title, mat)
        aux.append(c)

print(aux)

A = py.array(A)
print (A)


