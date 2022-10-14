from models import db
from models import Angel


def crear_y_guardar():
    # Para instanciar un nuevo objeto podemos hacerlo de dos formas distintas:
    # 1.- La manera tradicional, que consiste en instanciar los objetos directamente.
    adan = Angel(name="Adan", number_angel=1)
    lilith = Angel(name="Lilith", number_angel=2)
    # Y salvamos dentro de la base el nuevo objeto.
    adan.save()
    lilith.save()

    # 2.- Creando el objeto usando un méodo especial para la creación o instanciador.
    sachiel = Angel.create(name="Sachiel", number_angel=3)
    shamshel = Angel.create(name="Shamshel", number_angel=4)

    # Y guardamos los objetos de la misma forma que la anterir.
    sachiel.save()
    shamshel.save()

    # Antes de guardar el objeto dentro de la tabla, podemos modificarla mediane la
    # notación punto.
    ramiel = Angel.create(name="Ramiel", number_angel=5)
    ramiel.name = "Tabris"
    ramiel.number_angel = 17

    ramiel.save()


def recuperar_informacion():
    # Para recuperar la información, lo hacemos directamente sobre la clase-tabla
    # con el método selec.

    angelito = Angel.select().where(Angel.name == "Shamshel").get()

    # O tambien se puede usar el método get como alternativa corta
    angelito2 = Angel.get(Angel.name == "Tabris")

    print(angelito.name, angelito2.name)
    print("---")
    # Para traer una lista de resultados, simplemente hacemos el select, e iteramos
    # para visualizar los datos obtenidos

    query = Angel.select().where(Angel.number_angel <= 3)

    for angel in query:
        print(f"name = {angel.name}, position = {angel.number_angel}")


if __name__ == "__main__":
    # Nos conectamos a la base de datos.
    db.connect()
    # Creamos el schema y la tabla
    db.create_tables([Angel])

    # Creamos nuevos registros y guardamos en la DB
    # crear_y_guardar()

    # Recuperamos la información de la DB
    recuperar_informacion()


    # Cerramos la conexión con la base de datos
    db.close()