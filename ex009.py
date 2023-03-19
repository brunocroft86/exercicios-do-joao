#9) Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste.
#Calcular e escrever o valor do novo salário.

salario_atual = float(input('Digite seu salário atual: R$:'))
aumento =float (input('Quanto por cento foi o aumento? '))
novo = salario_atual +(salario_atual * aumento/ 100)
print(f'Com o aumento de {aumento:.0f}%,o seu salário passara de R$:{salario_atual:.2f}, para R$:{novo:.2f}.')

