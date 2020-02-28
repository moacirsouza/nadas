# Recebe um número, mostra o dobro, triplo e a raiz quadrada
numero = int(input('Digite um número inteiro: '))
dobro = 2*numero
triplo = 3*numero
raizquadrada = numero**(1/2)
print('O número digitado foi {}, o seu dobro é {}, o triplo é {}, e sua raíz quadrada é {:.3f}' . format(numero, dobro, triplo, raizquadrada))
