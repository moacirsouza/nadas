print("""
051) Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
""")

### A fórmula para calcular o enésimo termo de uma PA é dada
### por a(n) = a(1) + (n-1)r, onde "a(n)" é o enésimo termo, 
### "a(1)" é primeiro termo, "n" é a posição do enésimo termo
### e "r é a razão da PA.
### Fonte: https://www.somatematica.com.br/emedio/pa/pa3.php

primeiroTermo = int(input('Informe o primeiro termo da PA: ').strip())
razao = int(input('Informe a razão da PA: ').strip())

### O motivo de usar o décimo primeiro termo ao invés do décimo
### é por causa do comportamento da Classe range. Como o ponto
### de parada é um intervalo aberto, precisamos do próximo número
### para atender aos requisitos do enunciado.
decimoPrimeiroTermo = primeiroTermo + (11-1)*razao

print('\nOs dez primeiros termos de uma PA que começa com \
{} e tem razão {}, são: '.format(primeiroTermo, razao), end='')

for elemento in range(primeiroTermo, decimoPrimeiroTermo, razao):
    print(elemento, end=' ')
print('\n')
