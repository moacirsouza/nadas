print("""
\033[1;37;44m 035) \033[m  Crie um programa em PYTHON que: leia o comprimento de três retas e diga ao usuário se
elas podem ou não formar um triângulo.
""") 
Lado01 = float(input('Digite um lado do triangulo: '))
Lado02 = float(input('Digite um lado do triangulo: '))
Lado03 = float(input('Digite um lado do triangulo: '))

if (Lado01+Lado02 > Lado03):
    if(Lado03+Lado02 > Lado01):
        if(Lado01+Lado03 > Lado02):
            print("\nÉ um \033[1;33mTRIANGULO\033[m")
else:
    print('\nNão é \033[1;30;47mTRIANGULO\033[m')