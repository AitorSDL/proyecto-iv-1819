## Despliegue de la aplicación en Heroku

Para el despliegue de la aplicación hay que seguir unos pasos que explico a continuación.

Como prerrequisito deberemos tener una cuenta en [Heroku](https://www.heroku.com/) a partir de ahí:

1. Creamos nuestra aplicación, en este caso yo estoy utilizando Flask como framework.

2. Instalamos gunicorn y lo indicamos en el fichero requirements.txt

3. Ahora, para que Heroku pueda desplegar nuestra aplicación necesitamos un fichero llamado Procfile en nuestro directorio en el repositorio de GitHub. En este fichero indicamos las órdenes y qué tipo de aplicación es:

`web: cd src && gunicorn webApp:app --log-file `

Explicamos un poco las órdenes en el [Procfile](https://github.com/aitorSDL/proyecto-iv-1819/blob/master/Procfile):

`cd`: Como probablemente todos sepamos, esta orden nos cambia de directorio de trabajo, en este caso a 'src'.

Parámetro `--log-file`: Indica a bash que los logs producidos por las órdenes anteriores se escriban a un fichero.

A partir de este paso, emplearemos la interfaz que nos proporciona Heroku en su página:

[![Captura](https://i.postimg.cc/rwyj4ypT/Captura-de-pantalla-de-2018-11-26-11-37-49.png)](https://postimg.cc/PPc1sjZV)

Tras esto debemos enlazar nuestra aplicación a nuestro repositorio correspondiente en GitHub:

[![Captura](https://i.postimg.cc/gcD6ZVLw/Captura-de-pantalla-de-2018-11-26-11-45-18.png)](https://postimg.cc/9zDM3qpV)

Y por último, para habilitar el despliegue automático cada vez que se realiza un commit, vamos al apartado siguiente en Heroku y le damos a 'Enable Automatic Deploys':

[![Captura](https://i.postimg.cc/Xqp3X6yk/Captura-de-pantalla-de-2018-11-26-11-46-48.png)](https://postimg.cc/4HkjFMPY)

Para probar por primera vez nuestra aplicación vamos más abajo y pulsamos el botón de 'Deploy branch', una vez haya terminado pulsamos el botón de ir a la aplicación y ya tendríamos nuestra aplicación desplegada en Heroku con despliegue automático habilitado.

