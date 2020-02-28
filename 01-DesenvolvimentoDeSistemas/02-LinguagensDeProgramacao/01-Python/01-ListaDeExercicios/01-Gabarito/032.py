print("""
032) Faça um programa que leia um ano qualquer e moste se ele é BISSEXTO.
""")

### Entrada do programa: Recebe o número do ano como inteiro ("int").
ano = int(input('Informe o número do ano para saber se ele é bissexto: '))

### O seguinte pseudo-código pode ser encontrado no artigo oficial da 
### Wikipedia sobre ano bissexto. Nele é possível entender quais as
### verificações básicas para avaliar se um ano é bissexto ou não:
### https://en.wikipedia.org/wiki/Leap_year#Algorithm
# if (year is not divisible by 4) then (it is a common year)
# else if (year is not divisible by 100) then (it is a leap year)
# else if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year)

### O conceito matemático de divisibilidade é usado para realizar
### os testes deste programa. Um número é divisível por outro 
### quando o resto da divisão entre eles é zero.
if ano%4 != 0 or ano%400 != 0 and ano%100 == 0:
    print('{} é um ano comum.'.format(ano))
else:
    print('{} é um ano Bissexto'.format(ano))
