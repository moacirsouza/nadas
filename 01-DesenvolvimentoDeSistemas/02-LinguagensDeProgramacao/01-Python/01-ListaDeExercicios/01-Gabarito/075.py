print("""
075) Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma
tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
""")

### Solução 0: Essa solução é funcional, mas viola a regra de não utilizar
### conhecimentos ainda não ministrados no CeV até o momento da solicitação
### do exercício.
# listaTemporaria = []
# quantosNoves = 0
# essesSaoPares = ''
# ondeEstaoOsTres = []
# for contador in range(0,4):
#     listaTemporaria += [int(input('Informe um número inteiro entre 0 e 9: '))]
# tuplaComQuatroNumeros = tuple(listaTemporaria)
# for item in range(0, len(tuplaComQuatroNumeros)):
#     if tuplaComQuatroNumeros[item]%2 == 0:
#         essesSaoPares += str(tuplaComQuatroNumeros[item]) + ', '
#     if tuplaComQuatroNumeros[item] == 9:
#         quantosNoves += 1
#     if tuplaComQuatroNumeros[item] == 3:
#         ondeEstaoOsTres += [item]
#     item += 1
# if len(ondeEstaoOsTres) == 0:
#     posicaoDoPrimeiroTres = 'Não há números 3 nessa lista :(' 
# else:
#     posicaoDoPrimeiroTres = f'O primeiro três aparece na posição {ondeEstaoOsTres[0]}'

### Solução 1: Apesar de repetir código durante a solicitação de entrada de
### valores, esta solução não fere o acordo de não usar conhecimentos ainda
### não ministrados pelo CeV até a solicitação do execício.
tuplaComQuatroNumeros = (int(input('Primeiro número: ')),
                         int(input('Segundo número: ')),
                         int(input('Terceiro número: ')),
                         int(input('Quarto número: ')))

### Inicia a variável como string vazia, por causa do teste que será realizado
### para verificar se existem, ou não, números pares na tupla.
essesSaoPares = ''

### Avalia cada item, a fim de verificar se existem números pares. Em caso
### positivo, a string "essesSaoPares" vai sendo incrementada com o valor
### do número, além uma vírgula e um espaço, para melhor organização visual.
for item in tuplaComQuatroNumeros:
    if item%2 == 0:
        essesSaoPares += str(item) + ', '

### Em Python, uma "string" vazia, quando convertida para "Boolean", mesmo
### implicitamente, como neste caso, retorna o valor False. Como a variável
### "essesSaoPares" foi iniciada como vazia, se ela não recebeu nenhum valor
### durante a verificação do laço, significa que ela permanece vazia e assim,
### não existem números pares na tupla.
if not essesSaoPares:
    essesSaoPares = 'Não há números pares nesta tupla.'
else:
    essesSaoPares = f'Lista de números pares: {essesSaoPares[:-2]}.'

posicaoDoPrimeiroTres = 'Não há números 3 nessa lista.'

if 3 in tuplaComQuatroNumeros:
    ### A fim de evitar ultrapassar a coluna 80, a inicialização da variável
    ### "posicaoDoPrimeiroTres" empregou o uso da a barra invertida como quebra
    ### de linha
    posicaoDoPrimeiroTres = 'O primeiro número "3" aparece na posição: ' + \
                            str(tuplaComQuatroNumeros.index(3)+1)

print('\nResultado:')
print(f'O nove aparece {tuplaComQuatroNumeros.count(9)} vez(es).')
print(essesSaoPares)
print(posicaoDoPrimeiroTres)
