if __name__ == '__main__':
    n1, n2, n3, n4 = input().split()
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    n4 = float(n4)
    m = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10
    print('Media: %.1f'%m)
    if (m>=7.0):
        print('Aluno aprovado.')
    elif (m<5):
        print('Aluno reprovado.')
    elif (m>=5 and m<7):
        print('Aluno em anexo.')
        n5 = float(input())
        print('Nota do exame: %.1f'%n5)
        nmedia = (m+n5)/2
        if(nmedia>=5.0):
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')
        print('Media final: %.1f'%nmedia)