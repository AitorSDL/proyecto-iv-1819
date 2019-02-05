Vamos a comentar nuestro fichero Vagrantfile:

[![Captura-de-pantalla-de-2019-02-03-17-52-44.png](https://i.postimg.cc/QxfbnZPg/Captura-de-pantalla-de-2019-02-03-17-52-44.png)](https://postimg.cc/ZCypC2J0)

El primer aspecto a destacar es la variable en **`Vagrant.configure('2')`**. Este **2** indica la versión de la configuración que utilizaremos. Solo hay dos variantes, 1 ó 2.
El 2 indica, como ya explicamos en los comentarios del mismo fichero, que utilizaremos una versión entre 1.1+ y 2.0.x.

La línea **`config.ssh.private_key_path = '~/.ssh/id_rsa'`** nos ahorra tener que estar introduciendo la contraseña cada vez que nos conectamos por SSH.

Las línea siguientes que contienen el **`tenant_id, client_id, client_secret y subscription_id`** reciben los datos con ENV para evitar escribir directamente estos datos, lo cual nos da cierto grado de seguridad para la información relativa a nuestra cuenta Azure.

Los **parámetros** siguientes son para las opciones de la máquina virtual de Azure, como nombre, puertos, versión de disco de la máquina virtual, admin y localización. Hay más opciones pero en nuestro caso establecemos las consideremos oportunas.

Por último establecemos la opcion de **provision**, que indica el fichero que provisionará nuestra máquina virtual, en nuestro caso `playbook.yml`.

Para volver a la documentación principal sobre el despliegue de la aplicación, pinche [aqui](https://github.com/aitorSDL/proyecto-iv-1819/blob/master/doc/despliegueFinal.md).
