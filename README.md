# Tienda de ropa

[![Build Status](https://travis-ci.org/aitorSDL/proyecto-iv-1819.png?branch=master)](https://travis-ci.org/aitorSDL/proyecto-iv-1819)

Este proyecto consistirá en el desarrollo de un microservicio de tienda de ropa. El microservicio en cuestión se encargará de manejar el almacén de ropa manipulando los diferentes artículos presentes.

Nombre de proyecto: Microservicio de manejo de almacén de tienda de ropa.

Desarrollado por: Aitor Sarrionandia de León.

# Herramientas

- Como lenguaje de programación emplearemos Python 3.6.5 (Framework Flask mediante virtualenv para controlar actualizaciones de Python).  
- Para la BD utilizaremos MongoDB.
- Para editar texto utilizaremos Notepad++ o gedit.
- Integración continua: Travis.
- Tests: pytest.
- Despliegue: Heroku

# ¿Por qué este microservicio y estas herramientas?

El manejo de artículos de tiendas, por muy genérico que sea siempre me ha parecido interesante y además he cursado anteriormente una asignatura en la que, mediante una herramienta para creación de servicios web (PrestaShop) pude crear mi propia tienda de ropa. Como lenguaje he escogido Python dado que me parece un lenguaje bastante interesante con mucho potencial y versatilidad.

# ¿Qué hace el microservicio?

El microservicio recibirá una solicitud con una determinada ID y devolverá el nombre (por ejemplo: Camiseta de manga larga roja), el tipo (Camiseta), el precio y la ID (que la hemos introducido nosotros para solicitar información sobre dicho objeto).

# Tests

Los tests se realizarán con la librería de Python: pytest. Estos tests serán ejecutados por Travis-CI.

# Despliegue

En primer lugar, he de decir que la principal razón por la que he escogido Heroku es por la facilidad que ofrece a la hora de configurar la aplicación para su despliegue y, entre otras cosas, la amplia gama de documentación y tutoriales presentes por Internet.

Para el despliegue de la aplicación a desarrollar hemos realizado los siguientes pasos:

1. Creamos una cuenta en Heroku

2. Creamos la app y le damos nombre

3. Asociamos nuestra cuenta dee GitHub a Heroku y a partir de ahí desplegamos.

Enlace a la app: [Consultar ropa](https://consultar-ropa.herokuapp.com/)

Para probar status.json entraremos a este [enlace](https://consultar-ropa.herokuapp.com/todo) o simplemente agregando /todo al final de la URL principal.
