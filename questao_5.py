entrada = input("Digite a sequência de números inteiros separados por espaço: ")
sequencia = [int(num) for num in entrada.split()]

repetidos = []
ocorrencias = {}

for num in sequencia:
    if num in ocorrencias:
        ocorrencias[num] += 1
        if ocorrencias[num] == 2:
            repetidos += [num]
    else:
        ocorrencias[num] = 1

print("Elementos repetidos:", repetidos)

sequencia_invertida = sequencia[::-1]
print("Sequência invertida:", sequencia_invertida)

quantidade_inversoes = 0
inversoes = []

for i in range(len(sequencia)):
    for j in range(i + 1, len(sequencia)):
        if sequencia[i] > sequencia[j]:
            quantidade_inversoes += 1
            inversoes += [(sequencia[i], sequencia[j])]

print("Inversões:", inversoes)
print("Quantidade de inversões:", quantidade_inversoes)
