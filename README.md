# Biblioteca do Tio João  
**CRUD completo com Python + MySQL via linha de comando**  
Concluído em **menos de 1 hora** — do zero ao GitHub!

## Objetivo do projeto
Criar um sistema funcional mínimo (MVP) para gerenciar o acervo de uma pequena biblioteca usando apenas ferramentas reais do mercado:  
- MySQL via **linha de comando**  
- Python puro com **pymysql**  
- Git + GitHub com boas práticas  

O foco foi **aprender e dominar a integração real entre Python e banco de dados** de forma rápida, limpa e profissional.

## Planejamento e concepção (10 minutos)
1. Definir o domínio mais simples possível com CRUD completo → **cadastro de livros**
2. Escolher apenas **uma tabela** para não complicar (livros)
3. Priorizar clareza, velocidade e aprendizado prático
4. Decisão: tudo via terminal (sem Jupyter, sem interface gráfica)

## Tecnologias escolhidas e justificativa
| Tecnologia           | Motivo da escolha                                      |
|----------------------|--------------------------------------------------------|
| MySQL (linha de comando) | Skill obrigatória em 95% das vagas júnior/pleno     |
| Python 3 + pymysql   | Biblioteca leve, nativa e mais usada em empresas       |
| PowerShell + VS Code | Ambiente real de desenvolvimento Windows             |
| Git + GitHub         | Padrão absoluto da indústria                           |

## Estrutura do banco de dados
```sql
CREATE TABLE livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(80) NOT NULL,
    ano INT,
    disponivel BOOLEAN DEFAULT TRUE
);


```

## Como o código foi desenvolvido
1. Criação do banco e tabela diretamente no terminal MySQL
2. Inserção manual de 5 livros clássicos para testes iniciais
3. Criação do script `biblioteca.py` com:
   - Função `conectar()` com `DictCursor` (retorno como dicionário)
   - `listar_livros()` → SELECT + loop com formatação bonita
   - `cadastrar_livro()` → INSERT com validação de entrada
   - Menu interativo com `while True`
4. Tratamento básico de erros (ano inválido)
5. Commits organizados e .gitignore profissional

## Resultados dos testes realizados (100% sucesso)
| Teste realizado                          | Resultado                              |
|------------------------------------------|----------------------------------------|
| Listar livros iniciais                   | 5 livros exibidos corretamente         |
| Cadastrar novo livro                     | Inserido com sucesso no banco          |
| Listar novamente após cadastro           | Novo livro aparece na lista            |
| Conexão com banco recusando senha errada | Erro tratado corretamente              |
| Push completo para o GitHub              | Repositório limpo e funcional          |

**Tempo total do zero ao GitHub: 38 minutos**

## O que aprendi com este projeto
- Criar e manipular banco MySQL só com comandos
- Integrar Python com MySQL de forma segura e limpa
- Escrever scripts profissionais com menu interativo
- Dominar o fluxo completo: terminal → código → banco → GitHub
- Que é possível entregar valor real em menos de 1 hora com foco e método

## Próximos passos (já planejados)
- [ ] Sistema de empréstimos e devoluções
- [ ] Busca por título ou autor
- [ ] Relatório de livros mais emprestados
- [ ] Interface web com Flask (futuro)

**Feito em 23/11/2025**  
Higo Santos – @Higo80s  


---
⭐ Se esse projeto te ajudou, deixa uma estrela!  
Envie um feedback!
```
