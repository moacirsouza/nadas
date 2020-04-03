print( """\033[1;37;44m [036] Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, 
o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode 
exceder 30% do salário ou então o empréstimo será negado.\033[m """)
print("ola")
valorCasa = float(input("Digite o Valor da Casa: R$ "))
salario =  float(input("Digite o Valor do seu salario: R$ "))
anos =  int(input("Digite prazo para quitação do emprestimo em anos: "))
limite = float(salario*0.3)
prestacao =  float(valorCasa/(anos*12))
if prestacao > limite :
    print("com uma prestação de R${:.2f}, você passou seu limite disponivel de R${:.2f} para emprestimo \n Você teve o emprestimo \033[1;37;44m NEGADO \033[m ".format(prestacao,limite))
else:
    print("com uma prestação de R${:.2f}, você teve o emprestimo \033[1;37;44m APROVADO \033[m ".format(prestacao))