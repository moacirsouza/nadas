print("""
\033[1;37;44m 032) \033[m Crie um programa em PYTHON que: leia um ano qualquer e moste se ele é BISSEXTO.
""") 
### if (year is not divisible by 4) then (it is a common year)
### else if (year is not divisible by 100) then (it is a leap year)
### else if (year is not divisible by 400) then (it is a common year)
### else (it is a leap year)
ano = int(input('Digite o Ano: '))
if ano%4!=0 or ano%400!=0 and ano%100==0:
    print('\nO ano é {} é Comum'.format(ano))
else:
    print('\nO ano é {} é Bissexto'.format(ano))
