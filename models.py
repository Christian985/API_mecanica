from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from dotenv import load_dotenv
import os  # Criar variável de ambiente '.env'
import configparser  # Criar arquivo de configuração 'config.ini'

# Configurar Banco Vercel
# Ler variável de ambiente
load_dotenv()

# Carregue as configurações do Banco de Dados
url_ = os.environ.get("DATABASE_URL")
print(f'modo1:{url_}')

# Carregue o arquivo de configuração
config = configparser.ConfigParser()
config.read('config.ini')

# Obtenha as configurações do Banco de Dados
# database_url =config['database']['url']
# print(f'mode2:{database_url}')

# Configuração com a conexão com o Banco de Dados SQLite Online e local
# engine = create_engine(database_url) # Conectar Vercel

engine = create_engine('sqlite:///mecanica.sqlite3')  # Conectar local alterado/substituído

# Gerencia as sessões com o Banco de Dados
# db_session = scoped_session(sessionmaker(bind=engine))
Local_session = sessionmaker(bind=engine)

# Base_declarativa - Ela permite que você defina Classes Python que representam tabelas de
# Banco de Dados de forma declarativa, sem a necessidade de configurar manualmente a
# relação entre as Classes e as Tabelas.
Base = declarative_base()


# Base.query = db_session.query_property()


# Veículos
# Dados mais importantes:
# 1 - ID
# 2 - cliente_associado
# 3 - placa

# Mais precisam de controle:
# 1 - modelo
# 2 - ano_fabricacao
# 3 - marca
# 4 - placa
class Veiculo(Base):
    # Tabela de Veículos
    __tablename__ = 'veiculos'
    id = Column(Integer, primary_key=True)
    cliente_associado = Column(Integer, ForeignKey('clientes.id'), nullable=False, index=True)
    modelo = Column(String(100), nullable=False, index=True)
    placa = Column(String(100), nullable=False, index=True)
    ano_fabricacao = Column(Integer, nullable=False, index=True)
    marca = Column(String(100), nullable=False, index=True)

    # Representação de Classe
    def __repr__(self):
        return '<Veiculo: {} {} {} {} {}>'.format(self.cliente_associado,
                                                  self.modelo,
                                                  self.placa,
                                                  self.ano_fabricacao,
                                                  self.marca)

    # Função para Salvar no Banco
    def save(self, db_session):
        try:
            db_session.add(self)
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            raise e

    # Função para Deletar no Banco
    # def delete(self):
    #     db_session.delete(self)
    #     db_session.commit()

    # Coloca os Dados na Tabela
    def serialize_user(self):
        dados_user = {
            'cliente_associado': self.cliente_associado,
            'modelo': self.modelo,
            'placa': self.placa,
            'ano_fabricacao': self.ano_fabricacao,
            'marca': self.marca,
        }
        return dados_user


# Clientes
# Dados mais importantes:
# 1 - ID
# 2 - nome
# 3 - cpf
# 4 - telefone
# 5 - endereco

# Mais precisam de controle:
# 1 - nome
# 2 - cpf
# 3 - telefone
# 4 - endereco
class Cliente(Base):
    # Tabela de Clientes
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False, index=True)
    cpf = Column(String, nullable=False, index=True)
    email = Column(String(100), nullable=False, index=True)
    telefone = Column(String, nullable=False, index=True)
    endereco = Column(String(100), nullable=False, index=True)

    # Representação Classe
    def __repr__(self):
        return '<Cliente: {} {} {} {} {}>'.format(self.nome,
                                                  self.cpf,
                                                  self.email,
                                                  self.telefone,
                                                  self.endereco)

    # Função para Salvar no Banco
    def save(self, db_session):
        try:
            db_session.add(self)
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            raise e

    # Função para Deletar
    # def delete(self):
    #     db_session.delete(self)
    #     db_session.commit()

    # Coloca os Dados na Tabela
    def serialize_user(self):
        dados_user = {
            'id_user': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'email': self.email,
            'telefone': self.telefone,
            'endereco': self.endereco,
        }
        return dados_user


# Ordens e Serviços
# Dados mais importantes:
# 1 - ID
# 2 - status
# 3 - descricao_servico
# 4 - valor_estimado

# Mais precisam de controle:
# 1 - veiculo_associado
# 2 - data_abertura
# 3 - descricao_servico
# 4 - status
# 5 - valor_estimado
class Ordem(Base):
    # Tabela de Ordens e Serviços
    __tablename__ = 'ordens'
    id = Column(Integer, primary_key=True)
    veiculo_associado = Column(Integer, ForeignKey('veiculos.id'), nullable=False, index=True)
    data_abertura = Column(String(100), nullable=False, index=True)
    descricao_servico = Column(String(100), nullable=False, index=True)
    status = Column(String(100), nullable=False, index=True)
    valor_estimado = Column(Float, nullable=False, index=True)

    # Representação de Classe
    def __repr__(self):
        return '<Ordem: {} {} {} {} {}>'.format(self.veiculo_associado,
                                                self.data_abertura,
                                                self.descricao_servico,
                                                self.status,
                                                self.valor_estimado)

    # Função para Salvar
    def save(self, db_session):
        try:
            db_session.add(self)
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            raise e

    # Função para Deletar
    # def delete(self):
    #     db_session.delete(self)
    #     db_session.commit()

    # Coloca os Dados na Tabela
    def serialize_user(self):
        dados_user = {
            'veiculo_associado': self.veiculo_associado,
            'data_abertura': self.data_abertura,
            'descricao_servico': self.descricao_servico,
            'status': self.status,
            'valor_estimado': self.valor_estimado,
        }
        return dados_user


# Metodo para criar Banco
def init_db():
    Base.metadata.create_all(bind=engine)


# Iniciar o Banco
if __name__ == '__main__':
    init_db()
