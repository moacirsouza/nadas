print('[-- Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO". --]\n')

nomedacidade = input('Digite o nome da cidade: ').strip()
print(nomedacidade[0:5].upper() == 'SANTO')

