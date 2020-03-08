print("""
\033[1;37;44m 031) \033[m Crie um programa em PYTHON que:pergunte a distância de uma viagem em Km. Calcule o preço da
passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas.
""") 
distancia = float(input('Qual a distancia da viagem: '))
limite = 200
curta = 0.5
longa = 0.45
if distancia > limite:
    print('\nO valor da passagem é R$ {:.2f}'.format(distancia*longa))
else:
    print('\nO valor da passagem é R$ {:.2f}'.format(distancia*curta))