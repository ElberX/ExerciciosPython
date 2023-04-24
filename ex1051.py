if __name__ == '__main__':
    s = float(input())
    if (s>0) and (s<=2000):
        print('Isento')
    elif (s>2000) and (s<=3000):
        c = (s - 2000.0) * 0.08
        print('R$ %.2f'%c)
    elif (s>3000) and (s<=4500):
        c = (s - 3000.0) * 0.18 + (1000*0.08)
        print('R$ %.2f'%c)
    elif (s>4500):
        c = (s - 4500) * 0.28 + (1500 * 0.18) + (1000*0.08)
        print('R$ %.2f'%c)
