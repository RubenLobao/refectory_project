#criando a base CRUD
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from database import TipoUsuario, Usuario, Presenca

SessionLocal = sessionmaker(bind=engine)

class BaseCRUD:
    def __init__(self, model):
        self.model = model

    def create(self, session, **kwargs):
        try:
            instance = self.model(**kwargs)
            session.add(instance)
            session.commit()
            session.refresh(instance)
            return instance
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Falha ao criar {self.model.__name__}: {e}")
            return None

    def read(self, session, id):
        try:
            return session.query(self.model).get(id)
        except SQLAlchemyError as e:
            print(f"Falha ao ler {self.model.__name__}: {e}")
            return None

    def update(self, session, id, **kwargs):
        try:
            instance = session.query(self.model).get(id)
            if instance:
                for key, value in kwargs.items():
                    setattr(instance, key, value)
                session.commit()
                session.refresh(instance)
                return instance
            return None
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Falha ao atualizar {self.model.__name__}: {e}")
            return None

    def delete(self, session, id):
        try:
            instance = session.query(self.model).get(id)
            if instance:
                session.delete(instance)
                session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Falha ao deletar {self.model.__name__}: {e}")
            return False

    def read_all(self, session):
        try:
            return session.query(self.model).all()
        except SQLAlchemyError as e:
            print(f"Falha ao ler todas as informações {self.model.__name__}: {e}")
            return []


# Definindo as classes específicas CRUD
class TipoUsuarioCRUD(BaseCRUD):
    def __init__(self):
        super().__init__(TipoUsuario)

class UsuarioCRUD(BaseCRUD):
    def __init__(self):
        super().__init__(Usuario)

class PresencaCRUD(BaseCRUD):
    def __init__(self):
        super().__init__(Presenca)

