#32) Ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome
#do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

time01 = str(input('primeiro time: '))
time02 = str(input("segundo time: "))
gt01 = int(input(f"O {time01} marcou quantos gols? "))
gt02 = int(input(f"O {time02} marcou quantos gols? "))


if gt01 > gt02:
    print(f"O vencedor foi o time do {time01}.")
if gt02 > gt01:
    print(f"O vencedor foi o time do {time02}.")
else:
    print('A partida terminou em EMPATE')
