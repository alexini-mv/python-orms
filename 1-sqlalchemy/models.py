# Declaramos los modelos a partir de los cuales se instanciarán los objetos en la BD.

# Importamos de SQLAlchemy los tipos que mapearan a la tabla. Recordemos que cada
# atributo será una columna dentro de la tabla. Y cada columna tendrá un tipo de 
# dato especifico. Además puede existir relaciones entre las diferentes tablas.
from sqlalchemy import Column, String, Integer
from base import Base


class User(Base):
    # Es obligatorio que todo modelo tenga un __tablename__
    __tablename__ = 'users'
    
    # Declaramos las columnas de la tabla.
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    last_name = Column(String(30))
    age = Column(Integer)

    def __init__(self, name: str, last_name: str, age: int) -> None:
        self.name = name 
        self.last_name = last_name
        self.age = age

    # Este método no es obligatorio, pero es bueno tenerlo para saber como es representado
    # el objeto que estamos declarando
    def __repr__(self) -> str:
        return f"User(id={self.uid}, name={self.name}, last_name={self.last_name}, age={self.age})"