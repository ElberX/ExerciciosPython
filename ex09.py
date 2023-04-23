if __name__ == '__main__':
    a = int(input('Digite o valor inicial:'))
    r = int(input('Digite a razão '))
    pa = a
    for c in range(10):
        print('{} -> '.format(pa), end='')
        pa *= r
    print('ACABOU')