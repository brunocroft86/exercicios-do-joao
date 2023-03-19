#Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os
#minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é
#de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.

hora_inico = int(input('Qual o horário do inicio do jogo? '))
hora_fim = int(input('Qual o horário do fim do jogo? '))
duração = (hora_fim - hora_inico )
if duração > 24:
    print('tempo de jogo maior que o permitido!')
else:
    print(f'O tempo do jogo é de {duração} horas.')
