# Creación contenedor en DockerHub

Como primer paso deberemos crear una cuenta en la página de Docker.

A continuación, picaremos en la opción Create y seguidamente Automated Build.

[![Captura](https://i.postimg.cc/2yy0SgHj/Captura-de-pantalla-de-2018-12-12-10-42-58.png)](https://postimg.cc/RJr7Pp52)

Tras esto, elegiremos el repositorio que deseemos y ya tendremos el contenedor creado.

Ahora para que DockerHub realice la configuración para el contenedor deberemos crear un fichero llamado `Dockerfile` en el directorio principal del repositorio elegido anteriormente. En él, escribiremos las órdenes necesarias para que nuestra aplicación pueda ser ejecutada en el contenedor. Como en el propio DockerFile ya tenemos explicadas las órdenes, simplemente comentaremos lo que debe hacer el Dockerfile. Indicaremos el lenguaje de programación, el directorio de trabajo y después copiaremos el contenido del repositorio al directorio. Por último, mediante la orden pip instalaremos los requisitos indicados en el fichero "requirements.txt" y el puerto por el que se lanzará la aplicación. La última línea será indicar la orden requerida para ejecutar la aplicación, en nuestro caso, "python3" y el nombre del fichero a ejecutar.

Así nos quedaría el Dockerfile:

[![Captura-de-pantalla-](https://i.postimg.cc/9QLSVP4y/Captura-de-pantalla-de-2018-12-16-18-20-37.png)](https://postimg.cc/nXQTGDGL)

Ahora explicaremos por qué estas órdenes:

En primer lugar, uso esta versión de python porque es la que uso desde que empecé el proyecto y no he querido cambiar de versión por cuestiones de comodidad y prevención de errores por cambio de versión. En segundo lugar, creo el directorio de trabajo de la aplicación y copio solo los archivos necesarios, que son los ficheros python necesarios para la aplicación, los tests, para que se lleven a cabo también en el contenedor y el archivo .json que se usa en la ruta /status. En tercer lugar, instalo las bibliotecas necesarias mediante el archivo `requirement.tx`, a continuación abro el puerto 5000 que es por el que se lanzará la aplicación. Por último indicamos la orden que deberá ejecutar el contenedor la cual es `gunicorn`.

Creamos la imagen en local mediante la siguiente orden:

[![Captura-de-pantalla-de-2019-01-14-19-00-40.png](https://i.postimg.cc/zDj7ptTQ/Captura-de-pantalla-de-2019-01-14-19-00-40.png)](https://postimg.cc/CdRbx4PC)
[![Captura-de-pantalla-de-2019-01-14-19-00-53.png](https://i.postimg.cc/MHFjNQ6n/Captura-de-pantalla-de-2019-01-14-19-00-53.png)](https://postimg.cc/fSYL0k0s)
[![Captura-de-pantalla-de-2019-01-14-19-01-05.png](https://i.postimg.cc/MHvn7p7q/Captura-de-pantalla-de-2019-01-14-19-01-05.png)](https://postimg.cc/7JrPDDtW)
# Creación despliegue en Heroku para contenedor en DockerHub

Ahora crearemos la aplicación en Heroku como hemos explicado en la [documentación](proyecto-iv-1819/doc/despliegueHeroku.md) de la que disponemos de Heroku. Esta vez necesitaremos unos breves pasos más dado que esta vez alojaremos un contenedor.

Primero creamos el fichero `heroku.yml` el cual tiene como función definir una aplicación en Heroku para un contenedor:

[![Captura-de-pantalla-de-2018-12-12-11-06-31.png](https://i.postimg.cc/qRZQF4rc/Captura-de-pantalla-de-2018-12-12-11-06-31.png)](https://postimg.cc/1nwpnxf4)

Por último, deberemos indicar que se trata de un contenedor y así, estando en el directorio de nuestro repositorio ejecutamos la siguiente orden: `heroku stack:set container --app dockerhub-webapp`
