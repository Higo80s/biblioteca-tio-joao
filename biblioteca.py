# biblioteca.py - Biblioteca do Tio João
import pymysql

def conectar():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='f1&Y!%v8@0W1VC',   # ← SUA SENHA AQUI
        database='biblioteca_tio_joao',
        cursorclass=pymysql.cursors.DictCursor
    )

def listar_livros():
    conn = conectar()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM livros ORDER BY id")
        livros = cursor.fetchall()
    conn.close()
    
    print("\n=== LIVROS DA BIBLIOTECA DO TIO JOÃO ===\n")
    for livro in livros:
        status = "Disponível" if livro['disponivel'] else "Emprestado"
        print(f"{livro['id']} - {livro['titulo']} - {livro['autor']} ({livro['ano']}) [{status}]")
    print()

def cadastrar_livro():
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    while True:
        try:
            ano = int(input("Ano: "))
            break
        except ValueError:
            print("Digite apenas números!")
    
    conn = conectar()
    with conn.cursor() as cursor:
        sql = "INSERT INTO livros (titulo, autor, ano) VALUES (%s, %s, %s)"
        cursor.execute(sql, (titulo, autor, ano))
    conn.commit()
    conn.close()
    print("Livro cadastrado com sucesso!\n")

# MENU PRINCIPAL
print("=== Biblioteca do Tio João ===")
while True:
    print("\n1 - Listar todos os livros")
    print("2 - Cadastrar novo livro")
    print("3 - Sair")
    opcao = input("\nEscolha (1/2/3): ").strip()
    
    if opcao == "1":
        listar_livros()
    elif opcao == "2":
        cadastrar_livro()
    elif opcao == "3":
        print("Até logo! Volte sempre!")
        break
    else:
        print("Opção inválida! Tente novamente.")