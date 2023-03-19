#Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles

v1 = int(input('Digite o primeo valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))

if v1 > v2 and v3:
    print(f'o maior valor digitado foi {v1}.' )
elif v2 > v1 and v3:
    print(f'o maior valor digitado foi {v2}.' )
else:
    print(f'o maior valor digitado foi {v3}.' )
if  v1 == v2 and v3:
    print('valore iguais nao sao considerados.')


