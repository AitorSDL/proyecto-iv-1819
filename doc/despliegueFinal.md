# Despliegue de la aplicación dividida en 3 etapas:

## 1. Provisionamiento con Ansible

Para empezar, he elegido Ansible para el provisionamiento dada su facilidad e intuitividad a la hora de usarlo, y además, gracias a su amplio uso hay una extensa documentación sobre el mismo.
Para el provisionamiento tendremos que crear el fichero `playbook.yml`, y se encontrará en la ruta `provision/`, que trae en él las órdenes necesarias para añadir los archivos o paquetes (entre otros) que que creamos convenientes para el buen funcionamiento de nuestra aplicación. Nuestro `playbook.yml` quedaría así:

[![Captura-de-pantalla-de-2019-02-03-17-15-47.png](https://i.postimg.cc/0QrzXp1C/Captura-de-pantalla-de-2019-02-03-17-15-47.png)](https://postimg.cc/r0XyKRmd)

Para una información mas detallada sobre el fichero, pinche [aqui]().

Tras esto, deberemos indicar en el fichero `hosts`, localizado en la ruta `etc/ansible`, quienes utilizarán nuestro fichero. En nuestro caso quedaría así:

[![Captura-de-pantalla-de-2019-02-03-17-24-10.png](https://i.postimg.cc/DyzXYJ10/Captura-de-pantalla-de-2019-02-03-17-24-10.png)](https://postimg.cc/8sqc7CKg)

Si quisiésemos, podríamos cambiar el DNS indicado por la IP correspondiente.

Hecho esto, hemos concluido con la etapa de provisionamiento de la máquina virtual.

## 2. Creación de la máquina virtual con Microsoft Azure y Vagrant.

Una vez tenemos creado el fichero que servirá para la provisión de la máquina virtual, procedemos a la creación de la misma.
En nuestro caso, el profesor JJ nos ha conseguido suscripciones académicas para Azure.

El **primer paso** en esta etapa será instalar los paquetes necesarios para poder utilizar Azure y vagrant. Como la instalación de paquetes es la misma para todas las distribuciones Debian o Ubuntu, puede acceder [aqui](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest) para seguir la guía de instalación de **Azure CLI**.

Como **segundo paso** accederemos a nuestra cuenta Azure desde el terminal y así posteriormente poder lanzar nuestra máquina virtual. Escribimos `az login` en el terminal y nos llevará al navegador para acceder a nuestra cuenta Azure, unos segundos después, mostrará información sobre nuestra cuenta Azure en el terminal.

El **tercer paso** consiste en crear nuestro **Azure Active Directory**, el cual será necesario para poder ver los datos necesarios relativos a nuestra cuenta para la creación de la máquina virtual con **Vagrant**. Escribimos esto en el terminal:

[![Captura-de-pantalla-de-2019-02-01-12-24-26.png](https://i.postimg.cc/4xgqvgDJ/Captura-de-pantalla-de-2019-02-01-12-24-26.png)](https://postimg.cc/QHffsRNP)

Esto nos habrá creado un AAD con el nombre "tiendaropa" y además, como podemos observar, nos facilita unos datos los cuales utilizaremos a continuación.

Como podemos ver en la imagen, deberemos exportar:

  - **AZURE_CLIENT_ID**, que se corresponde con `appID`.
  - **AZURE_CLIENT_SECRET**, que se corresponde con `password`.
  - **AZURE_TENANT_ID**, que se corresponde con `tenant`.
  
Ahora solo nos queda una variable, **AZURE_SUBSCRIPTION_ID**, la información de ésta se obtiene, o bien accediendo a nuestra cuenta de Azure desde el navegador, o bien escribiendo `az account list --query "[?isDefault].id" -o tsv` copiamos la información que ha mostrado la orden y exportamos la información al igual que con las variables anteriores.

En el **cuarto paso** trataremos la creación del Vagrantfile, este fichero será necesario para poder utilizar Vagrant, y en él especificaremos órdenes que contendrán la información necesaria para el funcionamiento de nuestra máquina virtual. Tenemos:

[![Captura-de-pantalla-de-2019-02-03-17-52-44.png](https://i.postimg.cc/QxfbnZPg/Captura-de-pantalla-de-2019-02-03-17-52-44.png)](https://postimg.cc/ZCypC2J0)

Para información más detallada acerca de nuestro Vagrantfile, pinche [aqui]().

Como **quinto paso** instalaremos el plugin de Vagrant y Azure con la orden `vagrant plugin install vagrant-azure`. Y a continuación, ya estamos preparados para la creación de la máquina virtual, y escribimos en el terminal: `vagrant up --provider=azure`. Si todo ha ido bien, deberíamos ya tener la máquina virtual creada y los paquetes especificados en el `playbook.yml` instalado. Ya podemos comprobar el funcionamiento de la máquina virtual mediante **SSH**, escribimos en el terminal `vagrant ssh`:

[![Captura-de-pantalla-de-2019-02-03-18-01-19.png](https://i.postimg.cc/Y91NNhTR/Captura-de-pantalla-de-2019-02-03-18-01-19.png)](https://postimg.cc/DJwbnyv4)

Y ya hemmos terminado con la segunda etapa de nuestro despliegue.

## 3. Despliegue con Fabric.

Para poder agilizar el despliegue de la aplicación, nos hemos servido de **Fabric**, una herramienta utilizada para la automatización de despliegues de aplicaciones, la cual funciona mediante SSH.

En **primer lugar**, deberemos crear el fichero `fabfile.py` el cual estará localizado en la ruta `despliegue/`. Nuestro fichero quedará así:

[![Captura-de-pantalla-de-2019-02-03-18-11-59.png](https://i.postimg.cc/BvtPQXqb/Captura-de-pantalla-de-2019-02-03-18-11-59.png)](https://postimg.cc/sBdgTfGC)

Este fichero contendrá unas órdenes muy simples (aunque podemos añadirle las funciones que queramos) ya que solo queremos utilizarlo para levantar el servicio y para actualizarlo. Para ejecutar una función de este fichero en el terminal, basta con escribir: `fab -f despliegue/fabfile.py -H vagrant@<nombrededominio.com> <funcion>`. Cabe decir que las funciones las escribiremos como `init_service` y no `init_service()`.
