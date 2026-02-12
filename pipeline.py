#Pipeline de Extração, Limpeza, Transformação e Enriquecimento de Dados

#Imports
import csv
import sqlite3

#Cria novo banco de dados
conn = sqlite3.connect('producao.db')

#Cria tabela para armazemento dos dados
conn.execute('''CREATE TABLE producao (
                produto TEXT,
                quantidade INTEGER,
                preco_medio REAL,
                receita_total REAL
            )''')

#Grava e fecha a conexão
conn.commit()
conn.close()

#Abre o arquivo CSV
with open('producao_alimentos.csv', 'r') as file:

  #Cria leitor CSV
  reader = csv.reader(file)

  #Ignora primeira linha
  next(reader)

  #Connecta banco de dados
  conn = sqlite3.connect('producao.db')

  #Insere linhas na tabela do banco de dados
  for row in reader:
    conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES (?, ?, ?, ?)', row)

  conn.commit()
  conn.close()

print("Operação concluida com sucesso!")