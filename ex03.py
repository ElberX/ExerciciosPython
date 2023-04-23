if __name__ == '__main__':
    s = 0
    q = 0
    p = 0
    n = 0
    while True:
        v = int(input('Digite um valor: '))
        sair = input('Se deseja encerrar tecle (ENTER)')
        s += v
        q += 1
        if v >= 0:
            p += 1
        else:
            n += 1
        if sair in 'enter':
            break
    media = s / q
    percentuualPositivos = p*100/q
    percentualNegativos = n*100/q
    print('Média: {:.2f}'.format(media))
    print('Positivos: ', p)
    print('Negativos: ', n)
    print('% de positivos:{:.0f} '.format(percentuualPositivos))
    print('% de negativos:{:.0f} '.format(percentualNegativos))