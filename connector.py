import mysql.connector
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1144186@Aa",
    database="projeto-crud"
)

cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario (
               id_usuario INT AUTO_INCREMENT,
               nome VARCHAR(255) NOT NULL,
               senha VARCHAR(255) NOT NULL,
               email VARCHAR(255) NOT NULL

    )
""")

def inserir_pessoa_com_senha_email (nome, senha, email):
    cursor = conexao.cursor()
    sql = "INSERT INTO usuario (nome, senha, email) VALUES (%s, %s, %s)"
    val = (nome, senha, email)
    cursor.execute(sql, val)
    conexao.commit()
    print(f"{cursor.rowcount} registro(s) inserido(s).")

def listar_pessoas_com_senha_email():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuario")
    usuario = cursor.fetchall()
    for usuario in usuario:
        print(usuario)

inserir_pessoa_com_senha_email("Alice", "1234", "alice@email.com")
inserir_pessoa_com_senha_email("Bob", "12345", "bob@email.com")
listar_pessoas_com_senha_email()

conexao.close()