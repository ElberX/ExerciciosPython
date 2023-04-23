if __name__ == '__main__':
    nfunc = int(input('Digite o numero de funcionarios: '))
    nhoras = int(input('Horas trabalhadas: '))
    vhora = float(input('Valor por horas trabalhadas: '))
    salario = nhoras*vhora

    print('NUMBER = {}'.format(nfunc))
    print('SALARY = U$ %0.2F'%salario)
