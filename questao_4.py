numeroDegraus = input("Digite o número de degraus (n > 0): ")
if not numeroDegraus.isnumeric():
    print("Por favor, digite um número inteiro válido.")
else:
    n = int(numeroDegraus)

    if n <= 0:
        print("O número de degraus deve ser maior que 0.")
    else:
        maneiras = [0] * (n + 1)
        maneiras[0] = 1
        maneiras[1] = 1

        i = 2
        while i <= n:
            maneiras[i] = maneiras[i - 1] + maneiras[i - 2]
            i += 1

        print("Número de maneiras diferentes de subir os {} degraus: {}".format(n, maneiras[n]))