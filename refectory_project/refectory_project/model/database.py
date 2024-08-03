from sqlalchemy import *
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

DATABASE_URL = "mysql+pymysql://root:@localhost:3306/refectory_database"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class TipoUsuario(Base):
    __tablename__ = "tipo_de_usuario"

    id = Column(Integer, primary_key=True)
    tipo = Column(String(100), nullable=False)

    usuarios = relationship("Usuario", back_populates="tipo_de_usuario")

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    matricula = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)
    id_tipo_usuario = Column(Integer, ForeignKey('tipo_de_usuario.id'), nullable=False)

    tipo_de_usuario = relationship("TipoUsuario", back_populates = "usuarios")
    
    presencas = relationship("Presenca", back_populates="usuario")

class Presenca(Base):
    __tablename__ = "presencas"
    
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    data = Column(Date, nullable=False)
    hora_registro = Column(Time, nullable=False)
    
    usuario = relationship("Usuario", back_populates="presencas")

def init_db():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()

