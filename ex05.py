if __name__ == '__main__':
    n = 999
    soma = 0
    somapares = 0
    pares = 0
    impares = 0
    while n > 0:
        n = int(input('Digite um valor: '))
        if n < 0:
            n = int(input('Digite um valor positivo: '))
        soma += n
        if n > 0:
            if n % 2 == 0:
                pares += 1
                somapares += n
            else:
                impares += 1
    mediapares = somapares / pares
    mediageral = soma / (pares + impares)
    if n == 0:
        print('Programa encerrado!')

    print('Quantidade de números pares: ', pares)
    print('Quantidade de números ímpares: ', impares)
    print('A média de valores pares: ', mediapares)
    print('A média geral de valores: ', mediageral)