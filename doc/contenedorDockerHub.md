# Creación contenedor en DockerHub

Como primer paso deberemos crear una cuenta en la página de Docker.

A continuación, picaremos en la opción Create y seguidamente Automated Build.

[![Captura](https://i.postimg.cc/2yy0SgHj/Captura-de-pantalla-de-2018-12-12-10-42-58.png)](https://postimg.cc/RJr7Pp52)

Tras esto, elegiremos el repositorio que deseemos y ya tendremos el contenedor creado.

Ahora para que DockerHub realice la configuración para el contenedor deberemos crear un fichero llamado `Dockerfile` en el directorio principal del repositorio elegido anteriormente. En él, escribiremos las órdenes necesarias para que nuestra aplicación pueda ser ejecutada en el contenedor. Como en el propio DockerFile ya tenemos explicadas las órdenes, simplemente comentaremos lo que debe hacer el Dockerfile. Indicaremos el lenguaje de programación, el directorio de trabajo y después copiaremos el contenido del repositorio al directorio. Por último, mediante la orden pip instalaremos los requisitos indicados en el fichero "requirements.txt" y el puerto por el que se lanzará la aplicación. La última línea será indicar la orden requerida para ejecutar la aplicación, en nuestro caso, "python3" y el nombre del fichero a ejecutar.

Así nos quedaría el Dockerfile:

[![Captura-de-pantalla-](https://i.postimg.cc/9QLSVP4y/Captura-de-pantalla-de-2018-12-16-18-20-37.png)](https://postimg.cc/nXQTGDGL)

# Creación despliegue en Heroku para contenedor en DockerHub

Ahora crearemos la aplicación en Heroku como hemos explicado en la [documentación](proyecto-iv-1819/doc/despliegueHeroku.md) de la que disponemos de Heroku. Esta vez necesitaremos unos breves pasos más dado que esta vez alojaremos un contenedor.

Primero creamos el fichero `heroku.yml` el cual tiene como función definir una aplicación en Heroku para un contenedor:

[![Captura-de-pantalla-de-2018-12-12-11-06-31.png](https://i.postimg.cc/qRZQF4rc/Captura-de-pantalla-de-2018-12-12-11-06-31.png)](https://postimg.cc/1nwpnxf4)

Por último, deberemos indicar que se trata de un contenedor y así, estando en el directorio de nuestro repositorio ejecutamos la siguiente orden: `heroku stack:set container --app dockerhub-webapp`
