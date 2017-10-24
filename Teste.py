import easygui as ei
import pylab as py

A=[]
b=[]

msg= 'Informe o numero de linnhas e colunas da matriz'
title= 'Sistema Linear'
op= ('Linhas','Colunas')
coef= ei.multenterbox(msg,title,op)
if (coef[0]!=coef[1]):
    ei.msgbox('A Matriz nao e quadrada! Informe valores iguais para Linha e Coluna')
elif
    for i in range(coef[0]):
        for j in range(coef[1]):
            c =ei.enterbox(msg='Informe o valor para o termo A' + str(i) + str(j), title)
            aux=[]
            aux.append(c)
            aux = py.array(aux)
            A.append(aux)
            print (A)


