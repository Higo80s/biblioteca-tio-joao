# Biblioteca do Tio João  

**Projeto concluído em menos de 1 hora!**  
CRUD completo com **Python + MySQL** usando apenas linha de comando.

## Funcionalidades
- Listar todos os livros
- Cadastrar novo livro
- Conexão segura com MySQL via `pymysql`
- Menu interativo no terminal

## Tecnologias usadas
- Python 3.13
- MySQL (via terminal)
- pymysql
- VS Code + PowerShell

## Como rodar
```bash
pip install pymysql
python biblioteca.py


## Estrutura do banco
```sql
CREATE TABLE livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(80) NOT NULL,
    ano INT,
    disponivel BOOLEAN DEFAULT TRUE
);
```

## Próximos passos (já planejados)
- Empréstimo e devolução de livros
- Busca por título/autor
- Relatório de livros mais emprestados

** Projeto de estudo 100% funcional com integração real de banco de dados**  
Feito em 23/11/2025!
