if __name__ == '__main__':
    n = 1
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    while n > 0:
        n = int(input("Digite um número: "))
    if n >= 0 and n <= 25:
        c1 = c1 + 1
    elif n >= 26 and n <= 50:
        c2 = c2 + 1
    elif n >= 51 and n <= 75:
         c3 = c3 + 1
    elif n >= 76 and n <= 100:
        c4 = c4 + 1
print('A quantidade de números entre 0-25 é: {}, entre 26-50 é: {}, '
      'entre 51-75 é: {},e entre 76-100 é {}'.format(c1, c2, c3, c4))