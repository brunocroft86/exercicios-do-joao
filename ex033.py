#33) Ler dois valores e imprimir uma das três mensagens a seguir:
#‘Números iguais’, caso os números sejam iguais
#‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
#‘Segundo maior’, caso o segundo seja maior que o primeiro.

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input("Digite o segundo valor: "))

if v1 > v2:
    print("primeiro é maior")
if v1 == v2:
        print("numeros iguais! ")
if v1 < v2:
    print("segundo maior! ")

