import easygui as ei

lista=[]

n=int(ei.enterbox("Informe o numero de valores: "))
for x in range(0,n):
    valor=int(ei.enterbox("Informe um valor: "))
    lista.append(valor)

    #Teste

ei.msgbox(lista)