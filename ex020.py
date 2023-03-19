# Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente

v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
if v1 > v2:
    print(f'a forma crescente é {v2} e {v1}: ')
if v2 >v1:
    print(f'A forma crescente é {v1} e  {v2}: ')
if v1 == v2:
    print('valores iguais nao sao lidos.')



