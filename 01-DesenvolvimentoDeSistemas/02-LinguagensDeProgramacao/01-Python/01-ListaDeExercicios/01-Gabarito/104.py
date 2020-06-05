print("""
104) Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
semelhante à função input() do Python, só que fazendo a validação para aceitar
apenas um valor numérico. Ex: n = leiaInt('Digite um n: ')
""")

def leiaInt(mensagem):
    while True:
        numero = input(mensagem)
        
        if not numero.isnumeric():
            print(f'ERRO: [{numero}] não é um número inteiro positivo.')
        else:
            break
    
    return numero


supostoNumero = leiaInt('Digite um número inteiro positivo: ')
print(f'Você digitou o número {supostoNumero}.')
