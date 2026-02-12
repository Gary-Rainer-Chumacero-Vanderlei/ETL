#Pipeline de Extração, Limpeza, Transformação e Enriquecimento de Dados

#Regra de negócio: Carregar apenas registros com quantidade acima de 10.

#Imports
import csv
import sqlite3

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

  #Cria nova tabela
  conn.execute('''CREATE TABLE producao (
                  produto TEXT,
                  quantidade INTEGER,
                  preco_medio REAL,
                  receita_total REAL
              )''')
  
  #Insere no BD as linhas com quantidade superior a 10
  for row in reader:
    if int(row[1]) > 10:
      conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES (?, ?, ?, ?)', row)

  conn.commit()
  conn.close()

print("Operação concluída com sucesso!")