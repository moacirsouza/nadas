print('[-- Faça um programa que leia uma frase pelo teclado e mostre: a) Quantas vezes aparece a letra "A"; b) Em que posição ela aparece a primeira vez; c) Em que posição ela aparece a última vez. --]\n')
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira vez que a letra A aparece é na posição {}'.format(frase.find('A')))
print('A última vez em que a letra A aparece é na posição {}'.format(frase.rfind('A')))

