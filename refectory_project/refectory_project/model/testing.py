from database import *
from crud_base import *


if __name__ == "__main__":

    session = SessionLocal()

    user_crud = UsuarioCRUD()
    user_type = TipoUsuarioCRUD()

    funcionario = user_type.create(session, descricao = "Funcionário")

    user = user_crud.create(session, nome = "Ruben", matricula = "12345", email = "rubenlobao18@gmail.com", senha = "uma senha",tipo_usuario = funcionario)