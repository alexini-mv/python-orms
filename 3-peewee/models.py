# Importamos los objetos que mapearan a la tabla.
# Importamos la clase del cual heredaran todos nuestros modelos
from peewee import Model
# Importamos el engine especifico para nuestra base de datos.
from peewee import SqliteDatabase
# Importamos las clases especiales que indicarán el tipo de dato en la columna
from peewee import CharField, IntegerField, PrimaryKeyField

# Definimos el tipo de base de datos que realizará la conexión.
db = SqliteDatabase('BaseDeDatos.db')


class Angel(Model):
    name = CharField()
    number_angel = IntegerField()

    class Meta:
        # Esta subclase realiza la conexión entre el objeto y la DB.
       database = db
