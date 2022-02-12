La aplicación permite realizar el registro y la modificación de tanto de la lista de dueños de los predios, así como de los mismos predios.
Para la base de datos se usa una relación many to many, lo cual permite que se compartan los datos con mayor facilidad entre las tablas, además de permitir generar relaciones claras, como es el caso en el modelo de la aplicación.
![image](https://user-images.githubusercontent.com/90158740/153697780-370b0de2-4096-432f-8f65-e6add5fd832b.png)


La aplicación se puede subir tanto a un contenedor de docker como a una aplicación de heroku, como es el caso. Link base: http://shrouded-eyrie-59397.herokuapp.com/

Pasos para usarla localmente:

1. Abir una terminal en la carpeta donde se tiene almacenado (Tener python previamente instalado)
2. ejecutar `python3 -m venv env` si es en linux/mac o `python -m venv env` si es en windows
3. ingresar `source env/bin/activate` si es en linux/mac o `env/Scripts/activate`
4. ejecutar el comando `python3/py pip install django` y `python3/py pip install djangorestframework` (python3 o py dependiendo del sistema operativo)
5. ejecutar en este orden los siguientes comandos: `python3/py manage.py makemigrations` , `python3/py manage.py migrate` y `python3/py manage.py runserver`
6. abrir la dirección que retorna la terminal 

Guía de uso:
![image](https://user-images.githubusercontent.com/90158740/153697167-e1dbcc34-af4c-4bb0-9e59-45f39ea93939.png)
En la pantala principal se podrá ver las vistas que tiene la aplicación, la primera vista a la cual se debe acceder es a la de owner, en la cual se puede tanto ver a los dueños que ya se encuentran en el sistema, así como la posibilidad de registrar un nuevo dueño.
![image](https://user-images.githubusercontent.com/90158740/153697285-34a25a8a-ffac-49fd-bb9a-a97e0215485c.png)
Esta es la manera en la cual se ven los dueños ya registrados, además de poder visualizar los predios de los cuales son dueños.
![image](https://user-images.githubusercontent.com/90158740/153697306-89d4405e-7850-41c2-b65b-e1a93404f88c.png)
Esta es la vista del formulario para registrar al usuario.

Al registrarse el usuario se retornará la siguiente vista, para retornar a la pantalla anterior se debe dar click al botón GET (resaltado en rojo), o para retornar a la vista original dar click al link  api root (resaltado en azul)
![image](https://user-images.githubusercontent.com/90158740/153697375-807ad8da-db22-4569-a513-8a568558b69d.png)

La vista de predios es muy similar a la de los dueños, solo cabe destacar que a la hora de registrar un nuevo predio se tiene que enlazar al menos un dueño, el cual ya tiene que estar registrado.
![image](https://user-images.githubusercontent.com/90158740/153697464-02ca1de8-945d-4f5d-8aaa-167934eefc8c.png)

Vista de creación de predio:
![image](https://user-images.githubusercontent.com/90158740/153697487-4ebbb160-4bba-4f63-8192-6d27d715330f.png)
Predio creado:
![image](https://user-images.githubusercontent.com/90158740/153697501-c16633be-03e8-4650-a2cb-e58e742ac8f9.png)


Para la actualización de la información tanto de los dueños como de los usuarios se puede actualizar agregando a la url de la correspondiente vista el documento del objeto a actualizar o eliminar.

![image](https://user-images.githubusercontent.com/90158740/153697598-694db6e8-9d49-46b5-8289-6ed6beaa2511.png)
En verde está el dato a cambiar y su nuevo valor, y en azul el botón put, para realizar la actualización de los datos.

![image](https://user-images.githubusercontent.com/90158740/153697669-b7435da7-bddd-473f-87c0-46f3fd2fa1c1.png)
Estos son los datos cambiados, para añadir, el botón delete ejecutará la eliminación del objeto de la base de datos

![image](https://user-images.githubusercontent.com/90158740/153697701-ef21674b-4dac-4354-be79-5df9bcd7a2e7.png)
Esto se verá a la hora de eliminar el objeto, para destacar, permite en la misma vista la creación de un nuevo objeto
