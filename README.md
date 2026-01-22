# Estudos sobre vários DB no python
Repositório com exemplos práticos de operações CRUD (Create, Read, Update, Delete) utilizando diferentes tecnologias de banco de dados e interfaces.

## 📋 Tecnologias

- **SQLite** - Banco de dados relacional leve
- **PostgreSQL** - Banco de dados relacional robusto
- **MongoDB** - Banco de dados NoSQL orientado a documentos
- **SQLAlchemy** - ORM para Python
- **Tkinter** - Interface desktop
- **Streamlit** - Interface web

## 🗂️ Estrutura do Projeto

```
├── SQLite (arquivos 1-6)
│   ├── Criação de banco
│   ├── Criação de tabelas
│   ├── Operações CRUD básicas
│
├── MongoDB/
│   ├── Inserção, leitura, atualização e exclusão
│
├── postgres/
│   ├── Conexão e operações CRUD com PostgreSQL
│
├── aplicativo_desktop/
│   ├── Interface desktop com Tkinter
│   ├── ORM com SQLAlchemy
│
└── web/
    ├── Interface web com Streamlit
    ├── Formulários interativos
```

## 🚀 Como Usar

### SQLite Básico

```bash
# Criar banco de dados
python 1-db.py

# Criar tabela
python 2-tabela.py

# Inserir dados
python 3-inserindo.py

# Ler dados
python 4-leitura.py
```

### Aplicativo Desktop

```bash
cd aplicativo_desktop
python app.py
```

### Aplicativo Web

```bash
streamlit run web/form.py
```

### MongoDB

Certifique-se de ter o MongoDB instalado e rodando localmente, depois execute os scripts da pasta `MongoDB/`.

### PostgreSQL

1. Configure as credenciais em `postgres/post_connect.py`
2. Execute os scripts de operações conforme necessário

## 📦 Dependências

```bash
pip install streamlit
pip install sqlalchemy
pip install pymongo
pip install psycopg2
```

## 💡 Funcionalidades

- **CRUD completo** para filmes e jogos
- **Múltiplas interfaces**: linha de comando, desktop e web
- **Exemplos práticos** com diferentes bancos de dados
- **ORM e SQL puro** para diferentes necessidades

## 🎯 Objetivo

Este repositório serve como material de estudo e referência para operações básicas com bancos de dados em Python, demonstrando diferentes abordagens e tecnologias para o mesmo problema.

---

**Nota**: Os exemplos utilizam dados de filmes e jogos para demonstração. Adapte conforme sua necessidade.
