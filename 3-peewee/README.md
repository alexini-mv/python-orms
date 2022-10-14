# Implementación de un ORM con Peewee

*Peewee* es un ORM sencillo y pequeño. Tiene muchos conceptos expresivos, construidos para ser fácil de aprende e intuitivo de usar.

Tiene soporte para DB como sqlite, mysql, postgresql and cockroachdb.

Al igual que las librerias pasadas, es necesario crea los modelos en forma de clases, que mapea a la base de datos.

|Objecto|Corresponde a...|
|---|---|
|Clase Model|Tabla en la base de datos|
|Un campo de instancia|Columna en la tabla|
|Modelo instanciado|Renglón de una tabla en la base de datos|

Los archivos necesarios como se distribuye el código es el siguiente:
* `models.py`:  Donde se definen las clases modelos.
* `main.py`:    Archivo donde se define la lógica.

En este caso no se requiere un archivo especial de `db`, debido a la facilidad para abrir
una conexión o la creación del schema, que dentro del archivo `main.py` entran a la perfección.

## Referencias
* Documentación oficial de [peewee](http://docs.peewee-orm.com/en/latest/index.html).