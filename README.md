# Tutoriales de ORMs - Object Relational Mappers
ORM es un paradigma para interactuar con Base de Datos Relacionales dentro de python sin la necesidad de usar SQL. Para esto, se utiliza el enfoque de Programación Orientado a Objetos.

Con este enfoque, las Tablas de las BD relacionales se traducen en Clases. Las columnas en las bases de datos son trasladados a los atributos de las clases. Y cada reglón o registro dentro de una tabla corresponde a un objecto instanciado de la clase.

En este tutorial se revisa tres librerias para implementar ORM en python:
1. SQLAlchemy
2. SQLModel
3. Peewee

De las tres librerias. La más fácil de implementar es **Peewee**, seguido por nivel de complejidad por **SQLModel**, siendo **SQLAlchemy** la más compleja.

## Referencias
* Documentación de [SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/).
* Documentación de [SQLModel](https://sqlmodel.tiangolo.com/).
* Documentación de [Peewee](http://docs.peewee-orm.com/en/latest/index.html).