from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import enum

DATABASE_URL = "mysql+pymysql://root:@localhost:3306/refectory_database"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class TipoUsuarioEnum(enum.Enum):
    aluno = "aluno"
    funcionario = "funcionario"
    visitante = "visitante"

class TipoUsuario(Base):
    __tablename__ = "Tipo de Usuários"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(100), nullable=False)

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    matricula = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)
    tipo = Column(Enum(TipoUsuarioEnum), nullable=False)
    
    presencas = relationship("Presenca", back_populates="usuario")

class Presenca(Base):
    __tablename__ = "presencas"
    
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    data = Column(Date, nullable=False)
    hora_registro = Column(Time, nullable=False)
    
    usuario = relationship("Usuario", back_populates="presencas")


