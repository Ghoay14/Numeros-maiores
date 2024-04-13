numeros = []

while True:
    linha = input("Digite um número (ou pressione Enter para encerrar): ")
    if linha == '':
        break
    numero = float(linha)
    numeros = numeros + [numero] 
if numeros:
    ultimoNumero = numeros[-1]
    print("Números maiores que o último número digitado:")
    i = 0
    while i < len(numeros) - 1:
        if numeros[i] > ultimoNumero:
            print(numeros[i])
        i += 1
else:
    print("Nenhum número foi digitado.")
