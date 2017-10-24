import easygui as ei
vet=[]
n1=0
n2=0
n3=0
media=0

n1 = float(ei.enterbox(msg="Informe o valor pra a Nota 1: ", title="Media"))
n2 = float(ei.enterbox(msg="Informe o valor pra a Nota 2: ", title="Media"))
n3 = float(ei.enterbox(msg="Informe o valor pra a Nota 3: ", title="Media"))

media=(n1+n2+n3)/3

if media>=6:
    ei.msgbox("Parabens!!")
elif media>=4 and media<6:
    ei.msgbox("Exame")
else:
    ei.msgbox("REPROVADO")
