#9) Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste.
#Calcular e escrever o valor do novo salário.

# salarioatual = float(input('Digite o salário atual: '))
# percreajuste = float(input('Digite o reajuste: '))
# novosalario = (salarioatual * percreajuste)/100
# print(f'O novo salário é de R${novosalario + salarioatual:.2f}')

def aumentaSalario(salarioAtual,percReajuste):
    aumento = (salarioAtual * percReajuste) / 100
    novoSalario = aumento + salarioAtual
    return novoSalario
salarioAtual = float(input('Digite o salário atual:R$ '))
percReajuste = float(input('Digite o reajuste:R$ '))
resultado = aumentaSalario(salarioAtual,percReajuste)
print(f'o seu novo salário é de R${resultado:.2f}')









