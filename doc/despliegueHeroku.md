## Despliegue de la aplicación en Heroku

Para el despliegue de la aplicación hay que seguir unos pasos que explico a continuación.

Como prerrequisito deberemos tener una cuenta en [Heroku](https://www.heroku.com/) a partir de ahí:

1. Creamos nuestra aplicación, en este caso yo estoy utilizando Flask como framework.

2. Instalamos gunicorn y lo indicamos en el fichero requirements.txt

3. Ahora, para que Heroku pueda desplegar nuestra aplicación necesitamos un fichero llamado Procfile en nuestro directorio en el repositorio de GitHub. En este fichero indicamos las órdenes y qué tipo de aplicación es:

`web: gunicorn webApp:app`

Explicamos un poco las órdenes en el [Procfile](https://github.com/aitorSDL/proyecto-iv-1819/blob/master/Procfile):

`web:`: Indicamos el tipo de proceso del que se trata, declara que este proceso irá anclado a enrutamiento a http a Heroku y recibirá solicitudes web cuando sea desplegado

`gunicorn` : es el comando necesario para arrancar un servidor WSGI de Python y así ejecutar la aplicación web.

`webApp:app` : parámero perteneciente a la orden anterior, con él indicamos el nombre del servicio.

A partir de este paso, emplearemos la interfaz que nos proporciona Heroku en su página:

[![Captura](https://i.postimg.cc/rwyj4ypT/Captura-de-pantalla-de-2018-11-26-11-37-49.png)](https://postimg.cc/PPc1sjZV)

Tras esto debemos enlazar nuestra aplicación a nuestro repositorio correspondiente en GitHub:

[![Captura](https://i.postimg.cc/gcD6ZVLw/Captura-de-pantalla-de-2018-11-26-11-45-18.png)](https://postimg.cc/9zDM3qpV)

Y por último, para habilitar el despliegue automático cada vez que se realiza un commit, vamos al apartado siguiente en Heroku y le damos a 'Enable Automatic Deploys':

[![Captura](https://i.postimg.cc/Xqp3X6yk/Captura-de-pantalla-de-2018-11-26-11-46-48.png)](https://postimg.cc/4HkjFMPY)

Para probar por primera vez nuestra aplicación vamos más abajo y pulsamos el botón de 'Deploy branch', una vez haya terminado pulsamos el botón de ir a la aplicación y ya tendríamos nuestra aplicación desplegada en Heroku con despliegue automático habilitado.

