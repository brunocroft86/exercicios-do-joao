#7) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade
#dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

anos = int (input ('Digite o valor do anos: '))
dias = int (input ('Digite o valor do dias: '))
meses = int (input ('Digite o valor do meses: '))
total_de_dias=anos*365+meses*30+dias
print ('O valor do total de dias: ' + repr (total_de_dias))

