print("""
004) Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
primitivo e todas as informações possíveis sobre ele. 
""")

entradaDoTeclado=input('Digite algo: ')

print('O tipo primitivo do conteúdo informado é: \
{}'.format(type(entradaDoTeclado)))

print('É um composto de letras e/ou números? Resposta: \
{}'.format(entradaDoTeclado.isalnum()))

print('É composto só de letras? Resposta: \
{}'.format(entradaDoTeclado.isalpha()))

print('É um número inteiro? Resposta: \
{}'.format(entradaDoTeclado.isdecimal()))

print('É um número (Dígito)? Resposta: \
{}'.format(entradaDoTeclado.isdigit()))

print('É um número (Numérico)? Resposta: \
{}'.format(entradaDoTeclado.isnumeric()))

print('É um identificador válido (Nome de variável)? Resposta: \
{}'.format(entradaDoTeclado.isidentifier()))

print('É um caractere imprimível? Resposta: \
{}'.format(entradaDoTeclado.isprintable()))

print('É composto apenas por espaços? Resposta: \
{}'.format(entradaDoTeclado.isspace()))

print('É um texto com as primeiras letras capitalizadas? Resposta: \
{}'.format(entradaDoTeclado.istitle()))

print('É composto apenas por letras minúsculas? Resposta: \
{}'.format(entradaDoTeclado.islower()))

print('É composto apenas por letras maiúsculas? Resposta: \
{}'.format(entradaDoTeclado.isupper()))
