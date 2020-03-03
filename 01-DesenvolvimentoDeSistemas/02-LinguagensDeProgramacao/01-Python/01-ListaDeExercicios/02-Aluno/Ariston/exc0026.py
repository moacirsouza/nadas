print("""
026) Crie um programa em PYTHON que: leia uma frase pelo teclado e mostre: 
a) Quantas vezes aparece a letra "A"; 
b) Em que posição ela aparece a primeira vez; 
c) Em que posição ela aparece a última vez.
""")

frase = str(input('Digite a frase: '))
contarA=frase.upper().count('A')
primeiroA=(frase.upper().find('A'))+1
ultimoA=(frase.upper().rfind('A'))+1
print('\nNa frase: "{}" \ntemos: {} "A" \nele aparece primeiramente na posição: {} \ne por último na posição: {}.'.format(frase,contarA,primeiroA,ultimoA))
