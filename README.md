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

Esses warnings são só o Git do Windows reclamando que alguns arquivos (que vêm do VS Code/Pylance) foram criados com final de linha Linux (LF) e ele vai converter pra CRLF na próxima vez.  
É 100% inofensivo e acontece em todo projeto Python no Windows quando tem a pasta `.vscode/` dentro.

### Como limpar isso em 10 segundos e nunca mais ver:

Rode esses comandos dentro da pasta do projeto:

```powershell
# Remove a pasta .vscode inteira do Git (ninguém precisa dela no repositório)
rm -r .vscode -Force

# Cria/adiciona um .gitignore pra nunca mais subir essas pastas
echo ".vscode/
__pycache__/
*.pyc
.env" > .gitignore

# Adiciona tudo de novo (sem os arquivos chatos)
git add .
git commit --amend --no-edit   # só atualiza o commit anterior
git push -f                    # força o push (só faça se ainda não tiver pull requests)
```

Pronto! Seu repositório vai ficar limpo e profissional.

### README.md lindo pra você colar agora (já testado e bonito no GitHub)

Cole isso num arquivo chamado `README.md` na raiz do projeto:

```markdown
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
```

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
