'''
Centro Universitário Adventista de São Paulo
Campus SP

Turma       : CI73A2019
Aluno       : Gilson Nunes dos Santos Junior
RA          : 96992
Matéria     : Desenvolvimento Web
Professor   : Clodonil Honorio Trigo
Módulo      : https://github.com/clodonil/Python-Fundamentals/tree/master/modulo1/exercicios

Data        : 20 de Março de 2019
Descrição   : Apresenta a população total brasileira, somando todos os valores na tabela.
'''

# Importar biblioteca
from lib.scrapy_table import Scrapy_Table as st

# Criamos os parâmetros e variáveis
site = "https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"
conexao = st(site)
tabela = conexao.get_tables(0)
populacao = 0

for linha in tabela[1:] :
	populacao = populacao + int(linha[4])

print("Total da população brasileira :", populacao)