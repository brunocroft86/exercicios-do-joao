#11) Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês,
#mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele
#efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas
#vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do
#vendedor.


salario_fixo = float(input('Qual o seu salário fixo? R$: '))
carros_vendidos = int (input('Quantos carros você vendeu?'))
porcarvend = carros_vendidos + (5*100)
total_vendas = salario_fixo + porcarvend
salario_final = total_vendas
print(f'O salário final foi de R$: {salario_final:.2f}')