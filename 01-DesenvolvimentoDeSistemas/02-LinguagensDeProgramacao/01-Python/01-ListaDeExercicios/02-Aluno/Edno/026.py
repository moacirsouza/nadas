# Faça um programa que leia uma frase pelo teclado e mostre:
# a) Quantas vezes aparece a letra "A";
# b) Em que posição ela aparece a primeira vez;
# c) Em que posição ela aparece a última vez.

frase = str(input('Qual a frase? Rá, raiiiiê!!!\t'))
frase = frase.upper()

procura = frase.split('A')
# A bruchA de mentirA
print('A letra "A" aparece nessa frase ' + str(len(procura)-1) + ' vezes.')
print('A letra "A" aparece a primeira vez na posição ' + str(frase.find('A')+1))
print('A letra "A" aparece a última vez na posição ' + str(frase.rfind('A')+1))
