print("""
051) Desenvolva um programa que leia o primeiro termo e a razão de uma
PA. No final, mostre os 10 primeiros termos dessa progressão.
""")
primeirotermo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
décimo = primeirotermo + (10-1)*razão
for contador in range (primeirotermo, décimo, razão):
    print('{} '.format(contador), end=' ')
print('ACABOU')

