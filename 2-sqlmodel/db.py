# Agregamos la lógica para crear la conexión a la Base de Datos y el esquema 
# con las tablas definidas en models.py
from sqlmodel import create_engine, SQLModel
from models import * # Es importante importarlas para que se carguen dentro del objeto SQLModel

# Creamos la conexión a la DB con un engine. La opción `echo=True` ayuda para
# saber que pasa en cada paso de SQL, por lo que es relevante a la hora de 
# debuggear.
engine = create_engine("sqlite:///BaseDeDatos.db", echo=False)

# Creamos el schema de la base de datos, esto es, la base de datos y las tablas
# Declaradas en el modelos. Es sumamente importante importar los modelos que 
# heredan de SQLModel antes de ejecutar está sentencia.
SQLModel.metadata.create_all(engine)
