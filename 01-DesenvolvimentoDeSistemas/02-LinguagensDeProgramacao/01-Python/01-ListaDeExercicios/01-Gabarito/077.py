print("""
077) Crie um programa que tenha uma tupla com várias palavras (não usar
acentos). Depois disso, você deve mostrar, para cada palavra, quais são
as suas vogais.
""")

listaDePalavras = ('mongoloide', 'egregios', 'assincrona', 'mitigar',
                   'sincrona', 'confinamento', 'zaragatoa',
                   'comorbidade', 'inferir', 'dicotomia', 'connosco',
                   'inerente', 'moratoria', 'corroborar', 'conquanto')

for palavra in listaDePalavras:
    print(f'\nAs vogais da palavra {palavra.upper()}, são: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
print('')
