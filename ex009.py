#9) Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste.
#Calcular e escrever o valor do novo salário.

salarioatual = float(input('Digite o salário atual: '))
percreajuste = float(input('Digite o reajuste: '))
novosalario = (salarioatual * percreajuste)/100
print(f'O novo salário é R${novosalario + salarioatual:.2f}')

