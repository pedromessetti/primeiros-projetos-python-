print('***Manipulando Texto***')
frase = 'Curso em Vídeo Python'
print('\nDado a frase {}. Temos que:'.format(frase))
#print(frase[:21]) para escrever a frase inteira ou em partes de acordo com o valor digitado na máscara
print('A frase possui {} caractéres'.format(len(frase)))
print('A contagem de letras ´o´ nesta frase é de {}'.format(frase.count('o')))
print('A palavra ´Vídeo´ se encontra na posição {}'.format(frase.find('Vídeo')))
print('Qual palavra se encontra entre a posição 0 e 4? {}'.format(frase[:5]))
print('A palavra ´Android´ se encontra em qual posição? {}'.format(frase.find('Android')))
print('Possuo a palavra ´Curso´ na frase?', 'Curso' in frase)
print('Substituir a palavra ´Python´ por ´Android´: {}'.format(frase.replace('Python','Android')))
print('Substituir todas as letras por maiúsculas: {}'.format(frase.upper()))
print('Sunstituir todas as letras por minúsculas: {}'.format(frase.lower()))
print('Substituir todos os caracteres por minúsculas exceto o primeiro: {}'.format(frase.capitalize()))
print('Substituir todas as letras iniciais de cada palavra para maíuscula: {}'.format(frase.title()))
print('Para dividir a frase temos a função .split(): {}'.format(frase.split()))
frase = frase.split()
print('Vamos juntar novamente a frase porém agora com - : {}'.format('-'.join(frase)))
frase2 = '   Aprendendo Python   '
print('\nMudando a frase para: {}'.format(frase2))
print('Para remover esses espaços indesejados temos a função .strip(): {}'.format(frase2.strip()))
