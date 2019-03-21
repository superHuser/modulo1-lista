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
Descrição   : Listar todos os municípios, juntamente com sua população, se for maior ou igual a 70.000
'''

# Importar biblioteca
from lib.scrapy_table import Scrapy_Table as st

# Criamos os parâmetros e variáveis
site = "https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"
conexao = st(site)
tabela = conexao.get_tables(0)

print("Municipio | População")
print("----------------------")

for linha in tabela[1:] :
	if int(linha[4]) > 70000 :
		print(linha[2], '|', linha[4], "habitantes")

print("######################")