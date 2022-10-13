# Python ORM con sqlmodel

**sqlmodel** es la implementación de ORM inspirado fuertemente a el modelo de FastAPI. Es por eso que mucha de su sintaxis es similar a la utilizada en los Modelos de dicha libreria.

Para implementar el ORM, requiere de dividir el código en varios archivos.
* `models.py`:  Se definen aquí los modelos (tablas) que contendrá la base de datos.
* `db.py`:  Se define la Base de Datos, el schema y las tablas que serán creadas, al igual se crea el engine que permite la conexión con la DB.
* `main.py`:    Contendrá toda la lógica para modificar o extraer la información desde la base de datos, según se requiera.

Dentro de cada archivo, hay ejemplos del código implementado, con sus correspondientes comentarios explicativos.

## Referencias
* Documentación oficial de [sqlmodel](https://sqlmodel.tiangolo.com/).