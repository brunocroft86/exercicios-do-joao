#11) Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês,
#mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele
#efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas
#vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do
#vendedor.


salario_fixo = float(input('Qual o seu salário fixo? R$: '))
valorComissaoFixa = float(input('Qual o valor da comissão fixa por carro? '))
qntCarrosVendidos = int(input('Quantos carros você vendeu? '))
valorCarro = float(input('Quanto custa o carro? '))

porcentagemComissaoExtra = 0.05

valorTotalVendasSemComissao = qntCarrosVendidos*valorCarro
valorTotalComissaoFixa = qntCarrosVendidos * valorComissaoFixa
valorTotalComissaoExtra = valorTotalVendasSemComissao * porcentagemComissaoExtra
valorTotalComissao = valorTotalComissaoFixa + valorTotalComissaoExtra
valorTotalVendasComComissao = valorTotalVendasSemComissao + valorTotalComissao
salarioFinal = valorTotalVendasComComissao + salario_fixo
print(f'Parabéns vc tá fudido e vai receber um salário de R${salarioFinal:.2f}')



