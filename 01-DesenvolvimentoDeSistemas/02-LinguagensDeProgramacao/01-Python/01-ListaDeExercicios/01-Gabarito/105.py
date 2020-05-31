print("""
105) Faça um programa que tenha uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
""")

def notas(*notas, apresentaSituacao=False):
    """Função que sumariza informações sobre notas e média de uma turma
    de tamanho variável.

    Keyword Arguments:
        apresentaSituacao {bool} -- (default: {False})
        Permite apresentar ou surpimir a situação da turma, conforme
        os critérios a seguir:
        - RUIM: Média entre 0 e 5.9
        - BOA: Média entre 6 e 8
        - EXCELENTE: Média acima de 9
        

    Returns:
        [dict] -- Retorna o seguinte conjunto de informações, em um
        dicionário:
        - Quantidade de Notas
        - Maior Nota
        - Menor Nota
        - Média da Turma
        - Situação da Turma [Se apresentaSituacao=True]
    """
    quantidade = len(notas)
    maiorNota = max(notas)
    menorNota = min(notas)
    somaDasNotas = sum(notas)
    media = somaDasNotas/quantidade

    if 0 < media <= 5.9:
        situacao = 'RUIM'
    elif 5.9 < media <= 8:
        situacao = 'BOA'
    else:
        situacao = 'EXCELENTE'

    resposta = {'Quantidade de Notas':quantidade,
                'Maior Nota':maiorNota,
                'Menor Nota':menorNota,
                'Média da Turma':f'{media:.2f}'}
    
    if apresentaSituacao:
        resposta.update({'Situação da Turma':situacao})
    
    return resposta

resposta = notas(8.6, 7.7, 8.9, 10, 2.5, 7, 8, 1.0, 0.5, 3.2, apresentaSituacao=True)
print(resposta)
# help(notas)        
