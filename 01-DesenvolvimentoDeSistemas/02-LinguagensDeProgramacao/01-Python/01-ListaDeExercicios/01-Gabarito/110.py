print("""
110) Adicione o módulo moeda.py criado nos desafios anteriores, uma função
chamada resumo(), que mostre na tela algumas informações geradas pelas
funções que já temos no módulo criado até aqui.
""")

from utilidadesCeV import moeda

preco = float(input('Informe o preço: ').strip())
aumento = float(input('Informe o acréscimo percentual: ').strip())
reducao = float(input('Informe a reducao percentual: ').strip())

moeda.resumo(preco, aumento, reducao)
