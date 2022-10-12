# Utilización del ORM de SQLAlchemy para guardar datos en DB
# Importamos las librerias necesarias.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Abrimos una conexión a la base de datos. En este caso SQLite.
# En este caso, si no existe, crea el archivo de la base de datos.

# Definimos los tres objetos que exportaremos. El primero es el objeto 
# que creará la conexión a la base de datos.
engine = create_engine('sqlite:///BaseDeDatos.db')
# Iniciamos una sesión
Session = sessionmaker(bind=engine)
# Declaramos el objeto que construirá el schema de la Base de Datos
Base = declarative_base()