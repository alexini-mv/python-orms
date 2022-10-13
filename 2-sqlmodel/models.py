# Los modelos viene totalmente inspirados a los modelos de FastAPI, lo que si
# ya conoces esa libraria, se te facilitará la implementación.
from typing import Optional

from sqlmodel import SQLModel
from sqlmodel import Field

# Definimos el modelo. Nuestra clase hereda de SQLModel.
# En este caso será una tabla con nombre, apellido y edad.
# Es importante incluir la configuración `table=True`, ya que de esta forma le
# decimos a SQLModel que este modelo es un Modelo de Tabla, y no solo un 
# modelo de datos.
class Evangelion(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    last_name: str
    age: int
    rank: Optional[str] = None