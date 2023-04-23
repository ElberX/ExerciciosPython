if __name__ == '__main__':
    nome = input('Digite seu nome: ')
    salario = float(input('Digite seu salário: '))
    vendas = float(input('Digite suas vendas no mês: '))
    comissao = 0.15 * vendas
    salariof = comissao + salario
    print('TOTAL = R$ %.2F'%salariof)

