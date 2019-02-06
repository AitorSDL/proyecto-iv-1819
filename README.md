# Tienda de ropa

[![Build Status](https://travis-ci.org/aitorSDL/proyecto-iv-1819.svg?branch=master)](https://travis-ci.org/aitorSDL/proyecto-iv-1819)

Este proyecto consistirá en el desarrollo de un microservicio de tienda de ropa. El microservicio en cuestión se encargará de manejar el almacén de ropa manipulando los diferentes artículos presentes. Adem´as, para el desarrollo nos serviremos de servicios como Travis para la integración continua y Heroku como plataforma de despliegue de la aplicación, más adelante se detallan estos aspectos

Nombre de proyecto: Microservicio de manejo de almacén de tienda de ropa.

Desarrollado por: Aitor Sarrionandia de León.

# Herramientas

- Como lenguaje de programación emplearemos Python 3.6.5 (Framework Flask mediante virtualenv para controlar actualizaciones de Python).  
- Para base de datos emplearemos PostGreSQL o MongoDB.
- Integración continua Travis CI, elegido por su sencillez y porque es gratuito 
- Tests: pytest.
- Despliegue: Heroku, elegido porque es gratuito, muy cómodo para trabajar y sencillo de entender.
- Contenedor: DockerHub.
- Despliegue en nube: Microsoft Azure

# ¿Por qué este microservicio y estas herramientas?

El manejo de artículos de tiendas, por muy genérico que sea siempre me ha parecido interesante y además he cursado anteriormente una asignatura en la que, mediante una herramienta para creación de servicios web (PrestaShop) pude crear mi propia tienda de ropa. Como lenguaje he escogido Python dado que me parece un lenguaje bastante interesante con mucho potencial y versatilidad.

# ¿Qué hace el microservicio?

El microservicio recibirá una solicitud con una determinada ID y devolverá la ID, el nombre del artículo (Camiseta), el precio, la talla y el color.

# Tests

Los tests se realizarán con la librería de Python: pytest. Estos tests serán ejecutados por Travis-CI. Para ejecutarlos, escribiremos esta orden:

`pytest tests.py`

# Despliegue

Despliegue https://consultar-ropa.herokuapp.com/status 

En primer lugar, he de decir que la principal razón por la que he escogido Heroku es por la facilidad que ofrece a la hora de configurar la aplicación para su despliegue y, entre otras cosas, la amplia gama de documentación y tutoriales presentes por Internet. La documentación del despliegue a Heroku se encuentra [aqui](https://github.com/aitorSDL/proyecto-iv-1819/blob/master/doc/despliegueHeroku.md) La explicación acerca del fichero Procfile se encuentra en ese mismo fichero.

Enlace a la app: [Consultar ropa](https://consultar-ropa.herokuapp.com/)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://consultar-ropa.herokuapp.com/)

Las rutas para probar la aplicación, de momento, son:
  
  `/status`
  
   `/` : Devuelve las rutas disponibles contenidas en `seller.json`
   
   `/warehouse` : Devuelve todos los items disponibles, contenidos en el fichero `warehouse.json`

# Contenedor


Contenedor: https://dockerhub-webapp.herokuapp.com/

Como contenedor de la aplicación emplearemos DockerHub y una de las razones por las que lo he utilizado es por su sencillez a la hora de crear los automated build y su intuitiva configuración. Toda la documentación acerca de cómo hemos conseguido el uso de DockerHub se encuentra [aqui](https://github.com/aitorSDL/proyecto-iv-1819/blob/master/doc/contenedorDockerHub.md)

DockerHub: https://hub.docker.com/r/aitorsdl/proyecto-iv-1819/


# Despliegue en la nube

Hemos utilizado la herramienta de Microsoft Azure para el despliegue, Ansible para el provisionamiento y Fabric para la automatización del despliegue. Mas documentación acerca de esta última fase [aqui](https://github.com/aitorSDL/proyecto-iv-1819/blob/master/doc/despliegueFinal.md).

Despliegue final: 13.94.168.251/status
DNS: http://azurevm-proyecto.westeurope.cloudapp.azure.com/status
