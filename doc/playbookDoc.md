Tenemos nuestro `playbook.yml`:

[![Captura-de-pantalla-de-2019-02-03-17-15-47.png](https://i.postimg.cc/0QrzXp1C/Captura-de-pantalla-de-2019-02-03-17-15-47.png)](https://postimg.cc/r0XyKRmd)

En primer lugar se pueden observar las tres primeras líneas, con ellas establecemos:
  - `hosts: all`: permitimos **todos los hosts**, sin restricciones.
  - `become: true`: permitimos que el usuario pueda escalar a **root** cuando sea necesario. Si quisiésemos podríamos establecerlo para cada orden que queramos y no en general como hemos hecho en nuestro caso.
  - `remote_user: vagrant`: indicamos el usuario que utilizará este fichero, el cual será **vagrant**.
  
 En las siguientes líneas podemos ver que son ordenes para instalar paquetes, aplicaciones y por último clonar nuestro repositorio git, por lo que comentaremos qué significa cada opción:
  - `name: `: indicamos el nombre que queramos para la orden que ejecutará el `playbook.yml`.
  - `command: `: indicamos la orden directamente. Por ejemplo: `sudo apt-get update`.
  - `apt_repository: `: indicamos la adición de un repositorio a nuestra lista de repositorios.
  - `state: `: indicamos el estado para el paquete o aplicación que estamos instalando. Hay varios "flags":
    - `present` o `installed`: simplemente se asegura de que está instalado.
    - `latest`: se asegura de que además de instalado, esté también actualizado.
    En nuestro caso, hemos establecido `present` para evitar posible problemas entre versiones.
  - `pkg: `: indicamos el nombre del paquete que queremos instalar.
  - `git: `: se ejecutará una orden git.
    
