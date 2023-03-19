#8) Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos
#brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total
#de eleitores

eleitores = float(input('Qual foi o total de eleitores? '))
brancos = float(input('Total de votos em branco? '))
nulos = float(input('Total votos nulos? '))
invalidos = float(input('Total de votos inválidos?'))

pbranco = brancos * 100 / eleitores
pnulos = nulos * 100 / eleitores
pinvalidos = invalidos -(brancos + nulos)
print(f'\nO total de eleitores do municipio é {eleitores}%'
      f'\no total de votos em branco é {pbranco}%'
      f'\no tatal de votos nulos é {pnulos}%'
      f'\no total de votos inválidos é {pinvalidos}%')
