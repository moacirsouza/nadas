print("""
105) Faça um programa que tenha uma função notas() que pode receber várias
notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
""")

def apresentaNotas(*notasDosAlunos, apresentaSituacao=False):
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
    quantidade = len(notasDosAlunos)
    maiorNota = max(notasDosAlunos)
    menorNota = min(notasDosAlunos)
    somaDasNotas = sum(notasDosAlunos)
    media = somaDasNotas/quantidade

    if 0 < media <= 5.9:
        situacao = 'RUIM'
    elif 5.9 < media < 9:
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

resposta = apresentaNotas(9.6, 8.9, 9, apresentaSituacao=True)
print(resposta)
# help(apresentaNotas)
