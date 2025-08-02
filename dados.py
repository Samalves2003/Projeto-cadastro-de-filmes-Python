import sqlite3

def cria_tabela():
    conexao = sqlite3.connect('titulo.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

# Executa a criação ao rodar o programa
cria_tabela()

# 1- Conectar no BD
def conecta_bd():
    conexao = sqlite3.connect('titulo.db')
    return conexao

# 2- Inserir Dados
def insere_dados(nome, ano, nota):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute( 
    """
        INSERT INTO filmes(nome, ano, nota)
        VALUES (?, ?, ?)
    """, (nome, ano, nota)
    )
    conexao.commit()
    conexao.close()
    
# 3 - Listagem de Dados
def obter_dados():
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM filmes")
    dados = cursor.fetchall()
    cursor.close()
    return dados