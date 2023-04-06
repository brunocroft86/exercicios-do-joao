#Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e
#quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade
#média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual
#a quantidade média escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar
#compra'.

quant_atual = int(input('Informe a quantidade atual: '))
quant_maxima = int(input('Iinforme a quantidade máxima: '))
quant_minima = int(input('Informe a quantidade minima: '))
quant_media = (quant_maxima + quant_minima)/2
if quant_media >= quant_atual:
    print(f'Quantidade média = {quant_media:.0f}  Não efetuar compra! ')
else:
    print(f'quantidade média = {quant_media:.0f}, efetuar compra!')