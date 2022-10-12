from base import Base, engine, Session
from models import User


def main():
    # Creamos el schema de la base de datos a partir de la conexión
    Base.metadata.create_all(engine)

    # Abrimos una sesión actual a la base de datos, ya sea de esta
    # forma o con un with.
    session = Session()

    # Instanciamos a cada uno de los registros de la tabla
    shinji = User(name="Shinji",
                  last_name="Ikari",
                  age=13)

    rei = User(name="Rei",
               last_name="Ayanami",
               age=14)

    asuka = User(name="Asuka",
                 last_name="Langley Soryu",
                 age=13)

    mari = User(name="Mari",
                last_name="Makinami",
                age=16)

    # Se puede agregar uno por uno cada registro con el método session.add()
    # o como en este caso, agregar todos a la vez
    session.add_all([shinji, rei, asuka, mari])

    # Para guardar definitivamente los datos en la BD, debemos emplear el método commit
    session.commit()

    # Cerramos la sesión cuando hayamos terminado de trabajar
    session.close()

if __name__ == '__main__':
    main()
