print("""
075) Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma
tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
""")
listaTemporaria = []
quantosNoves = 0
essesSaoPares = ''
ondeEstaoOsTres = []
for contador in range(0,4):
    listaTemporaria += [int(input('Informe um número inteiro entre 0 e 9: '))]
tuplaComQuatroNumeros = tuple(listaTemporaria)
for item in range(0, len(tuplaComQuatroNumeros)):
    if tuplaComQuatroNumeros[item]%2 == 0:
        essesSaoPares += str(tuplaComQuatroNumeros[item]) + ', '
    if tuplaComQuatroNumeros[item] == 9:
        quantosNoves += 1
    if tuplaComQuatroNumeros[item] == 3:
        ondeEstaoOsTres += [item]
    item += 1
if len(ondeEstaoOsTres) == 0:
    posicaoDoPrimeiroTres = 'Não há números 3 nessa lista :(' 
else:
    posicaoDoPrimeiroTres = f'O primeiro três aparece na posição {ondeEstaoOsTres[0]}'
print(f'O nove aparece {quantosNoves} vezes.')
print(f'Lista de números pares: {essesSaoPares[:-2]}.')
print(posicaoDoPrimeiroTres)
