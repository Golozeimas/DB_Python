from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# cria a engine para criar o banco
engine = create_engine("sqlite:///banco.db", echo=True)

# importante para a ORM
Base = declarative_base()

# classe "filme", tem que passar o 'Base', para utilizar a ORM
# a classe == tabela
class Filme(Base):
    # esse é o nome da tabela
    __tablename__ = "filmes"
    
    # essa é a coluna de id, (int, key primária)
    id = Column(Integer, primary_key=True)

    # essa é a coluna de nome
    nome = Column(String, nullable=False)

    # essa é a coluna de ano
    ano = Column(Integer, nullable=False)

    # essa é a coluna de nota
    nota = Column(Float, nullable=False)

# Cria toda a estrutura do banco de dados
Base.metadata.create_all(engine)

# usa o session quando for criar as funções do nosso CRUD
def adiciona_filme(nome, ano, nota):
    Session = sessionmaker(bind=engine)
    # inicializa a sessão, que vai ser utilizada para fazer as operações do CRUD
    session = Session()
    # os das colunas com os respctivos parâmetros
    filme = Filme(nome=nome, ano=ano, nota=nota)
    session.add(filme)
    session.commit()
    session.close()

# adiciona_filme("Mario", 2022, 9.0)
# adiciona_filme("Sonic", 2020, 8.0)
# adiciona_filme("Hobbit", 2008, 7.0)

def atualizar_dados(id, nome = None, ano = None, nota = None):
    Session = sessionmaker(bind=engine)
    session = Session()
    # faça a query 
    filme = session.query(Filme).filter_by(id=id).first()

    if filme:
        # != null
        if nome is not None:
            filme.nome = nome
        if ano is not None:
            filme.ano = ano
        if nota is not None:
            filme.nota = nota
        session.commit()
    session.close()

# atualizar_dados(3, "El camino", 2022, 9.0)


def deletar_dados(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=id).first()
    if filme:
        session.delete(filme)
    session.commit()
    session.close()

# deletar_dados(4)