# Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever
#uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o
#aluno é aprovado). Escrever também a média calculada.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 +n2)/2
if media >= 6:
    print(f'Sua primeira note foi {n1}, e a segunda {n2} sendo assim, sua média foi {media} e está APROVADO!')
else:
    print(f'Sua primeira note foi {n1}, e a segunda {n2} sendo assim sua média foi {media} e está REPROVADO!')