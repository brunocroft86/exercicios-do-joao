#) Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))

if v1 > v2:
    print(v1)
if v1 == v2:
        print('Valores iguais nao são aceitos, tente novamente!')
if v1 < v2:
    print(v2)
