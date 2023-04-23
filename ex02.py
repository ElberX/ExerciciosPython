if __name__ == '__main__':
    maiorAL = 0
    menorAL = 0
    for a in range (1, 16):
        altura = float(input('Digite a altura da {}ª pessoa: '.format(a)))
        if a == 1:
            maiorAL = altura
            menorAL = altura
        else:
            if altura > maiorAL:
                maiorAL = altura
            if altura < menorAL:
                menorAL = altura
print('A maior altura: {}'.format(maiorAL))
print('A menor altura: {}'.format(menorAL))
