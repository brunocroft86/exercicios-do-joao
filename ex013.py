# Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno.
#Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5. Fórmula para o cálculo da média
#final é:

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
média = (n1 * 2) + (n2 * 3) + (n3 * 5)
print(f'A media final do aluno é {média}')