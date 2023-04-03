#8) Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos
#brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total
#de eleitores



total_eleitores = float(input('Total de eleitores da cidade? '))
total_votos_brancos = float(input('Total de fotos em brancos? '))
total_votos_nulos = float(input('Total de fotos nulos? '))
total_votos_validos = float(input('Total de votos válidos? '))
brancos = (100*total_votos_brancos)/total_eleitores
nulos = (100*total_votos_nulos)/total_eleitores
validos = (100*total_votos_validos)/total_eleitores

print(f'Porcentagem de votos brancos é de: {brancos:.2f}%')

print(f'Porcentagem de votos nulos é de: {nulos:.2f}%')

print(f'Porcentagem de votos validos é de: {validos:.2f}%')




