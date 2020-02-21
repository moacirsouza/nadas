print('[-- Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO". --]\n')
cidade = input('Digite o nome da cidade (Maiúsculas e Minúsculas não serão diferenciadas): ')
buscaPeloSanto = cidade.lower().strip().startswith('santo')
print('\nA cidade começa com a palavra SANTO? -> {}\n'.format(buscaPeloSanto))
