# (01-Gabarito/024.py)) Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".


cidade = str(input('Digite o nome da sua cidade, forasteiro. '))
print('')

if cidade.upper().startswith('SANTO'):
    print('Sua cidade começa com a palavra Santo!')
print('')
print('Obrigado. Pode Passar')
