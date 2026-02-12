#Pipeline de Extração, Limpeza, Transformação e Enriquecimento de Dados

#Regra de negócio: Carregar apenas registros com "quantidade" acima de 10.
#Especificação: Remover caractere "ponto" da coluna "receita total".
#Regra de negócio: Adicionar coluna com margem de lucro do produto.

#Imports
import csv
import sqlite3

#Remove caractere "ponto"
def remove_ponto(valor):
  return int(round(float(valor.replace('.', '')), 0))

#Abre arquivo CSV
with open ('producao_alimentos.csv', 'r') as file:

  #Cria leitor CSV
  reader = csv.reader(file)

  #Pula primeira linha
  next(reader)

  #Connecta ao BD
  conn = sqlite3.connect('producao.db')

  #Deleta tabela existente, caso exista
  conn.execute('DROP TABLE IF EXISTS producao')

  #Cria nova tabela, altera receita_total para inteiro e adiciona coluna "margem_lucro"
  conn.execute('''CREATE TABLE producao (
                  produto TEXT,
                  quantidade INTEGER,
                  preco_medio REAL,
                  receita_total INTEGER,
                  margem_lucro REAL
              )''')
  
  #Insere no BD as linhas com quantidade superior a 10
  for row in reader:
    if int(row[1]) > 10:

      #Remove caractere "ponto" e converte em inteiro
      row[3] = remove_ponto(row[3])

      #Calcula margem de lucro bruta: receita total dividido pela quantidade de produtos, menos preço medio
      margem_lucro = round((row[3] / float(row[1])) - float(row[2]), 2)

      #Insere registro no BD
      conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total, margem_lucro) VALUES (?, ?, ?, ?, ?)', (row[0], row[1], row[2], row[3], margem_lucro))

  conn.commit()
  conn.close()

print("Operação concluída com sucesso!")