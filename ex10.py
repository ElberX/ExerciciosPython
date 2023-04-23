if __name__ == '__main__':
    numero = int(input('Qual o numero que você quer saber o fatorial? '))
    c = numero
    f = 1
    print('{}! = '.format(numero), end='')
    while c > 0:
        print('{}'.format(c), end='')
        print(' x ' if c > 1 else ' = ', end='')
        f *= c
        c -= 1
    print('{}'.format(f))