letraProcurada = str(input("Digite o letra a ser procurada (sem acento): ")).upper()
palavrasIdentificadas = []
if not letraProcurada.isalpha():
        print("Por favor, digite uma letra válida.")
else:
    while True:
        linha = input("Digite uma linha de texto (ou pressione Enter para encerrar): ").upper()

        if linha == '':
            break

        palavras = linha.split()

        for palavra in palavras:
            if palavra and (palavra[0] == letraProcurada or palavra[-1] == letraProcurada):
                palavrasIdentificadas += [palavra]

    if palavrasIdentificadas:
        print("Palavras que começam e/ou terminam com '{}':".format(letraProcurada))
        for palavra in palavrasIdentificadas:
            print(palavra)

        print("Quantidade de palavras identificadas: {}".format(len(palavrasIdentificadas)))
    else:
        print("Nenhuma palavra identificada.")