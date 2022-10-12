# Python ORM con SQLAlchemy

Para implementar un ORM con la libreria de SQLAlchemy, se necesita implementar tres archivos.
1. `Base`: Aquí se declara la conexión a la base de datos, la sesión y el schema.
2. `Models`: En este archivo se declaran los modelos, esto es, las clases que permitiran instanciar los objetos que serán guardados en la base de datos.
3. `Main`:  Se implementa la lógica para manipular la información en la BD. Esto es, abrir la conexión a la BD, instanciar los objetos, guardar cada objetos dentro de la tabla y cerrar la conexión