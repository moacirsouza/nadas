print("""
112) Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo
chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar
como a função input(), mas com uma validação de dados para aceitar apenas
valores que sejam monetários.
""")

from modulos import moeda
from utilidadesCeV import dado

preco = dado.leiaDinheiro('Informe o preço (R$): ')
moeda.resumo(preco, 10, 15)
