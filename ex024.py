#Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que
#ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que
#ultrapassar este valor, calcular e escrever o seu salário total.

salarario = float(input('Digite o seu salário: R$'))
vendas = float(input('Total de vendas: R$'))
if vendas >= 1500:
    a = vendas*0.05
    b = salarario + a
    print(f'salário total R${b}')
if vendas <= 1499:
    a = vendas*0.03
    b = salarario = a
    print(f'salario total R${b}')

