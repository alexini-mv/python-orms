from sqlmodel import Session, select

from models import Evangelion
from db import engine


def add_users():
    # Creamos nuestros objetos que estarán dentro de la DB en la tabla Evangelion.
    # Cada objeto representará una fila de la tabla
    kaworu = Evangelion(name="Kaworu", last_name="Nagisa", age=13)
    misato = Evangelion(name="Misato", last_name="Katsuragi",
                        age=32, rank="Captain")
    kaji = Evangelion(name="Ryoji", last_name="Kaji",
                      age=33, rank="Special Inspector")

    # Cargamos los objetos a la DB iniciando una Session. Aqui lo haremos con la
    # sintaxis de with.
    with Session(engine) as session:
        # Podemos agregar los objetos uno por uno, o todos en una sola línea
        session.add_all([kaworu, misato, kaji])
        # Escribimos lo cambios directamente a DB
        session.commit()

    print("Tabla creada y datos agregados!!!")


def read_users():
    # Iniciamos una Session a la base de datos, y realizamos el query
    with Session(engine) as session:
        # Declaramos el query sobre la tabla-modelo
        query = select(Evangelion).where(Evangelion.age >= 18)
        # Ejecutamos el query sobre la session
        results = session.exec(query)

        for user in results:
            print( user)


if __name__ == "__main__":
    # add_users()
    read_users()
