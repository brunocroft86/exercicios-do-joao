#Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela
#poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu)
from _datetime import datetime

ano_atual = 2023
nas = int(input('Qual seu ano de nascimento? '))
idade = (ano_atual - nas)

if idade >= 16:
    print(f'Você tem {idade} e poderá votar')
else:
    print(f'Você tem {idade} e não poderá votar')
