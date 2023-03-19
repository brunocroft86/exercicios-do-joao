#) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
#compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e
#escreva o custo total da compra.

macas_compradas = float(input('Quantas maças vc comprou? '))
acima = macas_compradas * 1
abaixo = macas_compradas * 1.30

if macas_compradas > 11:
    print(f'Você comprou {macas_compradas:.0f} maças, e custará R${acima:.2f}.')
else:
    print(f'Você comprou {macas_compradas:.0f}maças, e custará R${abaixo:.2f}')
