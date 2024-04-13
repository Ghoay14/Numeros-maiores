resp = 'S'
quant= maior = menor = soma = 0
while resp == 'S':
    numeroInteiro = int(input('Digite um número:'))
    resp = input('Deseja continuar?(S/N) ') .upper()
    quant += 1
    soma += numeroInteiro
    if quant == 1:
        maior = numeroInteiro
        menor = numeroInteiro
    else:
        if numeroInteiro > maior:
            maior = numeroInteiro
        if numeroInteiro < menor:
            menor = numeroInteiro
print('A média entre os {} número(s) é: {:.2f} '.format(quant, soma/quant))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))


