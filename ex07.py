if __name__ == '__main__':
    n = int(input('Digite um numero para saber a tabuada do "N": '))
    for c in range(1, 10+1):
        print(' {} x {} = {} '.format(n, c, n*c), end='')