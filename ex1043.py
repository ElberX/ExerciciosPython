if __name__ == '__main__':
    a,b,c = map(float, input().split())
    p = a+b+c
    area = (a+b)*c/2
    if (a<(b+c)) and (b<(a+c)) and (c<(a+b)):
        print('Perimetro = %.1f'%p)
    else:
        print('Area = %.1f'%area)