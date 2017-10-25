while True:

    def VerificaSaida():
        c = input('Deseja continuar? s/n')
        if c=="n":
            exit()

    idade = int(input('Informe a idade do nadador: '))

    if idade < 9:
        print('Sua classificacao e Mirim')
        VerificaSaida()

    elif (idade >= 9) and (idade < 14):
        print('Sua classificacao e Infantil')
        VerificaSaida()

    elif (idade >= 14) and (idade < 18):
        print('Sua classificacao e Juvenil')
        VerificaSaida()

    else:
        print('Sua classificacao e Adulto')
        VerificaSaida()
