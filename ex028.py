#Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles

a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))
c = int(input("Digite o terceiro valor:"))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f"O maior número digitado foi {maior}")

