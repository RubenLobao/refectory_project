from crud_base import *
from database import *

import database

database.init_db()


if __name__ == "__main__":

    session = SessionLocal()

    crud_user = UsuarioCRUD()
    crud_typeUser = TipoUsuarioCRUD()


    funcionario = crud_typeUser.create(session, tipo="Funcionário")
    aluno = crud_typeUser.create(session, tipo="Aluno")
    avulso = crud_typeUser.create(session, tipo="Avulso")
    user = crud_user.create(session, nome="Ruben", matricula="123456", email="ruben@email.com", senha="alguma senha", id_tipo_usuario=1)

    session.close()